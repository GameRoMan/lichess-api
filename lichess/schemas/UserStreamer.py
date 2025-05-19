from ._internal import JsonDeserializable


class UserStreamer(JsonDeserializable):
    """
    UserStreamer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/UserStreamer.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, twitch: object, youtube: object, **kwargs):
        self.twitch = twitch
        self.youtube = youtube
