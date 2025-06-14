from pydantic import BaseModel


class ArenaPerf(BaseModel):
    """
    Arena performance

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaPerf.yaml
    """

    key: str
    name: str
    position: int
    icon: str | None = None
