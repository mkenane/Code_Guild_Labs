print("Hello! the computer has chosen a number between 0 and 2 billion try to guess that number, you have 20 tries!")

import random
numberOfTries = 0
computerNumber = random.randint(0, 2000000000)


while numberOfTries < 20:
    userGuess = int(input("try to guess the computers number: "))
    numberOfTries = numberOfTries + 1

    if computerNumber > userGuess:
        print("too low, guess again: ")
    elif computerNumber < userGuess:
        print("too high, guess again: ")
    elif computerNumber == userGuess:
        print("you got it! great job!")
        # q = input("play again?")
        # if q = "y":
        #     numberOfTries = 0
        #     computerNumber = random.randint(0, 2000000000)
        #     continue
