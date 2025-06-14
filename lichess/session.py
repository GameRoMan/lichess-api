from typing import Any, Generic, Literal, TypeVar, overload
from collections.abc import Callable, Iterator, Mapping

import logging

from urllib.parse import urljoin

import requests


from .formats import FormatHandler
from . import utils


logger = logging.getLogger("Lichess")

T = TypeVar("T")
U = TypeVar("U")

Params = Mapping[str, int | bool | str | None]
Data = str | Params
Converter = Callable[[T], T]
Json = dict[str, Any]


class Requestor(Generic[T]):
    """Encapsulates the logic for making a request.

    :param session: the authenticated session object
    :param str base_url: the base URL for requests
    :param default_fmt: default format handler to use
    """

    def __init__(self, session: requests.Session, base_url: str, default_fmt: FormatHandler[T]):
        self.session = session
        self.base_url = base_url
        self.default_fmt = default_fmt

    def request(
        self,
        method: str,
        path: str,
        *,
        stream: bool = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[Any] | None = None,
        converter: Converter[Any] = utils.noop,
        **kwargs: Any,
    ) -> Any | Iterator[Any]:
        """Make a request for a resource in a paticular format.

        :param method: HTTP verb
        :param path: the URL suffix
        :param stream: whether to stream the response
        :param params: request query parametrs
        :param data: request body data (url-encoded)
        :param json: request body json
        :param fmt: the format handler
        :param converter: function to handle field conversions
        :return: response
        :raises berserk.exceptions.ResponseError: if the status is >=400
        """

        fmt = fmt or self.default_fmt
        url = urljoin(self.base_url, path)

        logger.debug(
            "%s %s %s params=%s data=%s json=%s",
            "stream" if stream else "request",
            method,
            url,
            params,
            data,
            json,
        )
        try:
            response = self.session.request(
                method,
                url,
                stream=stream,
                params=params,
                headers=fmt.headers,
                data=data,
                json=json,
                **kwargs,
            )
        except requests.RequestException as e:
            raise Exception(e) from e
        if not response.ok:
            raise Exception(response)

        return fmt.handle(response, is_stream=stream, converter=converter)

    @overload
    def get(
        self,
        path: str,
        *,
        stream: Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[U],
        converter: Converter[U] = utils.noop,
        **kwargs: Any,
    ) -> U: ...

    @overload
    def get(
        self,
        path: str,
        *,
        stream: Literal[True],
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[U],
        converter: Converter[U] = utils.noop,
        **kwargs: Any,
    ) -> Iterator[U]: ...

    @overload
    def get(
        self,
        path: str,
        *,
        stream: Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: None = None,
        converter: Converter[T] = utils.noop,
        **kwargs: Any,
    ) -> T: ...

    @overload
    def get(
        self,
        path: str,
        *,
        stream: Literal[True],
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: None = None,
        converter: Converter[T] = utils.noop,
        **kwargs: Any,
    ) -> Iterator[T]: ...

    def get(
        self,
        path: str,
        *,
        stream: Literal[True] | Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[Any] | None = None,
        converter: Any = utils.noop,
        **kwargs: Any,
    ) -> Any | Iterator[Any]:
        """Convenience method to make a GET request."""
        return self.request(
            "GET",
            path,
            params=params,
            stream=stream,
            fmt=fmt,
            converter=converter,
            data=data,
            json=json,
            **kwargs,
        )

    @overload
    def post(
        self,
        path: str,
        *,
        stream: Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[U],
        converter: Converter[U] = utils.noop,
        **kwargs: Any,
    ) -> U: ...

    @overload
    def post(
        self,
        path: str,
        *,
        stream: Literal[True],
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[U],
        converter: Converter[U] = utils.noop,
        **kwargs: Any,
    ) -> Iterator[U]: ...

    @overload
    def post(
        self,
        path: str,
        *,
        stream: Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: None = None,
        converter: Converter[T] = utils.noop,
        **kwargs: Any,
    ) -> T: ...

    @overload
    def post(
        self,
        path: str,
        *,
        stream: Literal[True],
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: None = None,
        converter: Converter[T] = utils.noop,
        **kwargs: Any,
    ) -> Iterator[T]: ...

    def post(
        self,
        path: str,
        *,
        stream: Literal[True] | Literal[False] = False,
        params: Params | None = None,
        data: Data | None = None,
        json: Json | None = None,
        fmt: FormatHandler[Any] | None = None,
        converter: Any = utils.noop,
        **kwargs: Any,
    ) -> Any | Iterator[Any]:
        """Convenience method to make a POST request."""
        return self.request(
            "POST",
            path,
            params=params,
            stream=stream,
            fmt=fmt,
            converter=converter,
            data=data,
            json=json,
            **kwargs,
        )


class TokenSession(requests.Session):
    """Session capable of Lichess Personal API access token authentication.

    :param token: Lichess Personal API access token,
                  obtained from https://lichess.org/account/oauth/token
    """

    def __init__(self, token: str):
        super().__init__()
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}
