from pydantic import BaseModel

from . import VariantKey


class Variant(BaseModel):
    """
    Variant

    See https://github.com/lichess-org/api/blob/master/doc/specs/schemas/Variant.yaml
    """

    key: VariantKey
    name: str
    short: str | None = None
