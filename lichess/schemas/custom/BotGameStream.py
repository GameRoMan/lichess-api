from .._internal import JsonDeserializable

from ..GameFullEvent import GameFullEvent
from ..GameStateEvent import GameStateEvent
from ..ChatLineEvent import ChatLineEvent
from ..OpponentGoneEvent import OpponentGoneEvent


class BotGameStream(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        match json_string["type"]:
            case "gameFull":
                return GameFullEvent.de_json(obj)
            case "gameState":
                return GameStateEvent.de_json(obj)
            case "chatLine":
                return ChatLineEvent.de_json(obj)
            case "opponentGone":
                return OpponentGoneEvent.de_json(obj)
            case _:
                raise Exception("Unkown Event Type")
