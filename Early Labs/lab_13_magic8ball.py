import random

ballAnswers = [ "yes",  "nope", "maybe", "ask again later", "you're annoying stop asking me questions", "I have no idea, I hope you're not using this to make an important decision"]

userQuestion = input("please enter your question to ask the magic ball here: ")

def magicHappening():
    return random.choice(ballAnswers)

# print(magicHappening())

print(random.shuffle(ballAnswers))
