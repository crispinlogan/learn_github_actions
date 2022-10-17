import pytest

from learn_github_actions.add import add, add_lists


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (2, 1, 3), (0, 0, 0), (-1, 2, 1), (-2, 1, -1), (0, 15, 15)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


class TestAddList:
    @pytest.mark.parametrize(
        "a,b,expected", [([3, 1], [1, 5], [4, 6]), ([], [], []), ([1], [1], [2])]
    )
    def test_add_lists(self, a, b, expected):
        assert add_lists(a, b) == expected

    def test_add_lists_fails(self):
        with pytest.raises(ValueError):
            add_lists([1, 2], [1])
