from pydantic import BaseModel

from ..schemas import GameFullEvent, GameStateEvent, ChatLineEvent, OpponentGoneEvent


BotGameStreamEvent = GameFullEvent | GameStateEvent | ChatLineEvent | OpponentGoneEvent


class BotGameStream(BaseModel):
    event: BotGameStreamEvent
