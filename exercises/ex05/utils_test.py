"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730490041"


def test_only_evens() -> None:
    """Edge Case Test for the only_evens function."""
    xs: list[int] = [2]
    assert only_evens(xs)


def test_only_evens_1() -> None:
    """First Use Case Test for the only_evens function."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs)


def test_only_evens_2() -> None:
    """Second Use Case Test for the only_evens function."""
    xs: list[int] = [2, 2, 4, 8, 9]
    assert only_evens(xs)


def test_sub() -> None:
    """Edge Case Test for the sub function."""
    xs: list[int] = []
    a: int = 1
    b: int = 5
    assert sub(xs, a, b)


def test_sub_1() -> None:
    """First Use Case Test for the sub function."""
    xs: list[int] = [1, 2, 3, 4, 5]
    a: int = 1
    b: int = 3
    assert sub(xs, a, b)


def test_sub_2() -> None:
    """Second Use Case Test for the sub function."""
    xs: list[int] = [2, 3, 4, 5]
    a: int = 1
    b: int = 4
    assert sub(xs, a, b)


def test_concat() -> None:
    """Edge Case Test for the concat function."""
    xs: list[int] = [1]
    xt: list[int] = [1]
    assert concat(xs, xt)


def test_concat_1() -> None:
    """First Use Case Test for the concat function."""
    xs: list[int] = [1, 2, 3, 4]
    xt: list[int] = [1, 2, 3]
    assert concat(xs, xt)


def test_concat_2() -> None:
    """Second Use Case Test for the concat function."""
    xs: list[int] = [1, 4, 4]
    xt: list[int] = [1, 2, 3]
    assert concat(xs, xt)