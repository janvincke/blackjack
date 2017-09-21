class Card:

    def __init__(self, suit, value):
        if suit not in ['diamond', 'heart', 'spade', 'club']:
            raise ValueError('This is a standard card game. Suit must be in '
                             'diamond, heart, spade, club')
        self.suit = suit

        if value not in ['A', 'K', 'Q', 'J'] and value not in list(range(2,11)):
            raise ValueError

        self.value = value


class Deck:
    pass

