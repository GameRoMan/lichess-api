from typing import Literal

from ._internal import JsonDeserializable

from .GameSource import GameSource
from .GameStatus import GameStatus
from .Speed import Speed


class GameEventInfo(JsonDeserializable):
    """
    GameEventInfo

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventInfo.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self,
        fullId: str,
        gameId: str,
        fen: str,
        color: Literal["white", "black"],
        lastMove: str,
        source: GameSource,
        status: object,
        variant: object,
        speed: Speed,
        perf: str,
        rated: bool,
        hasMoved: bool,
        opponent: object,
        isMyTurn: bool,
        secondsLeft: int,
        compat: object,
        id: str,
    ):
        self.fullId = fullId
        self.gameId = gameId
        self.fen = fen
        self.color: Literal["white", "black"] = color
        self.lastMove = lastMove
        self.source: GameSource = source
        self.status = status
        self.variant = (variant,)
        self.speed: Speed = speed
        self.perf = perf
        self.rated = rated
        self.hasMoved = hasMoved
        self.opponent = (opponent,)
        self.isMyTurn = isMyTurn
        self.secondsLeft = secondsLeft
        self.compat = compat
        self.id = id
