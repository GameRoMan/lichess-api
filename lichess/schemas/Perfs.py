from ._internal import JsonDeserializable

from .Perf import Perf
from .PuzzleModePerf import PuzzleModePerf


class Perfs(JsonDeserializable):
    """
    Performances
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, chess960: Perf, atomic: Perf, racingKings: Perf, ultraBullet: Perf,
        blitz: Perf, kingOfTheHill: Perf, threeCheck: Perf, antichess: Perf,
        crazyhouse: Perf, bullet: Perf, correspondence: Perf, horde: Perf,
        puzzle: Perf, classical: Perf, rapid: Perf,
        storm: PuzzleModePerf, racer: PuzzleModePerf, streak: PuzzleModePerf
    ):
        self.chess960 = chess960
        self.atomic = atomic
        self.racingKings = racingKings
        self.ultraBullet = ultraBullet
        self.blitz = blitz
        self.kingOfTheHill = kingOfTheHill
        self.threeCheck = threeCheck
        self.antichess = antichess
        self.crazyhouse = crazyhouse
        self.bullet = bullet
        self.correspondence = correspondence
        self.horde = horde
        self.puzzle = puzzle
        self.classical = classical
        self.rapid = rapid
        self.storm = storm
        self.racer = racer
        self.streak = streak
