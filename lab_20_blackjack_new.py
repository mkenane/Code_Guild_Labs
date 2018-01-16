

class Cards:
    def __init__(self, value, suit, rank):
        self.value = value
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck:

    def __init__(self):
        self.deck =  self.createdeck()

    def createdeck(self):
        deck_list = []


        card_values = {
            'Ace': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'King': 10,
            'Queen': 10
        }

        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


        for s in suits:
            for rank, value in card_values.items():
                deck_list.append(Cards(value, s, rank))
        return deck_list


deckpile = Deck()
# print(deckpile.deck)
