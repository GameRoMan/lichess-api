from ._internal import JsonDeserializable

from . import Perfs, Title, Flair, Profile, PlayTime


class User(JsonDeserializable):
    """
    User

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/User.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "perfs" in obj:
            obj["perfs"] = Perfs.de_json(obj.get("perfs"))
        if "profile" in obj:
            obj["profile"] = Profile.de_json(obj.get("profile"))
        if "playTime" in obj:
            obj["playTime"] = PlayTime.de_json(obj.get("playTime"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        username: str,
        perfs: Perfs | None = None,
        title: Title | None = None,
        flair: Flair | None = None,
        createdAt: int | None = None,
        disabled: bool | None = None,
        tosViolation: bool | None = None,
        profile: Profile | None = None,
        seenAt: int | None = None,
        playTime: PlayTime | None = None,
        patron: bool | None = None,
        verified: bool | None = None,
        **kwargs,
    ):
        self.id = id
        self.username = username
        self.perfs = perfs
        self.title: Title | None = title
        self.flair = flair
        self.createdAt = createdAt
        self.disabled = disabled
        self.tosViolation = tosViolation
        self.profile = profile
        self.seenAt = seenAt
        self.playTime = playTime
        self.patron = patron
        self.verified = verified
