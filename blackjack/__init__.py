
import random


class Card:
    """Card of a standard card deck"""
    def __init__(self, suit, value):
        if suit not in ['diamond', 'heart', 'spade', 'club']:
            raise ValueError('This is a standard card game. Suit must be in '
                             'diamond, heart, spade, club')
        self.suit = suit

        if value not in ['A', 'K', 'Q', 'J'] and value not in list(range(2,11)):
            raise ValueError

        self.value = value

        if value in ['K', 'Q', 'J']:
            self.numeric_value = 10
        elif value == 'A':
            self.numeric_value = 11
        else:
            self.numeric_value = value

    def __add__(self, other):
        return self.numeric_value + other.numeric_value

    def __gt__(self, other):
        return self.numeric_value > other.numeric_value

    def __eq__(self, other):
        return self.numeric_value == other.numeric_value

    def __repr__(self):
        return '<{} of {}s>'.format(self.value, self.suit)

    def __str__(self):
        return repr(self)


class Deck:

    """"A Standard deck class with 52 cards, 13 cards in each suit"""

    def __init__(self):

        self.cards = []

        for suit in ['diamond', 'heart', 'spade', 'club']:
            for value in list(range(2,11)) + ['A', 'K', 'Q', 'J']:
                self.cards.append(Card(suit, value))

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            card = self.cards.pop(0)
            return card

        except IndexError:
            raise StopIteration('Deck is out of cards')

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self):
        return [self._deal_card(), self._deal_card()]

    def deal_card(self):
        return self._deal_card()

    def _deal_card(self):
        """

        :param cards (int):
        :return: number of cards from our deck
        """
        return next(self)


class Hand:
    """Number of cards owned by a player or the dealer"""
    def __init__(self, deck):
        self.deck = deck
        self.cards = deck.deal_hand()
        if self.cards[0].value == 'A' and self.cards[1].value == 'A':
            self.value = 12
        else:
            self.value = self.cards[0] + self.cards[1]
        print("My value is: {}\n"
              "My cards are: \n{}".format(self.value, self.cards))

    def get_card(self):
        self.cards.append(self.deck.deal_card())
        if self.cards[-1].value != 'A':
            self.value += self.cards[-1].numeric_value
        elif self.value < 11:
            self.value += 11
        else:
            self.value += 1
        print("My new value is: {}\n"
              "My cards are: \n{}".format(self.value, self.cards))
