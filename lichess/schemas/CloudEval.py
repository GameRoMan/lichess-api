from pydantic import BaseModel


class CloudEval(BaseModel):
    """
    CloudEval

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/CloudEval.yaml
    """

    depth: int
    fen: str
    nodes: int
    pvs: tuple[object, ...]
