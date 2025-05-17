from ._internal import JsonDeserializable

from .LightUser import LightUser


class GameUser(JsonDeserializable):
    """
    GameUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameUser.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        if "user" in obj:
            obj["user"] = LightUser.de_json(obj.get("user"))
        return cls(**obj)

    def __init__(
        self,
        user: LightUser,
        rating: int,
        ratingDiff: int,
        name: str,
        provisional: bool,
        aiLevel: int,
        analysis: object,
        team: str,
        **kwargs,
    ):
        self.user = user
        self.rating = rating
        self.ratingDiff = ratingDiff
        self.name = name
        self.provisional = provisional
        self.aiLevel = aiLevel
        self.analysis = analysis
        self.team = team
