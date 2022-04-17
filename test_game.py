from pytest import fixture,mark
from game import *


@fixture
def card_instance() -> Card:
    card = Card()
    card.numbers[0][1]= 5
    return card


@fixture
def player_instance(card_instance, number=1) -> Player:
    player = Player(card_instance, number)
    return player


class TestCard:

    def test_get_one_list(self, card_instance):
        lst = card_instance.get_one_list()
        assert len(lst) == 27


class TestPlayer:
    def test_init(self, card_instance):
        card = card_instance
        player = Player(card)
        assert player.card == card

    def test_computer_turn(self, player_instance):
        number = 5
        player_instance.computer_turn(number)
        assert player_instance.card.COUNT_NUMBERS == 14

    @mark.parametrize("number, answer, expected_result", [
        (5, "n", "Игрок 1 проиграл!"),
        (91, "y", "Игрок 1 проиграл!")
    ])
    def test_player_turn(self, number, answer, expected_result, player_instance):
        assert player_instance.player_turn(number, answer) == expected_result

