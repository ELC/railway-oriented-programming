from composable import Composable
from composable_functions import *
from compose import compose
from pipe import pipe
from pipe_eager import PipeEager
from pipe_iterative import pipe_iterative
from pipe_lazy import PipeLazy
from pipe_lazy_with_start import PipeLazyWithStart

test_compose = compose(
    compose(compose(compose(add_one, convert_to_string), sort_characters), len), str
)
assert test_compose(2) == "1"


test_pipe_iterative = pipe_iterative(
    add_one, convert_to_string, sort_characters, len, convert_to_string
)
assert test_pipe_iterative(2) == "1"


test_pipe = pipe(add_one, convert_to_string, sort_characters, len, str)
assert test_pipe(2) == "1"


test_pipe_class = (
    PipeEager(2)
    .then(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)

assert test_pipe_class() == "1"


test_pipe_with_start = (
    PipeLazyWithStart(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)

assert test_pipe_with_start(2) == "1"


test_pipe_lazy = (
    PipeLazy[[int], int]()
    .start(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)

assert test_pipe_lazy(2) == "1"


@Composable
def convert_to_string_decorated(x: int) -> str:
    return str(x)


test_pipe_lazy = (
    Composable(add_one)
    >> convert_to_string_decorated
    >> Composable(sort_characters)
    >> len
    >> str
)

assert test_pipe_lazy(2) == "1"
