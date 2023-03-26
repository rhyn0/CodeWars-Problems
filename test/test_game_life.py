# My Modules
from rank_up.game_of_life import get_generation


def test_gol_given():
    grid_in = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
    grid_out = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert get_generation(grid_in, 1) == grid_out


def test_gol_others():
    # fmt: off
    assert get_generation(
        [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ], 1) == [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ]
    assert get_generation(
        [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ], 2) == [
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0],
    ]
    # fmt: on


def test_gol_no_modify_original():
    cell_in = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
    assert get_generation(cell_in, 1) == [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ]
    assert cell_in == [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
