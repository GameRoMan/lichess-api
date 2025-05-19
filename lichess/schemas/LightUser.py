from ._internal import JsonDeserializable

from .Flair import Flair
from .Title import Title


class LightUser(JsonDeserializable):
    """
    LightUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/LightUser.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self,
        *,
        id: str,
        name: str,
        flair: Flair | None = None,
        title: Title | None = None,
        patron: bool | None = None,
        **kwargs,
    ):
        self.id = id
        self.name = name
        self.flair = flair
        self.title: Title | None = title
        self.patron = patron
