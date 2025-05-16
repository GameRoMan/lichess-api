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
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self,
        id: str,
        name: str,
        rating: float | None = None,
        title: Title | None = None,
        flair: Flair | None = None,
        patron: bool | None = None,
        provisional: bool | None = None,
        online: bool | None = None,
        lag: int | None = None,
        **kwargs,
    ):
        self.id = id
        self.name = name
        self.rating = rating
        self.title: Title | None = title
        self.flair = flair
        self.patron = patron
        self.provisional = provisional
        self.online = online
        self.lag = lag
