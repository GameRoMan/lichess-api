from ._internal import JsonDeserializable


class Profile(JsonDeserializable):
    """
    Profile

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Profile.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, flag: str, location: str, bio: str, realName: str,
        fideRating: int | None = None, uscfRating: int | None = None,
        ecfRating: int | None = None, cfcRating: int | None = None,
        rcfRating: int | None = None, dsbRating: int | None = None,
        links: str = ''
    ):
        self.flag = flag
        self.location = location
        self.bio = bio
        self.realName = realName
        self.fideRating = fideRating
        self.uscfRating = uscfRating
        self.ecfRating = ecfRating
        self.cfcRating = cfcRating
        self.rcfRating = rcfRating
        self.dsbRating = dsbRating
        self.links = links
