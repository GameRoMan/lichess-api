from pydantic import BaseModel, HttpUrl

from .Title import Title
from .Flair import Flair
from .Clock import Clock
from .ArenaSheet import ArenaSheet
from .Verdicts import Verdicts
from .ArenaRatingObj import ArenaRatingObj


class Spotlight(BaseModel):
    headline: str


class Quote(BaseModel):
    text: str
    author: str


class GreatPlayer(BaseModel):
    name: str
    url: HttpUrl


class MinRatedGames(BaseModel):
    nb: int


class Perf(BaseModel):
    icon: str
    key: str
    name: str


class Schedule(BaseModel):
    freq: str
    speed: str


class DuelPlayer(BaseModel):
    n: str
    r: int
    k: int


class Duel(BaseModel):
    id: str
    p: tuple[DuelPlayer, DuelPlayer]


class StandingPlayer(BaseModel):
    name: str
    title: Title
    patron: bool
    flair: Flair
    rank: int
    rating: int
    score: int
    sheet: ArenaSheet


class Standing(BaseModel):
    page: int
    players: tuple[StandingPlayer, ...]


class FeaturedPlayer(BaseModel):
    name: str
    id: str
    rank: int
    rating: int


class FeaturedClock(BaseModel):
    white: int
    "white's clock in seconds"
    black: int
    "black's clock in seconds"


class Featured(BaseModel):
    id: str
    fen: str
    orientation: str
    color: str
    lastMove: str
    white: FeaturedPlayer
    black: FeaturedPlayer
    c: FeaturedClock


class PodiumElementNumbers(BaseModel):
    game: int
    berserk: int
    win: int


class PodiumElement(BaseModel):
    name: str
    title: Title
    patron: bool
    flair: Flair
    rank: int
    rating: int
    score: int
    nb: PodiumElementNumbers
    performance: int


class Stats(BaseModel):
    games: int
    moves: int
    whiteWins: int
    blackWins: int
    draws: int
    berserks: int
    averageRating: int


class ArenaTournamentFull(BaseModel):
    """
    ArenaTournamentFull

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentFull.yaml
    """

    id: str
    fullName: str
    rated: bool
    spotlight: Spotlight
    berserkable: bool
    onlyTitled: bool
    clock: Clock
    minutes: int
    createdBy: str
    system: str
    secondsToStart: int
    secondsToFinish: int
    isFinished: bool
    isRecentlyFinished: bool
    pairingsClosed: bool
    startsAt: str
    nbPlayers: int
    verdicts: Verdicts
    quote: Quote
    "The quote displayed on the tournament page"
    greatPlayer: GreatPlayer
    allowList: tuple[str, ...]
    "List of usernames allowed to join the tournament"
    hasMaxRating: bool
    maxRating: ArenaRatingObj
    minRating: ArenaRatingObj
    minRatedGames: MinRatedGames
    botsAllowed: bool
    minAccountAgeInDays: int
    perf: Perf
    schedule: Schedule
    description: str
    variant: str
    duels: Duel
    standing: Standing
    featured: Featured
    podium: tuple[PodiumElement, ...]
    stats: Stats
    myUsername: str
