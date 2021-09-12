"""Finding duplicate letters in a word."""

__author__ = "730490041"
word: str = input("Enter a word: ")
i: int = 0
count: int = 0

while i < len(word):
    j: int = 0
    while j < len(word):
        if word[i] == word[j]:
            count = count + 1
            j = j + 1
        else:
            j = j + 1
    i = i + 1
print("Found duplicate: " + str((count - len(word)) >= 1))