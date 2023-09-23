from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Optional, ParamSpec, TypeVar

from compose import compose

T = TypeVar("T")
U = TypeVar("U")
P = ParamSpec("P")


@dataclass
class PipeLazy(Generic[P, T]):
    f: Optional[Callable[P, T]] = None

    def start(self, f: Callable[P, T]) -> PipeLazy[P, T]:
        return PipeLazy(f)

    def then(self, g: Callable[[T], U]) -> PipeLazy[P, U]:
        if not self.f:
            raise ValueError()
        return PipeLazy(compose(self.f, g))

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        if not self.f:
            raise ValueError()
        return self.f(*args, **kwargs)
