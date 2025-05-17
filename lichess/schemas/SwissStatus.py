"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/SwissStatus.yaml
"""

from typing import Literal


SwissStatus = Literal["created", "started", "finished"]
