"""Drawing forests in a loop."""

__author__ = "730490041"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
num: int = int(input("Depth: "))
i: int = 1
while i <= num:
    print(TREE * (i))
    i = i + 1