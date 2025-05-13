from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeUser import ChallengeUser
from .Variant import Variant
from .Speed import Speed


class ChallengeJson(JsonDeserializable):
    """
    Challenge json

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeJson.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, id: str, url: str, status: Literal['created', 'offline', 'canceled', 'declined', 'accepted'],
        challenger: ChallengeUser, destUser: ChallengeUser | None, variant: Variant, rated: bool, speed: Speed,
        timeControl: object, color: Literal['white', 'black', 'random'], finalColor: Literal['white', 'black'],
        perf: object, direction: Literal['in', 'out'], initialFen: str, declineReason: str, declineReasonKey: str
    ):
        self.id = id
        self.url = url
        self.status: Literal['created', 'offline', 'canceled', 'declined', 'accepted'] = status
        self.challenger = challenger
        self.destUser = destUser
        self.variant = variant
        self.rated = rated
        self.speed = speed
        self.timeControl = timeControl
        self.color: Literal['white', 'black', 'random'] = color
        self.finalColor: Literal['white', 'black'] = finalColor
        self.perf = perf
        self.direction: Literal['in', 'out'] = direction
        self.initialFen = initialFen
        self.declineReason = declineReason
        self.declineReasonKey = declineReasonKey
