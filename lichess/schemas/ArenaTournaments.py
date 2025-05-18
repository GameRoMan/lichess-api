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
        if "created" in obj:
            obj["created"] = tuple(
                arena_tournament
                for at in obj.get("created", [])
                if (arena_tournament := ArenaTournament.de_json(at))
            )
        if "started" in obj:
            obj["started"] = tuple(
                arena_tournament
                for at in obj.get("started", [])
                if (arena_tournament := ArenaTournament.de_json(at))
            )
        if "finished" in obj:
            obj["finished"] = tuple(
                arena_tournament
                for at in obj.get("finished", [])
                if (arena_tournament := ArenaTournament.de_json(at))
            )
        return cls(**obj)

    def __init__(
        self,
        created: tuple[ArenaTournament, ...],
        started: tuple[ArenaTournament, ...],
        finished: tuple[ArenaTournament, ...],
        **kwargs,
    ):
        self.created = created
        self.started = started
        self.fiinished = finished
