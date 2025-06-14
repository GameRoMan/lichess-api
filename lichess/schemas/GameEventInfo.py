from pydantic import BaseModel

from . import GameColor, GameSource, GameStatus, Variant, Speed, GameEventOpponent, GameCompat


class GameEventInfo(BaseModel):
    """
    GameEventInfo

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventInfo.yaml
    """

    fullId: str
    gameId: str
    fen: str
    color: GameColor
    lastMove: str
    source: GameSource
    status: GameStatus
    variant: Variant
    speed: Speed
    perf: str
    rated: bool
    hasMoved: bool
    opponent: GameEventOpponent
    isMyTurn: bool
    secondsLeft: int
    compat: GameCompat
    id: str
