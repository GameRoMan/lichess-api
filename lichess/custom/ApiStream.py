from pydantic import BaseModel

from ..schemas import (
    GameStartEvent,
    GameFinishEvent,
    ChallengeEvent,
    ChallengeCanceledEvent,
    ChallengeDeclinedEvent,
)


ApiStreamEvent = (
    GameStartEvent
    | GameFinishEvent
    | ChallengeEvent
    | ChallengeCanceledEvent
    | ChallengeDeclinedEvent
)


class ApiStream(BaseModel):
    event: ApiStreamEvent
