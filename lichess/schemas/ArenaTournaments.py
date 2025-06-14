from pydantic import BaseModel

from . import ArenaTournament


class ArenaTournaments(BaseModel):
    """
    ArenaTournaments

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournaments.yaml
    """

    created: tuple[ArenaTournament, ...]
    started: tuple[ArenaTournament, ...]
    finished: tuple[ArenaTournament, ...]
