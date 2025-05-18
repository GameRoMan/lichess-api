from typing import TypeVar

T = TypeVar("T")


def noop(arg: T) -> T:
    return arg
