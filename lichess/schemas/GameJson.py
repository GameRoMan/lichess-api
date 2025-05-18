from typing import Literal

from ._internal import JsonDeserializable

from .VariantKey import VariantKey
from .Speed import Speed
from .GameStatusName import GameStatusName
from .GameUser import GameUser
from .GameMoveAnalysis import GameMoveAnalysis


class GameJson(JsonDeserializable):
    """
    GameJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameJson.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        return cls(**obj)

    def __init__(
        self,
        id: str,
        rated: bool,
        variant: VariantKey,
        speed: Speed,
        perf: str,
        createdAt: int,
        lastMoveAt: int,
        status: GameStatusName,
        players: object,
        source: str | None = None,
        initialFen: str | None = None,
        winner: Literal["white", "black"] | None = None,
        opening: object | None = None,
        moves: str | None = None,
        pgn: str | None = None,
        daysPerTurn: int | None = None,
        analysis: tuple[GameMoveAnalysis, ...] | None = None,
        tournament: str | None = None,
        swiss: str | None = None,
        clock: object | None = None,
        clocks: tuple[int, ...] | None = None,
        division: object | None = None,
        **kwargs,
    ):
        self.id = id
        self.rated = rated
        self.variant: VariantKey = variant
        self.speed: Speed = speed
        self.perf = perf
        self.createdAt = createdAt
        self.lastMoveAt = lastMoveAt
        self.status: GameStatusName = status
        self.players = players
        self.source = source
        self.initialFen = initialFen
        self.winner: Literal["white", "black"] | None = winner
        self.opening = opening
        self.moves = moves
        self.pgn = pgn
        self.daysPerTurn = daysPerTurn
        self.analysis = analysis
        self.tournament = tournament
        self.swiss = swiss
        self.clock = clock
        self.clocks = clocks
        self.division = division
