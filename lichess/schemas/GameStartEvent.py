from typing import Literal

from ._internal import JsonDeserializable

from .GameEventInfo import GameEventInfo


class GameStartEvent(JsonDeserializable):
    """
    GameStartEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStartEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "game" in obj:
            obj["game"] = GameEventInfo.de_json(obj.get("game"))
        return cls(**obj)

    def __init__(self, type: Literal["gameStart"], game: GameEventInfo, **kwargs):
        self.type: Literal["gameStart"] = type
        self.game = game
