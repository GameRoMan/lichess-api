"""
https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameStatus.yaml
Game status code. https://github.com/lichess-org/scalachess/blob/0a7d6f2c63b1ca06cd3c958ed3264e738af5c5f6/src/main/scala/Status.scala#L16-L28
"""

from typing import Literal

GameStatus = Literal[
    'created',
    'started',
    'aborted',
    'mate',
    'resign',
    'stalemate',
    'timeout',
    'draw',
    'outoftime',
    'cheat',
    'noStart',
    'unknownFinish',
    'variantEnd'
]
