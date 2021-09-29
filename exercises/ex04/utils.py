"""List utility functions."""

__author__ = "730490041"


# TODO: Implement your functions here.
def all(a: list[int], b: int) -> bool:
    """Test if all values in a list are the same. """
    i: int = 0
    count: int = 0
    if len(a) > 0:
        while i < len(a):
            if a[i] == b:
                i = i + 1
                count = count + 1
            else:
                i = i + 1
        return(count == (len(a)))
    else:
        return False


def is_equal(a: list[int], b: list[int]) -> bool:
    """Test if two lists are equal. """
    if len(a) == len(b):
        i: int = 0
        num: int = 0
        while i < len(a):
            if a[i] == b[i]:
                i = i + 1
                num = num + 1
            else:
                i = i + 1
        return (num == len(a))
    else:
        return False


def max(input: list[int]) -> int:
    """Gets the max value of a list of int. """
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        input.sort()
        return input[-1]