from ._internal import JsonDeserializable


class TimeControl(JsonDeserializable):
    """
    TimeControl

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TimeControl.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, type: str, limit: int, increment: int, show: str, daysPerTurn: int):
        self.type = type
