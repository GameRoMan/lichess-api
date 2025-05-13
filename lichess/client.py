from . import schemas

from .schemas.custom.ApiStreamEvent import ApiStreamEvent

from .session import TokenSession, Requestor, _make_request

from .formats import JSON


# Base URL for the API
API_URL = "https://lichess.org"


class LichessClient:
    """
    Lichess Client

    :param token: Lichess Personal API access token, obtained from https://lichess.org/account/oauth/token
    :type token: `str`
    """

    def __init__(self, token: str, base_url = API_URL):
        self.token = token
        self.session = TokenSession(token)
        self._requestor = Requestor(self.session, base_url or API_URL, default_fmt=JSON)

    def stream_incoming_events(self):
        """
        Get your realtime stream of incoming events. See https://lichess.org/api#tag/Bot/operation/apiStreamEvent

        :return: stream of incoming events
        """
        path = "/api/stream/event"
        
        events = self._requestor.get(path, stream=True)

        return [ApiStreamEvent.de_json(event) for event in events]








# class FmtClient(BaseClient):
#     """Client that can return PGN or not.

#     :param session: request session, authenticated as needed
#     :param base_url: base URL for the API
#     :param pgn_as_default: ``True`` if PGN should be the default format for game exports
#         when possible. This defaults to ``False`` and is used as a fallback when
#         ``as_pgn`` is left as ``None`` for methods that support it.
#     """

#     def __init__(
#         self,
#         session: requests.Session,
#         base_url: str | None = None,
#         pgn_as_default: bool = False,
#     ):
#         super().__init__(session, base_url)
#         self.pgn_as_default = pgn_as_default

#     def _use_pgn(self, as_pgn: bool | None = None):
#         # helper to merge default with provided arg
#         return as_pgn if as_pgn is not None else self.pgn_as_default
