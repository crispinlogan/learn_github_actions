from typing import List


def add(a: int, b: int) -> int:
    """Adds the second arg to the first arg and returns the result"""
    return a + b


def add_lists(a: List, b: List) -> int:
    """Adds each element of the first list to each element in the second
    list and returns the result. Input lists need to be the same length"""
    if len(a) != len(b):
        raise ValueError(
            "Input args are not same length lists. They need to be same length"
        )

    ret = []
    for el_a, el_b in zip(a, b):
        ret.append(el_a + el_b)

    return ret
