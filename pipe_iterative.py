from typing import Any, Callable, TypeVar

from compose import compose

T = TypeVar("T")


# def pipe_iterative(*functions: Callable[[T], T]) -> Callable[[T], T]:
#     composed_function, *rest = functions
#     for function in rest:
#         composed_function = compose(composed_function, function)
#     return composed_function


def pipe_iterative(*functions: Callable[..., Any]) -> Callable[..., Any]:
    composed_function, *rest = functions
    for function in rest:
        composed_function = compose(composed_function, function)
    return composed_function
