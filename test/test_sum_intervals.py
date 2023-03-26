# External Party
from hypothesis import given
from hypothesis import note
from hypothesis import strategies as st

# My Modules
from rank_up.sum_intervals import sum_of_intervals
from rank_up.sum_intervals import top_bottom_pointers


def test_sum_interval_basic():
    assert sum_of_intervals([(1, 5)]) == 4
    assert sum_of_intervals([(1, 5), (6, 10)]) == 8
    assert sum_of_intervals([(1, 5), (1, 5)]) == 4
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7


@st.composite
def valid_intervals(draw):
    start = draw(st.integers())
    end = draw(st.integers(min_value=start + 1))
    return start, end


@given(st.lists(valid_intervals(), min_size=1))
def test_sum_interval_gen(vals):
    # pretty hard one to make automated tests
    note(vals)
    assert sum_of_intervals(vals) == top_bottom_pointers(vals)


def test_sum_interval_empty():
    assert sum_of_intervals([]) == 0
