from ._internal import JsonDeserializable

from .Perf import Perf
from .PuzzleModePerf import PuzzleModePerf


class Perfs(JsonDeserializable):
    """
    Performances

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Perfs.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        if "chess960" in obj:
            obj["chess960"] = Perf.de_json(obj.get("chess960"))
        if "atomic" in obj:
            obj["atomic"] = Perf.de_json(obj.get("atomic"))
        if "racingKings" in obj:
            obj["racingKings"] = Perf.de_json(obj.get("racingKings"))
        if "ultraBullet" in obj:
            obj["ultraBullet"] = Perf.de_json(obj.get("ultraBullet"))
        if "blitz" in obj:
            obj["blitz"] = Perf.de_json(obj.get("blitz"))
        if "kingOfTheHill" in obj:
            obj["kingOfTheHill"] = Perf.de_json(obj.get("kingOfTheHill"))
        if "threeCheck" in obj:
            obj["threeCheck"] = Perf.de_json(obj.get("threeCheck"))
        if "antichess" in obj:
            obj["antichess"] = Perf.de_json(obj.get("antichess"))
        if "crazyhouse" in obj:
            obj["crazyhouse"] = Perf.de_json(obj.get("crazyhouse"))
        if "bullet" in obj:
            obj["bullet"] = Perf.de_json(obj.get("bullet"))
        if "correspondence" in obj:
            obj["correspondence"] = Perf.de_json(obj.get("correspondence"))
        if "horde" in obj:
            obj["horde"] = Perf.de_json(obj.get("horde"))
        if "puzzle" in obj:
            obj["puzzle"] = Perf.de_json(obj.get("puzzle"))
        if "classical" in obj:
            obj["classical"] = Perf.de_json(obj.get("classical"))
        if "rapid" in obj:
            obj["rapid"] = Perf.de_json(obj.get("rapid"))
        if "storm" in obj:
            obj["storm"] = PuzzleModePerf.de_json(obj.get("storm"))
        if "racer" in obj:
            obj["racer"] = PuzzleModePerf.de_json(obj.get("racer"))
        if "streak" in obj:
            obj["streak"] = PuzzleModePerf.de_json(obj.get("streak"))
        return cls(**obj)

    def __init__(
        self,
        chess960: Perf,
        atomic: Perf,
        racingKings: Perf,
        ultraBullet: Perf,
        blitz: Perf,
        kingOfTheHill: Perf,
        threeCheck: Perf,
        antichess: Perf,
        crazyhouse: Perf,
        bullet: Perf,
        correspondence: Perf,
        horde: Perf,
        puzzle: Perf,
        classical: Perf,
        rapid: Perf,
        storm: PuzzleModePerf,
        racer: PuzzleModePerf,
        streak: PuzzleModePerf,
        **kwargs,
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
