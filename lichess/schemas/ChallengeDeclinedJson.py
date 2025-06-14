from typing import Literal

from pydantic import BaseModel

from . import ChallengeStatus, ChallengeUser, Variant, Speed, TimeControl, GameColor


class ChallengeDeclinedJson(BaseModel):
    """
    ChallengeDeclinedJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedJson.yaml
    """

    id: str
    url: str
    status: ChallengeStatus
    challenger: ChallengeUser
    destUser: ChallengeUser | None
    variant: Variant
    rated: bool
    speed: Speed
    timeControl: TimeControl
    color: Literal["white", "black", "random"]
    finalColor: GameColor | None = None
    perf: object
    direction: Literal["in", "out"] | None = None
    initialFen: str | None = None
    declineReason: str
    declineReasonKey: Literal[
        "generic",
        "later",
        "tooFast",
        "tooSlow",
        "timeControl",
        "rated",
        "casual",
        "standard",
        "variant",
        "noBot",
        "onlyBot",
    ]
