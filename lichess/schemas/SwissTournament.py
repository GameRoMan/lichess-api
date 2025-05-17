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
        nextRound: object,
        **kwargs,
    ): ...
