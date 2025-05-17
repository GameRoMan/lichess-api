from ._internal import JsonDeserializable


class GameJson(JsonDeserializable):
    """
    GameJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameJson.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        return cls(**obj)

    def __init__(
        self,
        id,
        rated,
        variant,
        speed,
        perf,
        createdAt,
        lastMoveAt,
        status,
        source,
        players,
        initialFen,
        winner,
        opening,
        mobes,
        pgn,
        daysPerTurn,
        analysis,
        tournament,
        swiss,
        clock,
        clocks,
        division,
        **kwargs,
    ): ...
