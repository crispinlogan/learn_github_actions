from learn_github_actions.subtract import subtract


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1
    assert subtract(-1, 2) == -3
    assert subtract(-2, 1) == -3
    assert subtract(0, 15) == -15
