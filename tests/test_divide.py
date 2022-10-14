from learn_github_actions.divide import divide


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(2, 1) == 2
    assert divide(0, 1) == 0
    assert divide(-1, 2) == -0.5
    assert divide(-2, 1) == -2
    assert divide(0, 15) == 0
