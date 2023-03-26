# External Party
from hypothesis import given
from hypothesis import strategies as st
import pytest

# My Modules
from rank_up.square_squares import decompose
from rank_up.square_squares import decompose_ref


def test_decompose_basic():
    assert decompose(5) == [3, 4]
    assert decompose(8) is None
    assert decompose(0) is None


def test_decompose_compare():
    assert decompose(5) == decompose_ref(5)
    assert decompose(8) == decompose_ref(8)


@pytest.mark.xfail()
def test_decompose_comp_falsifying():
    # this is expected since zero is technically not a positive integer
    assert decompose(0) == decompose_ref(0)


@given(st.integers(min_value=1, max_value=100_000))
def test_decompose(num: int):
    assert decompose(num) == decompose_ref(num)
