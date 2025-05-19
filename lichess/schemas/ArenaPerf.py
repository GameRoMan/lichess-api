from ._internal import JsonDeserializable


class ArenaPerf(JsonDeserializable):
    """
    Arena performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPerf.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, *, key: str, name: str, position: int, icon: str | None = None, **kwargs):
        self.key = key
        self.name = name
        self.position = position
        self.icon = icon
