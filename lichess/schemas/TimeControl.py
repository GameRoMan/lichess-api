from typing import Literal

from ._internal import JsonDeserializable


class TimeControl(JsonDeserializable):
    """
    TimeControl

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/TimeControl.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self,
        type: Literal["clock", "correspondence", "unlimited"],
        limit: int | None = None,
        increment: int | None = None,
        show: str | None = None,
        daysPerTurn: int | None = None,
        **kwargs,
    ):
        self.type: Literal["clock", "correspondence", "unlimited"] = type
        match self.type:
            case "clock":
                if limit is None or increment is None or show is None:
                    raise ValueError("clock time control must have limit, increment and show")
                self.limit = limit
                self.increment = increment
                self.show = show
            case "correspondence":
                if daysPerTurn is None:
                    raise ValueError("correspondence time control must have daysPerTurn")
                self.daysPerTurn = daysPerTurn
            case "unlimited":
                pass
