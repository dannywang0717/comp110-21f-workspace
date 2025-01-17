"""Create your own adventure project."""
__author__ = "730490041"
import random
BYE_EMOJI: str = "\U0001F917"
player: str = ""
points: int = 0
answer: str = ""


def main() -> None:
    """Main function."""
    greet()
    global points
    global answer
    print("Where do you want to go?")
    while answer != ("N"):
        path = int(input("Enter 1 to start Coin Flip Game, Enter 2 to start Number Game, Enter 3 to Enter Emoji Printing Shop, Enter 4 to Exit Game  "))
        if (path == 1):
            coingame()
            answer = input("Main Menu? Y or N ")
        elif (path == 2):
            numbergame()
            answer = input("Main Menu? Y or N ")
        elif (path == 3):
            shop(points)
            print(f"You have {points} Total Points")
            answer = input("Main Menu? Y or N ")
        elif (path == 4):
            answer = "N"
    print("Goodbye! " + BYE_EMOJI)

    return None


def greet() -> None:
    """Greets the player and ask for name."""
    print("Welcome!!! This is a game to see how many points you can get which can be used in the Emoji Printing Shop")
    global player
    player = (input("First, What is your name? "))
    return None


def coingame() -> None:
    """A coin game that counts how many guesses are correct in a row."""
    i: int = 0
    global points
    global player
    while i < 1:
        flip: int = random.randint(0, 1)
        if (flip == int(input((player) + " Guess Heads(0) or Tails(1)? "))):
            points = points + 1
            print(player + " You are Correct! Now guess again")
        else:
            i = i + 1
            print(player + " You are Incorrect!")
    print(f"You have {points} Total Points")
    return None
            

def numbergame() -> None:
    """A number game to test the ability of mutplication (1-9) * (1-9)."""
    i: int = 0
    global points
    while i < 1:
        num1: int = (random.randint(1, 9))
        num2: int = (random.randint(1, 9))
        guess: int = int(input(f"What does {num1} x {num2}= "))
        if((num1 * num2) == guess):
            points = points + 1
            print(f"Correct, you know have {points} Total Points!!")
        else:
            i = i + 1
            print(f"Incorrect you now have {points} Total Points")
    return None


def shop(a: int) -> int:
    """Emoji printing shop that allows the points earned to be used."""
    lion: str = "\U0001F981"
    turtle: str = "\U0001F422"
    dragon: str = "\U0001F409"
    global points
    if a > points:
        print("You dont have that many points")
    while (a > 0):
        print(lion + " = 1 point" + turtle + " = 2 points" + dragon + " = 3 points")
        emoji: int = int(input("What emoji do you want to purchase? 1 for lion   2 for turtle   3 for dragon    "))
        if (emoji <= a):
            if (emoji == 1):
                points = points - 1
                a = a - 1
                print(lion)
            elif (emoji == 2):
                points = points - 2
                a = a - 2
                print(turtle)
            elif (emoji == 3):
                points = points - 3
                a = a - 3
                print(dragon)
        else:
            print("You dont have enough with your budget")
    return points


if __name__ == "__main__":
    main()