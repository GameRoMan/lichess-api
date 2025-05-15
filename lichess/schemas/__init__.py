"""
See https://github.com/lichess-org/api/tree/master/doc/specs/schemas
"""

from .ArenaPerf import ArenaPerf
from .ArenaPosition import ArenaPosition
from .ChallengeCanceledEvent import ChallengeCanceledEvent
from .ChallengeDeclinedEvent import ChallengeDeclinedEvent
from .ChallengeDeclinedJson import ChallengeDeclinedJson
from .ChallengeEvent import ChallengeEvent
from .ChallengeJson import ChallengeJson
from .ChallengeStatus import ChallengeStatus
from .ChallengeUser import ChallengeUser
from .ChatLineEvent import ChatLineEvent
from .Clock import Clock
from .Count import Count
from .Error import Error
from .Flair import Flair
from .GameEventInfo import GameEventInfo
from .GameEventPlayer import GameEventPlayer
from .GameFinishEvent import GameFinishEvent
from .GameFullEvent import GameFullEvent
from .GameSource import GameSource
from .GameStartEvent import GameStartEvent
from .GameStateEvent import GameStateEvent
from .GameStatus import GameStatus
from .LightUser import LightUser
from .NotFound import NotFound
from .OAuthError import OAuthError
from .Ok import Ok
from .OpponentGone import OpponentGone
from .Perf import Perf
from .Perfs import Perfs
from .PerfType import PerfType
from .PlayTime import PlayTime
from .Profile import Profile
from .PuzzleModePerf import PuzzleModePerf
from .Speed import Speed
from .TimeControl import TimeControl
from .Title import Title
from .TvGame import TvGame
from .UserNote import UserNote
from .Variant import Variant
from .VariantKey import VariantKey


__all__ = [
    "ArenaPerf",
    "ArenaPosition",
    "ChallengeCanceledEvent",
    "ChallengeDeclinedEvent",
    "ChallengeDeclinedJson",
    "ChallengeEvent",
    "ChallengeJson",
    "ChallengeStatus",
    "ChallengeUser",
    "ChatLineEvent",
    "Clock",
    "Count",
    "Error",
    "Flair",
    "GameEventInfo",
    "GameEventPlayer",
    "GameFinishEvent",
    "GameFullEvent",
    "GameSource",
    "GameStartEvent",
    "GameStateEvent",
    "GameStatus",
    "LightUser",
    "NotFound",
    "OAuthError",
    "Ok",
    "OpponentGone",
    "Perf",
    "Perfs",
    "PerfType",
    "PlayTime",
    "Profile",
    "PuzzleModePerf",
    "Speed",
    "TimeControl",
    "Title",
    "TvGame",
    "UserNote",
    "Variant",
    "VariantKey",
]
