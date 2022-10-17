import pytest

from learn_github_actions.multiply import multiply


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 2), (2, 1, 2), (0, 1, 0), (-1, 2, -2), (-2, 1, -2), (0, 15, 0)],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
