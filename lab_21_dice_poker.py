from random import randrange

class Dice:


    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.rollAll()


    def rollAll(self):
        for index in range(5):
            self.dice[index] = randrange(1,7)

    def rollSelected(self, userselection):
        for selectedCards in userselection:
            self.dice[selectedCards] = randrange(1,7)
            #need to adjust for user selection to correct index (subtract 1)

    def values():
        return self.dice[:]

    def score(self):
        howMany = []
        for i in self.dice:
            occurences = self.dice.count(i)
            howMany.append(occurences)

        if sorted(howMany) == [1, 2, 2, 2, 2]:
            return "Two Pairs", 5

        elif sorted(howMany) == [1, 1, 3, 3, 3]:
            return "Three of a kind", 8

        elif sorted(howMany) == [2, 2, 3, 3, 3]:
            return "Full house", 12

        elif sorted(howMany) == [1, 4, 4, 4, 4]:
            return "Four of a Kind", 15

        elif sorted(howMany) == [1, 1, 1, 1, 1] : #and sum of how any equals 21
            return "Straight!", 20

        elif sorted(howMany) == [5, 5, 5, 5, 5]:
            return "Five of a Kind!", 30

        else:
            return "You Got Nothing!"
mydice = Dice()
print(mydice.dice)
print(mydice.score())
print(mydice.rollSelected([4]))
print(mydice.dice)
print(mydice.score())

class PokerApp:


    def __init__(self):
        self.dice = Dice()
        self.money = 100
        self.userInterface = PokerInterface


    def playRound(self):
        self.money = self.money - 10
        self.doRolls()

    def doRolls():
        self.dice.rollAll()
        roll = 1
        self.userInterface.values())


#
# def score(self):
#     counts = [0, 0, 0, 0, 0, 0, 0]
#     for value in self.dice:
#         counts[value] = counts[value] + 1
#     if 5 in counts:
#         return "Five of a Kind you lucky bastard"
