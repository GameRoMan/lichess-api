from pydantic import BaseModel

from . import ArenaTournament, ArenaTournamentPlayer


class ArenaTournamentPlayed(BaseModel):
    """
    ArenaTournamentPlayed

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ArenaTournamentPlayed.yaml
    """

    tournament: ArenaTournament
    player: ArenaTournamentPlayer
