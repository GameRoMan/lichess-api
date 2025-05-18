from ._internal import JsonDeserializable


class GameEventOpponent(JsonDeserializable):
    """
    GameEventOpponent

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameEventOpponent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, id: str, username: str, rating: int, **kwargs):
        self.id = id
        self.username = username
        self.rating = rating
