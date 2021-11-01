"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730490041"


def test_invert() -> None:
    """Edge Case Test for the invert function."""
    xs: dict[str, str] = {"a": "z"}
    assert invert(xs)


def test_invert_1() -> None:
    """First Use Case Test for the invert function."""
    xs: dict[str, str] = {"a": "z", "apple": "zebra"}
    assert invert(xs)


def test_invert_2() -> None:
    """Second Use Case Test for the invert function."""
    xs: dict[str, str] = {"a": "z", "cat": "dog", "one": "two"}
    assert invert(xs)


def test_favorite_color() -> None:
    """Edge Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red"}
    assert favorite_color(xs)


def test_favorite_color_1() -> None:
    """First Use Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red", "b": "red", "c": "blue", "d": "black"}
    assert favorite_color(xs)


def test_favorite_color_2() -> None:
    """Second Use Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red", "b": "red", "c": "red", "d": "black"}
    assert favorite_color(xs)


def test_count() -> None:
    """Edge Case Test for the count function."""
    xs: list = ["a"]
    assert count(xs)


def test_count_1() -> None:
    """First Use Case Test for the count function."""
    xs: list = ["a", "a", "b"]
    assert count(xs)


def test_count_2() -> None:
    """Second Use Case Test for the count function."""
    xs: list = ["a", "a", "a", "c", "c", "b"]
    assert count(xs)