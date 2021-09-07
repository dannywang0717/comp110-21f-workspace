"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730490041"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
i: int = 0
print("Your fortune cookie says...")
num = randint(1, 4)
if num == 1:
    print("A fresh start will put you on your way.")      
elif num == 2:
    print("You should def go for it")
elif num == 3:
    print("Follow what calls you.")
elif num == 4:
    print("To be found, stop hiding.")
print("Now, go spread positive vibes!")
