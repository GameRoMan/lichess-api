from typing import Literal

from ._internal import JsonDeserializable

from .GameEventInfo import GameEventInfo


class GameFinishEvent(JsonDeserializable):
    """
    GameFinishEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameFinishEvent.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, type: Literal['gameFinish'], game: GameEventInfo):
        self.type: Literal['gameFinish'] = type
        self.game = game
