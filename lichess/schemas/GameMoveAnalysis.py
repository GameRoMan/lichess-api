from ._internal import JsonDeserializable


class GameMoveAnalysis(JsonDeserializable):
    """
    GameMoveAnalysis

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/GameMoveAnalysis.yaml
    """

    def __init__(self, **kwargs): ...
