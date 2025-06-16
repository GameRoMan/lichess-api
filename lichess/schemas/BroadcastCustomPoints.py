from pydantic import BaseModel, Field


class BroadcastCustomPoints(BaseModel):
    """
    BroadcastCustomPoints

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastCustomPoints.yaml
    """

    win: float = Field(ge=0, le=10)
    draw: float = Field(ge=0, le=10)
