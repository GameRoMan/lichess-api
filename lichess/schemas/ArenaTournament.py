from typing import Literal

from pydantic import BaseModel

from . import ArenaPerf, ArenaPosition, ArenaRatingObj, ArenaStatus, Clock, LightUser, Variant


class ArenaTournament(BaseModel):
    """
    ArenaTournament

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournament.yaml
    """

    id: str
    createdBy: str
    system: Literal["arena"]
    minutes: int
    clock: Clock
    rated: bool
    fullName: str
    nbPlayers: int
    variant: Variant
    startsAt: int
    finishesAt: int
    status: ArenaStatus
    perf: ArenaPerf

    secondsToStart: int | None = None
    hasMaxRating: bool | None = None
    maxRating: ArenaRatingObj | None = None
    minRating: ArenaRatingObj | None = None
    minRatedGames: object | None = None
    botsAllowed: bool | None = None
    minAccountAgeInDays: int | None = None
    onlyTitled: bool | None = None
    teamMember: str | None = None
    private: bool | None = None
    position: ArenaPosition | None = None
    schedule: object | None = None
    teamBattle: object | None = None
    winner: LightUser | None = None
