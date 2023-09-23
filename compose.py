from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T")
U = TypeVar("U")
P = ParamSpec("P")


def identity(x: T) -> T:
    return x


def compose(f: Callable[P, T], g: Callable[[T], U]) -> Callable[P, U]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> U:
        return g(f(*args, **kwargs))

    return inner
