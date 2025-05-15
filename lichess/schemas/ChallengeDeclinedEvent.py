from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeDeclinedJson import ChallengeDeclinedJson


class ChallengeDeclinedEvent(JsonDeserializable):
    """
    ChallengeDeclinedEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "challenge" in obj:
            obj["challenge"] = ChallengeDeclinedJson.de_json(obj.get("challenge"))
        return cls(**obj)

    def __init__(self, type: Literal["challengeDeclined"], challenge: ChallengeDeclinedJson):
        self.type: Literal["challengeDeclined"] = type
        self.challenge = challenge
