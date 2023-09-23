from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


@dataclass
class PipeEager(Generic[T]):
    x: T

    def then(self, f: Callable[[T], U]) -> PipeEager[U]:
        return PipeEager(f(self.x))

    def __call__(self) -> T:
        return self.x
