from ._internal import JsonDeserializable

from .LightUser import LightUser
from .GameColor import GameColor


class TvGame(JsonDeserializable):
    """
    TvGame

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TvGame.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "user" in obj:
            obj["user"] = LightUser.de_json(obj.get("user"))
        return cls(**obj)

    def __init__(self, user: LightUser, rating: int, gameId: str, color: GameColor, **kwargs):
        self.user = user
        self.rating = rating
        self.gameId = gameId
        self.color: GameColor = color
