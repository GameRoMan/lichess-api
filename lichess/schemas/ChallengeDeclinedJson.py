from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeStatus import ChallengeStatus
from .ChallengeUser import ChallengeUser
from .Variant import Variant
from .Speed import Speed
from .TimeControl import TimeControl


class ChallengeDeclinedJson(JsonDeserializable):
    """
    ChallengeDeclinedJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedJson.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "challenger" in obj:
            obj["challenger"] = ChallengeUser.de_json(obj.get("challenger"))
        if "destUser" in obj:
            obj["destUser"] = ChallengeUser.de_json(obj.get("destUser"))
        if "variant" in obj:
            obj["variant"] = Variant.de_json(obj.get("variant"))
        if "timeControl" in obj:
            obj["timeControl"] = TimeControl.de_json(obj.get("timeControl"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        url: str,
        status: ChallengeStatus,
        challenger: ChallengeUser,
        destUser: ChallengeUser | None,
        variant: Variant,
        rated: bool,
        speed: Speed,
        timeControl: TimeControl,
        color: Literal["white", "black", "random"],
        finalColor: Literal["white", "black"],
        perf: object,
        direction: Literal["in", "out"],
        initialFen: str,
        declineReason: str,
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
        ],
        **kwargs,
    ):
        self.id = id
        self.url = url
        self.status: ChallengeStatus = status
        self.challenger = challenger
        self.destUser = destUser
        self.variant = variant
        self.rated = rated
        self.speed: Speed = speed
        self.timeControl = timeControl
        self.color: Literal["white", "black", "random"] = color
        self.finalColor: Literal["white", "black"] = finalColor
        self.perf = perf
        self.direction: Literal["in", "out"] = direction
        self.initialFen = initialFen
        self.declineReason = declineReason
        self.declineReasonKey = declineReasonKey
