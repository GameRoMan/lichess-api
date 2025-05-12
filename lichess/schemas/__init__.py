"""
See https://github.com/lichess-org/api/tree/master/doc/specs/schemas
"""


from ._internal import JsonSerializable, Dictionaryable, JsonDeserializable










class UserPreferences(JsonDeserializable):
    ...




class LightUser(JsonDeserializable):
    ...







class TvGame(JsonDeserializable):
    ...





class PuzzlePerformance(JsonDeserializable):
    ...



class Verdicts(JsonDeserializable):
    ...





class GameEventInfo(JsonDeserializable):
    ...




class ChallengeCanceledJson(JsonDeserializable):
    ...




class GameStartEvent(JsonDeserializable):
    ...


class GameFinishEvent(JsonDeserializable):
    ...


class ChallengeEvent(JsonDeserializable):
    ...



class ChallengeCanceledEvent(JsonDeserializable):
    ...


class ChallengeDeclinedEvent(JsonDeserializable):
    ...



class Simul(JsonDeserializable):
    ...




class GameEventPlayer(JsonDeserializable):
    ...


class ChallengeUser(JsonDeserializable):
    ...


class ArenaRatingObj(JsonDeserializable):
    ...



class BroadcastTour(JsonDeserializable):
    ...

class BroadcastGroup(JsonDeserializable):
    ...


class BroadcastRoundInfo(JsonDeserializable):
    ...




class ExternalEngineWork(JsonDeserializable):
    ...

class ExternalEngine(JsonDeserializable):
    ...


