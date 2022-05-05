from bet import Bet
from horse import Horse
from player import Player


class Payout:
    def __init__(self):
        self.bets = []

    # call Bet.makeBet and use the bet returned to add it to bets
    # if amount <= 0 raise BetTooSmallError
    # if amount > player.money raise BetTooLargeError
    # if player has already made a bet, raise MultipleBetError 
    def addBet(self, player: Player, horse: Horse, amount: int):
        pass

    # pay out every player that bet on the winner
    # according to the winners odds
    def payoutPlayers(self, winner: Horse):
        pass

    # remove given bet from bets
    # give bet money back to player
    # if bet does not exist, raise BetDoesNotExistError
    def removeBet(self, playerName: str):
        pass