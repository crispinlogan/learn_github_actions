from typing import List


def subtract(a: int, b: int) -> int:
    """Subtracts the second arg from the first arg and returns the result"""
    return a - b


def subtract_lists(a: List, b: List) -> int:
    """Subtracts each element of the second list from each element in the first
    list and returns the result. Input lists need to be the same length"""
    if len(a) != len(b):
        raise ValueError(
            "Input args are not same length lists. They need to be same length"
        )

    ret = []
    for el_a, el_b in zip(a, b):
        ret.append(el_a - el_b)

    return ret
