from ._internal import JsonDeserializable


class GameEventPlayer(JsonDeserializable):
    """
    GameEventPlayer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventPlayer.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, aiLevel: int, id: str, name: str, title: str | None, rating: int, provisional: bool, **kwargs
    ):
        self.aiLevel = aiLevel
        self.id = id
        self.name = name
        self.title = title
        self.rating = rating
        self.provisional = provisional
