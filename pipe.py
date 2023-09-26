from functools import reduce
from typing import Callable, TypeVar

from compose import compose

T = TypeVar("T")


# def pipe(*functions: Callable[[T], T]) -> Callable[[T], T]:
#     return reduce(compose, functions)


def pipe(*functions: Callable[..., Any]) -> Callable[..., Any]:
    return reduce(compose, functions, identity)
