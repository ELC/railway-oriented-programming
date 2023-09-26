from dataclasses import dataclass
from typing import Callable, Generic, ParamSpec, TypeVar

from pipe_lazy_with_start import PipeLazyWithStart

T = TypeVar("T")
P = ParamSpec("P")


@dataclass
class PipeLazy(Generic[P, T]):
    def then(self, f: Callable[P, T]) -> PipeLazyWithStart[P, T]:
        return PipeLazyWithStart(f)
