from typing import Literal

from ._internal import JsonDeserializable

from .ChallengeStatus import ChallengeStatus
from .Variant import Variant
from .Speed import Speed
from .TimeControl import TimeControl


class ChallengeOpenJson(JsonDeserializable):
    """
    ChallengeOpenJson

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/ChallengeOpenJson.yaml
    """

    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string)
        if "variant" in obj:
            obj["variant"] = Variant.de_json(obj.get("variant"))
        if "timeControl" in obj:
            obj["timeControl"] = TimeControl.de_json(obj.get("timeControl"))
        return cls(**obj)

    def __init__(
        self,
        id: str,
        url: str,
        status: ChallengeStatus,
        challenger: None,
        destUser: None,
        variant: Variant,
        rated: bool,
        speed: Speed,
        timeControl: TimeControl,
        color: Literal["white", "black", "random"],
        finalColor: Literal["white", "black"],
        perf: object,
        urlWhite: str,
        urlBlack: str,
        open: object,
        initialFen: str | None = None,
        **kwargs,
    ):
        self.id = id
        self.url = url
        self.status: ChallengeStatus = status
        self.challenger = challenger
        self.destUser = destUser
        self.variant = variant
        self.rated = rated
        self.speed = speed
        self.timeControl = timeControl
        self.color: Literal["white", "black", "random"] = color
        self.finalColor: Literal["white", "black"] = finalColor
        self.perf = perf
        self.initialFen = initialFen
        self.urlWhite = urlWhite
        self.urlBlack = urlBlack
        self.open = open


"""
type: object
properties:
  id:
    type: string
  url:
    type: string
    format: uri
  status:
    $ref: "./ChallengeStatus.yaml"
  challenger:
    type: "null"
  destUser:
    type: "null"
  variant:
    $ref: "./Variant.yaml"
  rated:
    type: boolean
  speed:
    $ref: "./Speed.yaml"
  timeControl:
    $ref: "./TimeControl.yaml"
  color:
    type: string
    enum: ["white", "black", "random"]
  finalColor:
    type: string
    enum: ["white", "black"]
  perf:
    type: object
    properties:
      icon:
        type: string
      name:
        type: string
  initialFen:
    type: string
  urlWhite:
    type: string
  urlBlack:
    type: string
  open:
    type: object
    properties:
      userIds:
        description: "An optional array of two user ids. If set, only these users will be allowed to join the game. The first username gets the white pieces."
        type: array
        items:
          type: string

required:
  - id
  - url
  - status
  - challenger
  - destUser
  - variant
  - rated
  - speed
  - timeControl
  - color
  - perf
  - urlWhite
  - urlBlack
  - open
  """
