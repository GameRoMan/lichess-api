from typing import Literal


GameStatusName = Literal[
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

"""
GameStatusName

See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatusName.yaml
"""
