from . import dealer, player, card
from dealer import Dealer
from player import Player

class round():
    _number_of_players = int
    _dealer = Dealer
    _players = list

    def add_player(self, name:str) -> bool:
        if len(name) == 0:
            name = str(len(self.players))
        new_player = Player(name)
        self.players.append(new_player)
        self.number_of_players += 1
        return True

    def add_dealer(self) -> None:
        self._dealer = Dealer()

    def __init__(self):
        self.add_dealer()
        self._number_of_players = 0
        self._players = []
        return self 