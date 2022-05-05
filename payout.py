from bet import Bet
from errors import AmountTooLargeError, AmountTooSmallError, BetDoesNotExistError, MultipleBetError
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
        if (amount <= 0):
            raise AmountTooSmallError()
        if (amount > player.money):
            raise AmountTooLargeError()
        bet: Bet
        for bet in self.bets:
            if bet.player.name == player.name:
                raise MultipleBetError()
        newBet = Bet()
        newBet.makeBet(player, horse, amount)
        self.bets.append(newBet)

    # pay out every player that bet on the winner
    # according to the winners odds
    def payoutPlayers(self, winner: Horse):
        bet: Bet
        for bet in self.bets:
            if bet.horse.name == winner.name:
                payoutMultiplier = (1 - winner.winProbability) / winner.winProbability
                bet.player.addMoney(bet.money + (bet.money * payoutMultiplier))

    # remove given bet from bets
    # give bet money back to player
    # if bet does not exist, raise BetDoesNotExistError
    def removeBet(self, playerName: str):
        found = 0
        bet: Bet
        for bet in self.bets:
            if bet.player.name == playerName:
                bet.player.addMoney(bet.money)
                self.bets.remove(bet)
                found = 1
        if found == 0:
            raise BetDoesNotExistError()