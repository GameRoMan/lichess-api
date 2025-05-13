from .._internal import JsonDeserializable

from ..GameStartEvent import GameStartEvent
from ..GameFinishEvent import GameFinishEvent
from ..ChallengeEvent import ChallengeEvent
from ..ChallengeCanceledEvent import ChallengeCanceledEvent
from ..ChallengeDeclinedEvent import ChallengeDeclinedEvent

import json

class ApiStreamEvent(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        print(json.dumps(obj, indent=2))
        match json_string['type']:
            case 'gameStart':
                return GameStartEvent.de_json(obj)
            case 'gameFinish':
                return GameFinishEvent.de_json(obj)
            case 'challenge':
                return ChallengeEvent.de_json(obj)
            case 'challengeCanceled':
                return ChallengeCanceledEvent.de_json(obj)
            case 'challengeDeclined':
                return ChallengeDeclinedEvent.de_json(obj)
            case _:
                raise Exception('Unkown Event Type')
