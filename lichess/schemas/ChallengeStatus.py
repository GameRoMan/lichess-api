"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeStatus.yaml
"""

from typing import Literal


ChallengeStatus = Literal["created", "offline", "canceled", "declined", "accepted"]
