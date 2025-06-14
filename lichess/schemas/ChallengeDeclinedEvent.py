from typing import Literal

from pydantic import BaseModel

from . import ChallengeDeclinedJson


class ChallengeDeclinedEvent(BaseModel):
    """
    ChallengeDeclinedEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedEvent.yaml
    """

    type: Literal["challengeDeclined"]
    challenge: ChallengeDeclinedJson
