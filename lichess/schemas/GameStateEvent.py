from typing import Literal

from pydantic import BaseModel

from .GameStatusName import GameStatusName


class GameStateEvent(BaseModel):
    """
    GameState event

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStateEvent.yaml
    """

    type: Literal["gameState"]
    moves: str
    wtime: int
    btime: int
    winc: int
    binc: int
    status: GameStatusName
    winner: str | None = None
    wdraw: bool | None = None
    bdraw: bool | None = None
    wtakeback: bool | None = None
    btakeback: bool | None = None
