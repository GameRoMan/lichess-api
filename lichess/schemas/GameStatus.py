"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatus.yaml
"""

from typing import Literal


GameStatus = Literal[
    "created",
    "started",
    "aborted",
    "mate",
    "resign",
    "stalemate",
    "timeout",
    "draw",
    "outoftime",
    "cheat",
    "noStart",
    "unknownFinish",
    "variantEnd",
]
