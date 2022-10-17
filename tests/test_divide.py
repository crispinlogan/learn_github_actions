import pytest

from learn_github_actions.divide import divide


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 0.5), (2, 1, 2), (0, 1, 0), (-1, 2, -0.5), (-2, 1, -2), (0, 15, 0)],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected
