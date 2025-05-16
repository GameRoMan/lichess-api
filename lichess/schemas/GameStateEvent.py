from typing import Literal

from ._internal import JsonDeserializable

from .GameStatus import GameStatus


class GameStateEvent(JsonDeserializable):
    """
    GameState event

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStateEvent.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self,
        type: Literal["gameState"],
        moves: str,
        wtime: int,
        btime: int,
        winc: int,
        binc: int,
        status: GameStatus,
        winner: str | None = None,
        wdraw: bool | None = None,
        bdraw: bool | None = None,
        wtakeback: bool | None = None,
        btakeback: bool | None = None,
        **kwargs,
    ):
        self.type: Literal["gameState"] = type
        self.moves = moves
        self.wtime = wtime
        self.btime = btime
        self.winc = winc
        self.binc = binc
        self.status: GameStatus = status
        self.winner = winner
        self.wdraw = wdraw
        self.bdraw = bdraw
        self.wtakeback = wtakeback
        self.btakeback = btakeback
