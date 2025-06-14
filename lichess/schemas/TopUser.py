from ._internal import JsonDeserializable

from . import Title


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
        perfs: object | None = None,
        title: Title | None = None,
        patron: bool | None = None,
        online: bool | None = None,
        **kwargs,
    ):
        self.id = id
        self.username = username
        self.perfs = perfs
        self.title: Title | None = title
        self.patron = patron
        self.online = online
