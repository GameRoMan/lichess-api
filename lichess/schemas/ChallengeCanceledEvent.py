from typing import Literal

from pydantic import BaseModel

from . import ChallengeJson


class ChallengeCanceledEvent(BaseModel):
    """
    ChallengeCanceledEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeCanceledEvent.yaml
    """

    type: Literal["challengeCanceled"]
    challenge: ChallengeJson
