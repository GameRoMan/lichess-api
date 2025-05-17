from ._internal import JsonDeserializable


class Verdicts(JsonDeserializable):
    """
    Verdicts

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Verdicts.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, accepted: bool, list: tuple[object], **kwargs):
        self.accepted = accepted
        self.iist = list
