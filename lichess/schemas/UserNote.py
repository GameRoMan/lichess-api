from ._internal import JsonDeserializable

from .LightUser import LightUser


class UserNote(JsonDeserializable):
    """
    UserNote

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserNote.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, from_: LightUser, to: LightUser, text: str, date: int):
        self.from_ = from_
        self.to = to
        self.text = text
        self.date = date
