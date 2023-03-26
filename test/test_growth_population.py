# External Party
from hypothesis import given
from hypothesis import strategies as st
import pytest

# My Modules
from fundamentals.growth_population import nb_year


def test_nb_basics():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
    assert nb_year(1000, 4, 10, 500) == 0


@given(st.floats())
def test_nb_input_p0(start_pop: float):
    with pytest.raises(TypeError):
        nb_year(start_pop, 5, 100, 5000)  # type: ignore


@given(st.complex_numbers())
def test_nb_input_percent(percent: complex):
    with pytest.raises(TypeError):
        nb_year(5, percent, 100, 5000)  # type: ignore


@given(st.floats())
def test_nb_input_aug(augment_pop: float):
    with pytest.raises(TypeError):
        nb_year(5, 5, augment_pop, 5000)  # type: ignore


@given(st.floats())
def test_nb_input_final(final_pop: float):
    with pytest.raises(TypeError):
        nb_year(5, 5, 100, final_pop)  # type: ignore


@given(st.integers(max_value=-2), st.integers(max_value=-1))
def test_nb_input_negatives(start_pop: int, goal_pop: int):
    with pytest.raises(ValueError, match="Populations must be greater 0."):
        nb_year(start_pop, 5, 100, 1000)

    with pytest.raises(ValueError, match="Populations must be greater 0."):
        nb_year(1, 5, 100, goal_pop)
