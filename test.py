import pytest


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def descending_order(num: int) -> int:
    return int(''.join(sorted(str(num), reverse=True)))




def test_descending_order():
    assert descending_order(12345) == 54321
    assert descending_order(54321) == 54321
    assert descending_order(9000) == 9000
    assert descending_order(0) == 0
    assert descending_order(13579) == 97531