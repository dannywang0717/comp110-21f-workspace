"""Repeating a beat in a loop."""

__author__ = "730490041"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
count: int = int(input("How many times do you want to repeat it? "))

i: int = 0

if count <= 0:
    print("No beat...")
else:
    while i < count:
        print(beat)
        i = i + 1