from learn_github_actions.add import add


def test_add():
    assert add(1, 2) == 3
    assert add(2, 1) == 3
    assert add(0, 0) == 0
    assert add(-1, 2) == 1
    assert add(-2, 1) == -1
    assert add(0, 15) == 15
