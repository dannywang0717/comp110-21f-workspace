"""List utility functions part 2."""

__author__ = "730490041"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Returns all even numbers in a give list."""
    evens = []
    for i in a:
        if i % 2 == 0:
            evens.append(i)

    return evens


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Returns a sublist given a start and end index."""
    if len(a) == 0:
        return []
    elif b < 0:
        return a[0:c]
    elif c > len(a):
        return a[b:len(a)]
    return a[b:c]


def concat(a: list[int], b: list[int]) -> list[int]:
    """Concats two list together."""
    new = []
    new = a + b
    return new


num = [1, 2, 3, 4, 5, 6]
num2 = [1, 2, 3, 4, 5, 6, 7]

print(concat(num, num2))