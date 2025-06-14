from pydantic import BaseModel

from . import Flair, Title


class LightUser(BaseModel):
    """
    LightUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/LightUser.yaml
    """

    id: str
    name: str
    flair: Flair | None = None
    title: Title | None = None
    patron: bool | None = None
