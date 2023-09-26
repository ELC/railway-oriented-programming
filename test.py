from composable import Composable
from composable_functions import *
from compose import compose
from pipe import pipe
from pipe_eager import PipeEager
from pipe_eager_same import PipeEagerSameType
from pipe_iterative import pipe_iterative
from pipe_lazy import PipeLazy
from pipe_lazy_with_start import PipeLazyWithStart

user_defined_composition = compose(
    compose(compose(compose(add_one, convert_to_string), sort_characters), len), str
)
assert user_defined_composition(2) == "1"


user_defined_composition = pipe_iterative(
    add_one, convert_to_string, sort_characters, len, str
)
assert user_defined_composition(2) == "1"

user_defined_composition = pipe(add_one, convert_to_string, sort_characters, len, str)
assert user_defined_composition(2) == "1"

user_defined_composition = (
    PipeEagerSameType(2)
    .then(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)
assert user_defined_composition() == "1"

user_defined_composition = (
    PipeEager(2)
    .then(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)
assert user_defined_composition() == "1"


user_defined_composition = (
    PipeLazyWithStart(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)
assert user_defined_composition(2) == "1"


user_defined_composition = (
    PipeLazy[[int], int]()
    .then(add_one)
    .then(convert_to_string)
    .then(sort_characters)
    .then(len)
    .then(str)
)
assert user_defined_composition(2) == "1"


@Composable
def convert_to_string_decorated(x: int) -> str:
    return str(x)


user_defined_composition = (
    Composable(add_one)
    >> convert_to_string_decorated
    >> Composable(sort_characters)
    >> len
    >> str
)
assert user_defined_composition(2) == "1"
