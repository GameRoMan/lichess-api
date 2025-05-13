"""
See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Speed.yaml
"""

from typing import Literal


Speed = Literal[
    'ultraBullet',
    'bullet',
    'blitz',
    'rapid',
    'classical',
    'correspondence'
]
