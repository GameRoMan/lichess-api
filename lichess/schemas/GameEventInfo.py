from ._internal import JsonDeserializable

from .GameColor import GameColor
from .GameSource import GameSource
from .GameStatus import GameStatus
from .Variant import Variant
from .Speed import Speed
from .GameEventOpponent import GameEventOpponent
from .GameCompat import GameCompat


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
        if "status" in obj:
            obj["status"] = GameStatus.de_json(obj.get("status"))
        if "variant" in obj:
            obj["variant"] = Variant.de_json(obj.get("variant"))
        if "opponent" in obj:
            obj["opponent"] = GameEventOpponent.de_json(obj.get("opponent"))
        if "compat" in obj:
            obj["compat"] = GameCompat.de_json(obj.get("compat"))
        return cls(**obj)

    def __init__(
        self,
        *,
        fullId: str,
        gameId: str,
        fen: str,
        color: GameColor,
        lastMove: str,
        source: GameSource,
        status: GameStatus,
        variant: Variant,
        speed: Speed,
        perf: str,
        rated: bool,
        hasMoved: bool,
        opponent: GameEventOpponent,
        isMyTurn: bool,
        secondsLeft: int,
        compat: GameCompat,
        id: str,
        **kwargs,
    ):
        self.fullId = fullId
        self.gameId = gameId
        self.fen = fen
        self.color: GameColor = color
        self.lastMove = lastMove
        self.source: GameSource = source
        self.status = status
        self.variant = variant
        self.speed: Speed = speed
        self.perf = perf
        self.rated = rated
        self.hasMoved = hasMoved
        self.opponent = opponent
        self.isMyTurn = isMyTurn
        self.secondsLeft = secondsLeft
        self.compat = compat
        self.id = id
