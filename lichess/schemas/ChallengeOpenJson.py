from typing import Literal

from pydantic import BaseModel

from . import ChallengeStatus, Variant, Speed, TimeControl, GameColor


class ChallengeOpenJson(BaseModel):
    """
    ChallengeOpenJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeOpenJson.yaml
    """

    id: str
    url: str
    status: ChallengeStatus
    challenger: None
    destUser: None
    variant: Variant
    rated: bool
    speed: Speed
    timeControl: TimeControl
    color: Literal["white", "black", "random"]
    finalColor: GameColor | None = None
    perf: object
    initialFen: str | None = None
    urlWhite: str
    urlBlack: str
    open: object
