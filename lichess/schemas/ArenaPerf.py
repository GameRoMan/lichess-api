from ._internal import JsonDeserializable

class Perf(JsonDeserializable):
    """
    Performance
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, key: str, name: str, position: int, icon: str):
        self.key = key
        self.name = name
        self.position = position
        self.icon = icon
