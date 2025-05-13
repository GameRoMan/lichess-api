from ._internal import JsonDeserializable


class Count(JsonDeserializable):
    """
    Count

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Count.yaml
    """
    @classmethod
    def de_json(cls, json_string):
        if json_string is None: return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(
        self, all: int, rated: int, ai: int, draw: int, drawH: int,
        loss: int, lossH: int, win: int, winH: int, bookmark: int,
        playing: int, _import: int, me: int
    ):
        self.all = all
        self.rated = rated
        self.ai = ai
        self.draw = draw
        self.drawH = drawH
        self.loss = loss
        self.lossH = lossH
        self.win = win
        self.winH = winH
        self.bookmark = bookmark
        self.playing = playing
        self._import = _import
        self.me = me
