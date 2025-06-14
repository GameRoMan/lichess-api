from pydantic import BaseModel

from . import Flair, LightUser


class Team(BaseModel):
    """
    Team

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Team.yaml
    """

    id: str
    name: str
    description: str | None = None
    flair: Flair | None = None
    leader: LightUser | None = None
    leaders: tuple[LightUser, ...] | None = None
    nbMemebers: int | None = None
    open: bool | None = None
    joined: bool | None = None
    requested: bool | None = None
