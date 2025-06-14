from pydantic import BaseModel

from . import GameStatusId, GameStatusName


class GameStatus(BaseModel):
    """
    GameStatus

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatus.yaml
    """

    id: GameStatusId
    name: GameStatusName
