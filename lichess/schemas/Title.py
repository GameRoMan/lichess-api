"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Title.yaml
"""

from typing import Literal


Title = Literal["GM", "WGM", "IM", "WIM", "FM", "WFM", "NM", "CM", "WCM", "WNM", "LM", "BOT"]
