# Standard Library
from typing import List

# External Party
from hypothesis import given
from hypothesis import strategies as st
import pytest

# My Modules
from fundamentals.tribonacci_sequence import tribonacci


def test_trib_basics():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]


@given(st.lists(st.one_of(st.integers(), st.floats()), min_size=3, max_size=3))
def test_trib_n_one(start_seq: List[int | float]):
    assert tribonacci(start_seq, 1) == start_seq[:1]


@given(st.lists(st.one_of(st.integers(), st.floats()), min_size=3, max_size=3))
def test_trib_n_zero(start_seq: List[int | float]):
    assert tribonacci(start_seq, 0) == []


@given(
    st.lists(st.one_of(st.integers(), st.floats()), min_size=0, max_size=2),
    st.integers(min_value=0),
)
def test_trib_short_start(start_seq: List[int | float], out_len: int):
    with pytest.raises(
        ValueError, match=r"Argument 'signature' must be of length 3, \d is not valid."
    ):
        tribonacci(start_seq, out_len)


def test_trib_floats():
    assert tribonacci([0.5, 0.5, 0.5], 30) == [
        0.5,
        0.5,
        0.5,
        1.5,
        2.5,
        4.5,
        8.5,
        15.5,
        28.5,
        52.5,
        96.5,
        177.5,
        326.5,
        600.5,
        1104.5,
        2031.5,
        3736.5,
        6872.5,
        12640.5,
        23249.5,
        42762.5,
        78652.5,
        144664.5,
        266079.5,
        489396.5,
        900140.5,
        1655616.5,
        3045153.5,
        5600910.5,
        10301680.5,
    ]
