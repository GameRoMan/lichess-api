from typing import Literal

from ._internal import JsonDeserializable


class ChatLineEvent(JsonDeserializable):
    """
    ChatLineEvent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChatLineEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, type: Literal["chatLine"], room: Literal["player", "spectator"], username: str, text: str):
        self.type: Literal["chatLine"] = type
        self.room: Literal["player", "spectator"] = room
        self.username = username
        self.text = text
