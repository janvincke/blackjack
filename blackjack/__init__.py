class Card:
    def __init__(self, suit):
        if suit not in ['diamond', 'heart', 'spade', 'club']:
            raise ValueError('This is a standard card game. Suit must be in '
                             'diamond, heart, spade, club')
        self.suit = suit


class Deck:
    pass

