from .card import Card

class Player():
    _name = str
    _hand = list
    _is_winning = True

    def draw_card(self):
        new_card = Card()
        self.hand.append(new_card)

    def get_hand_sum(self):
        return sum([card.value for card in self._hand])

    def get_is_winning(self):
        return self._is_winning

    def get_name(self) -> str:
        return self._name

    def __init__(self, name:str) -> object:
        self._name = name
        self._hand = []
        return self