
from random import random

POSSIBLE_VALUES = [1,2,3,4,5,6,7,8,9,10,10,10,10]
POSSIBLE_SUITS = ["Hearts","Clubs","Diamonds","Spades"]

class Card():
    value = int
    suit = str
    _is_face_up = bool

    def _get_value(self):
        return self.value

    def _set_value(self) -> bool:
        index = random.randint(0,len(POSSIBLE_VALUES)-1)
        self.value = POSSIBLE_VALUES[index]

    def _set_suit(self) -> bool:
        index = random.randint(0,len(POSSIBLE_SUITS)-1)
        self.suit = POSSIBLE_SUITS[index]

    def turn_up(self):
        self._is_face_up = True

    def __init__(self, is_face_up:bool=True) -> None:
        self._is_face_up = is_face_up
        self._set_value()
        self._set_suit()