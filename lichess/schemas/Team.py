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
        if "leaders" in obj:
            obj["leaders"] = tuple(
                light_user
                for leader in obj.get("leaders", [])
                if (light_user := LightUser.de_json(leader))
            )
        return cls(**obj)

    def __init__(
        self,
        id: str,
        name: str,
        description: str | None = None,
        flair: Flair | None = None,
        leader: LightUser | None = None,
        leaders: tuple[LightUser, ...] | None = None,
        nbMemebers: int | None = None,
        open: bool | None = None,
        joined: bool | None = None,
        requested: bool | None = None,
        **kwargs,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.flair = flair
        self.leader = leader
        self.leaders = leaders
        self.nbMemebers = nbMemebers
        self.open = open
        self.joined = joined
        self.requested = requested
