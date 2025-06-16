from pydantic import BaseModel

from .BroadcastCustomPoints import BroadcastCustomPoints


class BroadcastCustomScoring(BaseModel):
    """
    BroadcastCustomScoring

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/BroadcastCustomScoring.yaml
    """

    white: BroadcastCustomPoints
    black: BroadcastCustomPoints
