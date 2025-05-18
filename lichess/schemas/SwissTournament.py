from ._internal import JsonDeserializable

from .SwissStatus import SwissStatus
from .Verdicts import Verdicts


class SwissTournament(JsonDeserializable):
    """
    SwissTournament

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/SwissTournament.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "verdicts" in obj:
            obj["verdicts"] = Verdicts.de_json(obj.get("verdicts"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        createdBy: str,
        startsAt: str,
        name: str,
        clock: object,
        variant: str,
        round: int,
        nbRounds: int,
        nbPlayers: int,
        nbOngoing: int,
        status: SwissStatus,
        stats: object,
        rated: bool,
        verdicts: Verdicts,
        nextRound: object | None = None,
        **kwargs,
    ):
        self.id = id
        self.createdBy = createdBy
        self.startsAt = startsAt
        self.name = name
        self.clock = clock
        self.variant = variant
        self.round = round
        self.nbRounds = nbRounds
        self.nbPlayers = nbPlayers
        self.nbOngoing = nbOngoing
        self.status: SwissStatus = status
        self.stats = stats
        self.rated = rated
        self.verdicts = verdicts
        self.nextRound = nextRound
