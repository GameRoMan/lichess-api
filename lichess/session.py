from typing import (
    Any,
    Callable,
    Generic,
    Iterator,
    Literal,
    LiteralString,
    Mapping,
    TypeVar,
    overload,
)

import requests

import logging

from urllib.parse import urljoin


from .formats import FormatHandler
from . import exceptions, utils


API_URL = "https://lichess.org"

CONNECT_TIMEOUT = 15
READ_TIMEOUT = 30


logger = logging.getLogger('Lichess')

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
            raise Exception(e)
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
    ) -> U:
        ...

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
    ) -> Iterator[U]:
        ...

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
    ) -> T:
        ...

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
    ) -> Iterator[T]:
        ...

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
    ) -> U:
        ...

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
    ) -> Iterator[U]:
        ...

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
    ) -> T:
        ...

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
    ) -> Iterator[T]:
        ...

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

    :param token: Lichess Personal API access token, obtained from https://lichess.org/account/oauth/token
    """

    def __init__(self, token: str):
        super().__init__()
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}



def _make_request(session: TokenSession, api_path: LiteralString, method='get', params: dict | None = None, timeout: int | float | None = None):
    raise Exception('DO NOT USE THIS METHOD')
    """
    Makes a request to the Lichess API.

    :param session: Session capable of Lichess Personal API access token authentication
    :type session: `TokenSession`
    :param api_path: Api path. for example "/api/account".
    :type api_path: `str`
    :param method: HTTP method to be used. Defaults to 'get'.
    :type method: `str`
    :param params: Optional parameters. Should be a dictionary with key-value pairs.
    :type method: `dict`
    :return: The result parsed to a JSON dictionary.
    """

    request_url = f"{API_URL}{api_path}"

    read_timeout = READ_TIMEOUT
    connect_timeout = CONNECT_TIMEOUT

    if timeout:
        read_timeout = timeout
        connect_timeout = read_timeout

    params = params or None  # Set params to None if empty
    print('xxx')
    result = session.request(
        method, request_url, params=params,
        timeout=(connect_timeout, read_timeout)
    )
    print(f"{result = }")

    json_result = _check_result(api_path, result)
    if json_result:
        return json_result['result']


def _check_result(api_path: LiteralString, result: requests.Response):
    """
    Checks whether `result` is a valid API response.
    A result is considered invalid if:
        - The server returned an HTTP response code other than 200
        - The content of the result is invalid JSON.
        - The method call was unsuccessful (The JSON 'ok' field equals False)

    :raises ApiException: if one of the above listed cases is applicable
    :param api_path: The name of the method called
    :param result: The returned result of the method request
    :return: The result parsed to a JSON dictionary.
    """

    try:
        result_json = result.json()
    except:
        if result.status_code != 200:
            raise exceptions.ApiHTTPException(api_path, result)
        else:
            raise exceptions.ApiInvalidJSONException(api_path, result)
    else:
        if not result_json['ok']:
            raise exceptions.ApiLichessException(api_path, result, result_json)

        return result_json
