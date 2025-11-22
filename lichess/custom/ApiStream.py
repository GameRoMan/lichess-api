from pydantic import BaseModel

from ..schemas import (
    GameStartEvent,
    GameFinishEvent,
    ChallengeEvent,
    ChallengeCanceledEvent,
    ChallengeDeclinedEvent,
)


type ApiStreamEvent = (
    GameStartEvent
    | GameFinishEvent
    | ChallengeEvent
    | ChallengeCanceledEvent
    | ChallengeDeclinedEvent
)


class ApiStream(BaseModel):
    event: ApiStreamEvent
