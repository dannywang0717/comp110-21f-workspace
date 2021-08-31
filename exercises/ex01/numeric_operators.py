"""Shows how the four numeric operators work in python."""
__author__ = "730490041"
left: int = (int(input("Left-hand side: ")))
right: int = (int(input("Right-hand side: ")))
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))