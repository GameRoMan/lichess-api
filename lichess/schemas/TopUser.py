from ._internal import JsonDeserializable

from .Title import Title


class TopUser(JsonDeserializable):
    """
    TopUser

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TopUser.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        return cls(**obj)

    def __init__(
        self,
        id: str,
        username: str,
        perfs,
        title: Title,
        patron: bool | None = None,
        online: bool | None = None,
        **kwargs,
    ):
        self.id = id
        self.username = username
        self.perfs = perfs
        self.title = title
        self.patron = patron
        self.online = online
