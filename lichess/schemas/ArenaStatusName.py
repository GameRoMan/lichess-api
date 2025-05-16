"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaStatusName.yaml
"""

from typing import Literal


ArenaStatusName = Literal["created", "started", "finished"]
