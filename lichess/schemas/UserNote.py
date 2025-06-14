from pydantic import BaseModel, Field

from . import LightUser


class UserNote(BaseModel):
    """
    UserNote

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserNote.yaml
    """

    from_: LightUser = Field(alias="sss")
    to: LightUser
    text: str
    date: int
