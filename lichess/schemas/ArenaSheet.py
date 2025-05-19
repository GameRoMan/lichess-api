from ._internal import JsonDeserializable


class ArenaSheet(JsonDeserializable):
    """
    ArenaSheet

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaSheet.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, *, scores: str, fire: bool | None = None, **kwargs):
        self.scores = scores
        self.fire = fire
