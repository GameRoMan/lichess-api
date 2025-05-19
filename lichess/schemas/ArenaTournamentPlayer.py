from ._internal import JsonDeserializable


class ArenaTournamentPlayer(JsonDeserializable):
    """
    ArenaTournamentPlayer

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentPlayer.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        return cls(**obj)

    def __init__(self, *, games: int, score: int, rank: int, performance: int | None = None, **kwargs):
        self.games = games
        self.score = score
        self.rank = rank
        self.performance = performance
