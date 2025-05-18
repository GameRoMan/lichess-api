from ._internal import JsonDeserializable

from .GameStatusId import GameStatusId
from .GameStatusName import GameStatusName


class GameStatus(JsonDeserializable):
    """
    GameStatus

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatus.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, id: GameStatusId, name: GameStatusName, **kwargs):
        self.id: GameStatusId = id
        self.name: GameStatusName = name
