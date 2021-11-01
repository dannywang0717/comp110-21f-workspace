"""Practice with dictionaries."""

__author__ = "730490041"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the key and the value of a dictionary."""
    result: dict[str, str] = {}
    result = {x: y for y, x in a.items()}
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Finds the favorite color of a dictionary."""
    x = b.values()
    duplicate = []
    unique = []
    for i in x:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    if len(duplicate) > 0:
        return str(duplicate[0])
    else:
        return str(unique[0])
    

def count(c: list[str]) -> dict[str, int]:
    """Creats a dictionary given a list of string and the value is the count it repeats."""
    empty = {}
    for i in c:
        if i in empty.keys():
            empty[i] += 1
        else:
            empty[i] = 1
    return empty     