from typing import Literal

from pydantic import BaseModel

from . import ChallengeJson, GameCompat


class ChallengeEvent(BaseModel):
    """
    ChallengeEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeEvent.yaml
    """

    type: Literal["challenge"]
    challenge: ChallengeJson
    compat: GameCompat | None = None
