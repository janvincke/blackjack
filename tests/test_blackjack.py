import pytest

from unittest.mock import MagicMock

from blackjack import Card, Deck, Hand


def test_cards():
    pass


def test_deck():
    pass


def test_card_has_suit():
    card = Card('diamond', 2)
    assert hasattr(card, 'suit')


def test_card_has_valid_suit():
    with pytest.raises(ValueError):
        Card('robotrics', 2)

    c = Card('spade', 2)
    assert c.suit == 'spade'


def test_card_has_a_value():
    king_of_spades = Card('spade', 'K')
    queen_of_spades = Card('spade', 'Q')

    assert king_of_spades.value == 'K'
    assert queen_of_spades.value == 'Q'


def test_add_card():
    assert 5 == Card('spade', 2) + Card('spade', 3)
    assert 13 == Card('spade', 'K') + Card('spade', 3)


def test_compare():
    assert True == (Card('spade', 'Q') == Card('spade', 'J'))


def test_greater_than():
    assert True == (Card('spade', 'Q') > Card('spade', 3))


def test_proper_repr():
    assert "<A of spades>" == repr((Card('spade', 'A')))


def test_init_deck():
    deck = Deck()
    assert len(deck.cards) == 52


def test_shuffle_deck():
    deck_a = Deck()
    deck_b = Deck()

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        assert c_a.value == c_b.value

    deck_b.shuffle()
    randomness = []

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        randomness.append(c_a.value != c_b.value)

    assert any(randomness)


def test_len_deck():
    deck = Deck()

    assert len(deck) == 52


def test_iter_deck():
    deck = Deck()

    assert next(deck) == Card('spade', 2)
    assert next(deck) == Card('spade', 3)


def test_deal_hands():
    deck = Deck()

    assert isinstance(deck.deal_card(), Card)

    deck = Deck()
    deck.shuffle()
    card1, card2 = deck.deal_hand()

    assert isinstance(card1, Card)
    assert isinstance(card2, Card)
    assert card1.value != card2.value or card1.suit != card2.suit


def test_hand_value():
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    assert isinstance(hand.cards[0], Card)
    assert isinstance(hand.cards[1], Card)

    hand.value = 20
    hand.deck.deal_card = MagicMock(return_value=Card('spade', 'A'))
    hand.get_card()
    assert hand.value == 21
