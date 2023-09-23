from typing import Any, Callable, TypeVar

from compose import compose, identity

T = TypeVar("T")


def pipe_iterative(*functions: Callable[..., Any]) -> Callable[..., Any]:
    composed_function = identity
    for function in functions:
        composed_function = compose(composed_function, function)
    return composed_function
