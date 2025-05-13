from ._internal import JsonDeserializable

from .VariantKey import VariantKey


class Variant(JsonDeserializable):
    """
    Puzzle mode performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Variant.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, key: VariantKey, name: str, short: str):
        self.key = key
        self.name = name
        self.short = short
