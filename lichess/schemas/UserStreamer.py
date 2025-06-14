from pydantic import BaseModel


class UserStreamer(BaseModel):
    """
    UserStreamer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserStreamer.yaml
    """

    twitch: object
    youtube: object
