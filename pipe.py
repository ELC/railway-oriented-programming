from functools import reduce
from typing import Any, Callable

from compose import compose, identity


def pipe(*functions: Callable[..., Any]) -> Callable[..., Any]:
    return reduce(compose, functions, identity)
