# Standard Library
import itertools
from typing import Iterable

# External Party
from hypothesis import given
from hypothesis import strategies as st

# My Modules
from fundamentals.unique_order import unique_in_order


def test_unique_order_basic():
    assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
    assert unique_in_order([]) == []
    assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]


@given(st.text(min_size=1))
def test_unique_order_more(i: Iterable):
    assert unique_in_order(i) == [k for k, _ in itertools.groupby(i)]
