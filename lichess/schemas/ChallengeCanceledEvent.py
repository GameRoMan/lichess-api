from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeJson import ChallengeJson


class ChallengeCanceledEvent(JsonDeserializable):
    """
    ChallengeCanceledEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeCanceledEvent.yaml
    """
    @classmethod
    def de_json(cls, json_string: str | dict):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, type: Literal['challengeCanceled'], challenge: ChallengeJson):
        self.type: Literal['challengeCanceled'] = type
        self.challenge = challenge
