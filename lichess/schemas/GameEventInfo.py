from pydantic import BaseModel

from .GameColor import GameColor
from .GameSource import GameSource
from .GameStatus import GameStatus
from .Variant import Variant
from .Speed import Speed
from .GameEventOpponent import GameEventOpponent
from .GameCompat import GameCompat


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
