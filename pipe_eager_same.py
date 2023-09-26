from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


@dataclass
class PipeEagerSameType(Generic[T]):
    x: T

    def then(self, f: Callable[[T], T]) -> PipeEagerSameType[T]:
        self.x = f(self.x)
        return self

    def __call__(self) -> T:
        return self.x
