from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeJson import ChallengeJson
from .GameCompat import GameCompat


class ChallengeEvent(JsonDeserializable):
    """
    ChallengeEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "challenge" in obj:
            obj["challenge"] = ChallengeJson.de_json(obj.get("challenge"))
        if "compat" in obj:
            obj["compat"] = GameCompat.de_json(obj.get("compat"))
        return cls(**obj)

    def __init__(
        self,
        *,
        type: Literal["challenge"],
        challenge: ChallengeJson,
        compat: GameCompat | None = None,
        **kwargs,
    ):
        self.type: Literal["challenge"] = type
        self.challenge = challenge
        self.compat = compat
