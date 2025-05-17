from typing import Literal

from ._internal import JsonDeserializable

from .ArenaPerf import ArenaPerf
from .ArenaPosition import ArenaPosition
from .ArenaRatingObj import ArenaRatingObj
from .ArenaStatus import ArenaStatus
from .Clock import Clock
from .LightUser import LightUser
from .Variant import Variant


class ArenaTournament(JsonDeserializable):
    """
    ArenaTournament

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournament.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "variant" in obj:
            obj["variant"] = Variant.de_json(obj.get("variant"))
        if "perf" in obj:
            obj["perf"] = ArenaPerf.de_json(obj.get("perf"))
        if "maxRating" in obj:
            obj["maxRating"] = ArenaRatingObj.de_json(obj.get("maxRating"))
        if "minRating" in obj:
            obj["minRating"] = ArenaRatingObj.de_json(obj.get("minRating"))
        if "position" in obj:
            obj["position"] = ArenaPosition.de_json(obj.get("position"))
        if "winner" in obj:
            obj["winner"] = LightUser.de_json(obj.get("winner"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        createdBy: str,
        system: Literal["arena"],
        minutes: int,
        clock: Clock,
        rated: bool,
        fullName: str,
        nbPlayers: int,
        variant: Variant,
        startsAt: int,
        finishesAt: int,
        status: ArenaStatus,
        perf: ArenaPerf,
        secondsToStart: int | None = None,
        hasMaxRating: bool | None = None,
        maxRating: ArenaRatingObj | None = None,
        minRating: ArenaRatingObj | None = None,
        minRatedGames: object | None = None,
        botsAllowed: bool | None = None,
        minAccountAgeInDays: int | None = None,
        onlyTitled: bool | None = None,
        teamMember: str | None = None,
        private: bool | None = None,
        position: ArenaPosition | None = None,
        schedule: object | None = None,
        teamBattle: object | None = None,
        winner: LightUser | None = None,
        **kwargs,
    ):
        self.id = id
        self.createdBy = createdBy
        self.system: Literal["arena"] = system
        self.minutes = minutes
        self.clock = clock
        self.rated = rated
        self.fullName = fullName
        self.nbPlayers = nbPlayers
        self.variant = variant
        self.startsAt = startsAt
        self.finishesAt = finishesAt
        self.status: ArenaStatus = status
        self.perf = perf
        self.secondsToStart = secondsToStart
        self.hasMaxRating = hasMaxRating
        self.maxRating = maxRating
        self.minRating = minRating
        self.minRatedGames = minRatedGames
        self.botsAllowed = botsAllowed
        self.minAccountAgeInDays = minAccountAgeInDays
        self.onlyTitled = onlyTitled
        self.teamMember = teamMember
        self.private = private
        self.position = position
        self.schedule = schedule
        self.teamBattle = teamBattle
        self.winner = winner
