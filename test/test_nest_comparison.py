# My Modules
from rank_up.nesting_comparison import same_structure_as


def test_structure_basic():
    assert same_structure_as([1, 1, 1], [2, 2, 2])
    assert same_structure_as([1, [1, 1]], [2, [2, 2]])
    assert same_structure_as([[[], []]], [[[], []]])

    assert not same_structure_as([1, [1, 1]], [[2, 2], 2])
    assert not same_structure_as([1, [1, 1]], [[2], 2])
    assert not same_structure_as([[[], []]], [[1, 1]])


def test_structure_edge():
    assert not same_structure_as([], 1)
    assert same_structure_as([1, "[", "]"], ["[", "]", 1])
