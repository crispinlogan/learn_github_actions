from learn_github_actions.multiply import multiply


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(2, 1) == 2
    assert multiply(0, 1) == 0
    assert multiply(-1, 2) == -2
    assert multiply(-2, 1) == -2
    assert multiply(0, 15) == 0
