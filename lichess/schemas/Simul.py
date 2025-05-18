from ._internal import JsonDeserializable


class Simul(JsonDeserializable):
    """
    Simultaneous

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Simul.yaml
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
        host: object,
        name: str,
        fullName: str,
        variants,
        isCreated: bool,
        isFinished: bool,
        isRunning: bool,
        nbApplicants: int,
        nbPairings: int,
        text: str | None = None,
        estimatedStartAt: int | None = None,
        startedAt: int | None = None,
        finishedAt: int | None = None,
        **kwargs,
    ):
        self.id = id
        self.host = host
        self.name = name
        self.fullName = fullName
        self.variants = variants
        self.isCreated = isCreated
        self.isFinished = isFinished
        self.isRunning = isRunning
        self.text = text
        self.estimatedStartAt = estimatedStartAt
        self.startedAt = startedAt
        self.finishedAt = finishedAt
        self.nbApplicants = nbApplicants
        self.nbPairings = nbPairings
