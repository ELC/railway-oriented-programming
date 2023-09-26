from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, ParamSpec, TypeVar

from compose import compose

T = TypeVar("T")
U = TypeVar("U")
P = ParamSpec("P")
Q = ParamSpec("Q")


@dataclass
class Composable(Generic[P, T]):
    f: Callable[P, T]

    def __rshift__(self, other: Callable[Q, U]) -> Composable[P, U]:
        if not isinstance(other, Composable):
            other = Composable(other)
        return Composable(compose(self.f, other.f))

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.f(*args, **kwargs)
