from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypeVar, Callable, Generic, ParamSpec


from functools import reduce

T = TypeVar("T")
U = TypeVar("U")
W = TypeVar("W")
P = ParamSpec("P")

def compose(f: Callable[P, U], g: Callable[[U], W]) -> Callable[P, W]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> W:
        return g(f(*args, **kwargs))
    return inner

def identity(x: T) -> T:
    return x


def add_one(x: int) -> int:
    return x + 1

def convert_to_string(x: int) -> str:
    return str(x)

def count_letters(x: str) -> int:
    return len(x)


test_ = compose(compose(add_one, convert_to_string), count_letters)
assert test_(2) == 1


def pipe_iterative(*functions):
    composed_function = identity
    for function in functions:
        composed_function = compose(composed_function, function)
    return composed_function

test_ = pipe_iterative(add_one, convert_to_string, count_letters)
assert test_(2) == 1


def pipe(*functions):
    return reduce(
        compose,
        functions,
        identity
    )

test_ = pipe(add_one, convert_to_string, count_letters)
assert test_(2) == 1


@dataclass
class Pipe(Generic[T]):
    x: T

    def then(self, f: Callable[[T], W]) -> Pipe[W]:
        return Pipe(f(self.x))
    
    def __call__(self) -> T:
        return self.x


test_pipe = (
    Pipe(2)
    .then(add_one)
    .then(convert_to_string)
    .then(count_letters)
)

assert test_pipe() == 1



@dataclass
class PipeLazyWithStart(Generic[P, W]):
    f: Callable[P, W]

    def then(self, g: Callable[[W], U]) -> PipeLazyWithStart[P, U]:
        return PipeLazyWithStart(compose(self.f, g))

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> W:
        return self.f(*args, **kwargs)


test_pipe = (
    PipeLazyWithStart(add_one)
    .then(convert_to_string)
    .then(count_letters)
)

assert test_pipe(2) == 1



@dataclass
class PipeLazy(Generic[P, W]):
    f: Optional[Callable[P, W]] = None

    def start(self, f: Callable[P, W]) -> PipeLazy[P, W]:
        return PipeLazy(f)

    def then(self, g: Callable[[W], U]) -> PipeLazy[P, U]:
        if not self.f:
            raise ValueError()
        return PipeLazy(compose(self.f, g))

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> W:
        if not self.f:
            raise ValueError()
        return self.f(*args, **kwargs)


test_pipe = (
    PipeLazy[[int], int]()
    .start(add_one)
    .then(convert_to_string)
    .then(count_letters)
)

assert test_pipe(2) == 1
