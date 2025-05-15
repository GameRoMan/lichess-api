from typing import Literal

from ._internal import JsonDeserializable

from .Variant import Variant
from .Speed import Speed
from .GameEventPlayer import GameEventPlayer
from .GameStateEvent import GameStateEvent


class GameFullEvent(JsonDeserializable):
    """
    GameFullEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameFullEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "variant" in obj:
            obj["variant"] = Variant.de_json(obj.get("variant"))
        if "white" in obj:
            obj["white"] = GameEventPlayer.de_json(obj.get("white"))
        if "black" in obj:
            obj["black"] = GameEventPlayer.de_json(obj.get("black"))
        if "state" in obj:
            obj["state"] = GameStateEvent.de_json(obj.get("state"))
        return cls(**obj)

    def __init__(
        self,
        type: Literal["gameFull"],
        id: str,
        variant: Variant,
        clock: object,
        speed: Speed,
        perf: object,
        rated: bool,
        createdAt: int,
        white: GameEventPlayer,
        black: GameEventPlayer,
        initialFen: str,
        state: GameStateEvent,
        tournamentId: str,
    ):
        self.type: Literal["gameFull"] = type
        self.id = id
        self.variant = variant
        self.clock = clock
        self.speed: Speed = speed
        self.perf = perf
        self.rated = rated
        self.createdAt = createdAt
        self.white = white
        self.black = black
        self.initialFen = initialFen
        self.state = state
        self.tournamentId = tournamentId
