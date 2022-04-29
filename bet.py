from typing_extensions import Self
from horse import Horse
from player import Player


class Bet:
    def __init__(self):
        self.player = None
        self.money = None
        self.horse = None

    # Assume amount <= self.money
    # And amount > 0   
    # call player.subtractMoney
    # then set fields to the given parameters
    # return self
    def makeBet(self, player: Player, horse: Horse, amount: int) -> Self:
        return None