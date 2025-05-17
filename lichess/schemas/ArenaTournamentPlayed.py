from ._internal import JsonDeserializable

from .ArenaTournament import ArenaTournament


class ArenaTournamentPlayed(JsonDeserializable):
    """
    ArenaTournamentPlayed

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentPlayed.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "tournament" in obj:
            obj["tournament"] = ArenaTournament.de_json(obj.get("tournament"))
        return cls(**obj)

    def __init__(self, tournament: ArenaTournament, player: object, **kwargs):
        self.tournament = tournament
        self.player = player
