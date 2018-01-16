# """
# >>> advise_player('A', 'K')
# 21 Blackjack!
# >>> advise_player(10, 5)
# 15 Hit.
# >>> advise_player('Q', 5)
# 15 Hit.
# >>> advise_player('J', 'K')
# 20 Stay.
# >>> advise_player(10, 5, 'J')
# 25 You lost.
# >>> advise_player()
# Traceback (most recent call last):
#     ...
# ValueError: Requires at least 2 arguments.
# """

def advise_player(c1, c2):

    cardValueKey = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
    handValue = cardValueKey[c1] + cardValueKey[c2]

    if handValue >= 17:
        print("{} Stay".format(handValue))

    elif handValue == 21:
        print("{} 21 Blackjack!".format(handValue))

    elif handValue <= 17:
        print("{} Hit me baby one more time".format(handValue))

    elif handValue > 21:
        print("{} You lost".format(handValue))


print(advise_player('3', '5'))


















# LAB: 21 ADVICE
# DELIVERY METHOD: DOCTEST
# GOAL
# Write a function that advises a player on the best next move in a round of blackjack.
#
# INSTRUCTIONS
# For now, just use 15 as a Hit/Stay Threshold, and ignore the case of two Aces.
#
# ADVANCED
#
# Implement a solution that employs a dictionary
# Write an additional doctest and execute it
