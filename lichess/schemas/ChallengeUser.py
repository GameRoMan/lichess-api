from ._internal import JsonDeserializable

from .Flair import Flair
from .Title import Title


class ChallengeUser(JsonDeserializable):
    """
    Challenge user

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeUser.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, rating: float, provisional: bool, online: bool, lag: float,
        id: str, name: str, flair: Flair, title: Title, patron: bool
    ):
        self.rating = rating
        self.provisional = provisional
        self.online = online
        self.lag = lag
        self.id = id
        self.name = name
        self.flair = flair
        self.title = title
        self.patron = patron
