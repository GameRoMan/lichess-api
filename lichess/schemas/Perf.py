from ._internal import JsonDeserializable


class Perf(JsonDeserializable):
    """
    Performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Perf.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, games: int, rating: int, rd: int, prog: int, prov: bool | None = None, **kwargs):
        self.games = games
        self.rating = rating
        self.rd = rd
        self.prog = prog
        self.prov = prov
