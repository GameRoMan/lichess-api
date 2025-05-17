from ._internal import JsonDeserializable

from .Flair import Flair
from .LightUser import LightUser


class Team(JsonDeserializable):
    """
    Team

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Team.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "user" in obj:
            obj["user"] = LightUser.de_json(obj.get("user"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        flair: Flair,
        leader: LightUser,
        leaders: tuple[LightUser],
        nbMemebers: int,
        open: bool,
        joined: bool,
        requested: bool,
        **kwargs,
    ): ...
