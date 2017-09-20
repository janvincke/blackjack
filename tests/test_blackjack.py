import pytest

from blackjack import Card, Deck


def test_cards():
    pass


def test_deck():
    pass


def test_card_has_suit():
    card = Card('diamond')
    assert hasattr(card, 'suit')


def test_card_has_valid_suit():
    with pytest.raises(ValueError):
        Card('robotrics')

    c = Card('spade')
    assert c.suit == 'spade'
