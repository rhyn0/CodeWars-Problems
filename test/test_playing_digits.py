# External Party
from hypothesis import given
from hypothesis import strategies as st
import pytest

# My Modules
from fundamentals.playing_digits import dig_pow


def test_pow_basics():
    assert dig_pow(89, 1) == 1
    assert dig_pow(92, 1) == -1
    assert dig_pow(46288, 3) == 51
    assert dig_pow(695, 2) == 2


@given(st.floats(min_value=0.1), st.floats(min_value=0.1))
def test_pow_in_floats(num: float, power: float):
    with pytest.raises(TypeError):
        dig_pow(num, 2)  # type: ignore

    with pytest.raises(TypeError):
        dig_pow(2, power)  # type: ignore


@given(st.integers(max_value=-1), st.integers(max_value=-1))
def test_pow_in_negatives(num: int, power: int):
    with pytest.raises(ValueError, match="Arguments must be positive integers."):
        dig_pow(num, 2)

    with pytest.raises(ValueError, match="Arguments must be positive integers."):
        dig_pow(2, power)
