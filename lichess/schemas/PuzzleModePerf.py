from ._internal import JsonDeserializable

class PuzzleModePerf(JsonDeserializable):
    """
    Puzzle mode performance
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, runs: int, score: int):
        self.runs = runs
        self.score = score
