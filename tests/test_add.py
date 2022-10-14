import pytest

from learn_github_actions.add import add, add_lists


def test_add():
    assert add(1, 2) == 3
    assert add(2, 1) == 3
    assert add(0, 0) == 0
    assert add(-1, 2) == 1
    assert add(-2, 1) == -1
    assert add(0, 15) == 15


def test_add_lists():
    assert add_lists([3, 1], [1, 5]) == [4, 6]
    assert add_lists([], []) == []
    assert add_lists([1], [1]) == [2]


def test_add_lists_fails():
    with pytest.raises(ValueError):
        add_lists([1, 2], [1])
