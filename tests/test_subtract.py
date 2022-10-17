import pytest

from learn_github_actions.subtract import subtract


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, -1), (2, 1, 1), (0, 1, -1), (-1, 2, -3), (-2, 1, -3), (0, 15, -15)],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
