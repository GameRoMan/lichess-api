"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UciVariant.yaml
"""

from typing import Literal


UciVariant = Literal[
    "chess", "crazyhouse", "antichess", "atomic", "horde", "kingofthehill", "racingkings", "3check"
]
