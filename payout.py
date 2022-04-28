from bet import Bet
from horse import Horse
from player import Player


class Payout:
    def __init__(self):
        self.bets = None

    # call player.bet() and use the bet returned to add it to bets
    def addBet(player: Player, horse: Horse, amount: int):
        pass

    # pay out every player that bet on the winner
    # according to the winners odds
    def payoutPlayers(winner: Horse):
        pass