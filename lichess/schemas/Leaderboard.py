from ._internal import JsonDeserializable

from .TopUser import TopUser


class Leaderboard(JsonDeserializable):
    """
    Leaderboard

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Leaderboard.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        if "users" in obj:
            obj["users"] = tuple(
                top_user for users in obj.get("users", []) if (top_user := TopUser.de_json(users))
            )
        return cls(**obj)

    def __init__(self, *, users: tuple[TopUser, ...], **kwargs):
        self.users = users
