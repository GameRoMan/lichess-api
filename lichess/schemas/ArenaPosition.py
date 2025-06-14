from typing import Annotated, Literal

from pydantic import BaseModel, HttpUrl, Field


class ThematicPosition(BaseModel):
    eco: str | None = None
    name: str
    fen: str
    url: HttpUrl | None = None


class CustomPosition(BaseModel):
    name: Literal["Custom position"]
    fen: str


ArenaPosition = Annotated[ThematicPosition | CustomPosition, Field(discriminator="name")]

"""
ArenaPosition

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPosition.yaml
"""
