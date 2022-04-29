from bet import Bet
from horse import Horse
from player import Player


class Payout:
    def __init__(self):
        self.bets = None

    # call Bet.makeBet and use the bet returned to add it to bets
    # if amount <= 0 or amount >= player.money
    # return an error and don't add bet
    def addBet(self, player: Player, horse: Horse, amount: int):
        pass

    # pay out every player that bet on the winner
    # according to the winners odds
    def payoutPlayers(self, winner: Horse):
        pass