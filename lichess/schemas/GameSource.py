"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameSource.yaml
"""

from typing import Literal


GameSource = Literal[
    "lobby", "friend", "ai", "api", "tournament", "position", "import", "importlive", "simul", "relay", "pool", "swiss"
]
