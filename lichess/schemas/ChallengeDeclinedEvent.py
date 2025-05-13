from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeCanceledJson import ChallengeCanceledJson


class ChallengeDeclinedEvent(JsonDeserializable):
    """
    ChallengeDeclinedEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeDeclinedEvent.yaml
    """
    @classmethod
    def de_json(cls, json_string: str | dict):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, type: Literal['challengeDeclined'], challenge: ChallengeCanceledJson):
        self.type: Literal['challengeDeclined'] = type
        self.challenge = challenge
