from ._internal import JsonDeserializable

from .ArenaTournament import ArenaTournament
from .ArenaTournamentPlayer import ArenaTournamentPlayer


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
        if "player" in obj:
            obj["player"] = ArenaTournamentPlayer.de_json(obj.get("player"))
        return cls(**obj)

    def __init__(self, *, tournament: ArenaTournament, player: ArenaTournamentPlayer, **kwargs):
        self.tournament = tournament
        self.player = player
