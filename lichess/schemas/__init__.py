"""
See https://github.com/lichess-org/api/tree/master/doc/specs/schemas
"""

from .ArenaPerf import ArenaPerf
from .ArenaPosition import ArenaPosition
from .ArenaRatingObj import ArenaRatingObj
from .ArenaSheet import ArenaSheet
from .ArenaStatus import ArenaStatus
from .ArenaStatusName import ArenaStatusName
from .ArenaTournament import ArenaTournament
from .ArenaTournamentPlayed import ArenaTournamentPlayed
from .ArenaTournamentPlayer import ArenaTournamentPlayer
from .ArenaTournaments import ArenaTournaments

from .ChallengeCanceledEvent import ChallengeCanceledEvent
from .ChallengeDeclinedEvent import ChallengeDeclinedEvent
from .ChallengeDeclinedJson import ChallengeDeclinedJson
from .ChallengeEvent import ChallengeEvent
from .ChallengeJson import ChallengeJson
from .ChallengeOpenJson import ChallengeOpenJson
from .ChallengeStatus import ChallengeStatus
from .ChallengeUser import ChallengeUser

from .ChatLineEvent import ChatLineEvent
from .Clock import Clock
from .CloudEval import CloudEval
from .Count import Count
from .Crosstable import Crosstable
from .Error import Error
from .Flair import Flair

from .GameColor import GameColor
from .GameCompat import GameCompat
from .GameEventInfo import GameEventInfo
from .GameEventOpponent import GameEventOpponent
from .GameEventPlayer import GameEventPlayer
from .GameFinishEvent import GameFinishEvent
from .GameFullEvent import GameFullEvent
from .GameJson import GameJson
from .GameSource import GameSource
from .GameStartEvent import GameStartEvent
from .GameStateEvent import GameStateEvent
from .GameStatus import GameStatus
from .GameStatusId import GameStatusId
from .GameStatusName import GameStatusName
from .GameUser import GameUser

from .Leaderboard import Leaderboard
from .LightUser import LightUser
from .NotFound import NotFound
from .OAuthError import OAuthError
from .Ok import Ok
from .OpponentGoneEvent import OpponentGoneEvent
from .Perf import Perf
from .Perfs import Perfs
from .PerfType import PerfType
from .PlayTime import PlayTime
from .Profile import Profile
from .PuzzleModePerf import PuzzleModePerf
from .Simul import Simul
from .Speed import Speed
from .SwissStatus import SwissStatus
from .SwissTournament import SwissTournament
from .Team import Team
from .TimeControl import TimeControl
from .Title import Title
from .TopUser import TopUser
from .TvGame import TvGame
from .UciVariant import UciVariant
from .User import User
from .UserNote import UserNote
from .UserStreamer import UserStreamer
from .Variant import Variant
from .VariantKey import VariantKey
from .Verdicts import Verdicts


__all__ = [
    "ArenaPerf",
    "ArenaPosition",
    "ArenaRatingObj",
    "ArenaSheet",
    "ArenaStatus",
    "ArenaStatusName",
    "ArenaTournament",
    "ArenaTournamentPlayed",
    "ArenaTournamentPlayer",
    "ArenaTournaments",
    "ChallengeCanceledEvent",
    "ChallengeDeclinedEvent",
    "ChallengeDeclinedJson",
    "ChallengeEvent",
    "ChallengeJson",
    "ChallengeOpenJson",
    "ChallengeStatus",
    "ChallengeUser",
    "ChatLineEvent",
    "Clock",
    "CloudEval",
    "Count",
    "Crosstable",
    "Error",
    "Flair",
    "GameColor",
    "GameCompat",
    "GameEventInfo",
    "GameEventOpponent",
    "GameEventPlayer",
    "GameFinishEvent",
    "GameFullEvent",
    "GameJson",
    "GameSource",
    "GameStartEvent",
    "GameStateEvent",
    "GameStatus",
    "GameStatusId",
    "GameStatusName",
    "GameUser",
    "Leaderboard",
    "LightUser",
    "NotFound",
    "OAuthError",
    "Ok",
    "OpponentGoneEvent",
    "Perf",
    "Perfs",
    "PerfType",
    "PlayTime",
    "Profile",
    "PuzzleModePerf",
    "Simul",
    "Speed",
    "SwissStatus",
    "SwissTournament",
    "Team",
    "TimeControl",
    "Title",
    "TopUser",
    "TvGame",
    "UciVariant",
    "User",
    "UserNote",
    "UserStreamer",
    "Variant",
    "VariantKey",
    "Verdicts",
]
