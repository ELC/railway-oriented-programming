from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, ParamSpec, TypeVar

from compose import compose

T = TypeVar("T")
U = TypeVar("U")
P = ParamSpec("P")


@dataclass
class PipeLazyWithStart(Generic[P, T]):
    f: Callable[P, T]

    def then(self, g: Callable[[T], U]) -> PipeLazyWithStart[P, U]:
        return PipeLazyWithStart(compose(self.f, g))

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.f(*args, **kwargs)
