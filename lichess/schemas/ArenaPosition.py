from typing import Literal

from pydantic import BaseModel, HttpUrl, field_validator


class ThematicPosition(BaseModel):
    eco: str | None = None
    name: str
    fen: str
    url: HttpUrl | None = None


class CustomPosition(BaseModel):
    name: Literal["Custom position"]
    fen: str


ArenaPositionUnion = ThematicPosition | CustomPosition


class ArenaPosition(BaseModel):
    """
    ArenaPosition

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPosition.yaml
    """

    position: ArenaPositionUnion | None = None

    @field_validator("position", mode="before")
    @classmethod
    def parse_position(cls, v):
        if not isinstance(v, dict):
            return v
        if _v.get("name") == "Custom position":
            return CustomPosition(**v)
        # fallback to ThematicPosition
        return ThematicPosition(**v)
