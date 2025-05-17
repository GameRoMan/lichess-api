from ._internal import JsonDeserializable

from .ArenaTournament import ArenaTournament


class ArenaTournaments(JsonDeserializable):
    """
    ArenaTournaments

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournaments.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        return cls(**obj)

    def __init__(
        self,
        created: tuple[ArenaTournament],
        started: tuple[ArenaTournament],
        finished: tuple[ArenaTournament],
        **kwargs,
    ):
        self.created = created
        self.started = started
        self.fiinished = finished
