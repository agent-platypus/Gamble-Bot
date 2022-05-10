from bet import Bet
from errors import AmountTooLargeError, AmountTooSmallError, BetDoesNotExistError, HorseMissingError, MultipleBetError
from horse import Horse
from player import Player
from race import Race


class Payout:
    def __init__(self, race: Race):
        self.bets = []
        self.race = race

    # call Bet.makeBet and use the bet returned to add it to bets
    # if amount <= 0 raise BetTooSmallError
    # if amount > player.money raise BetTooLargeError
    # if player has already made a bet, raise MultipleBetError
    # TODO: account for when the horse does exist 
    def addBet(self, player: Player, horse: Horse, amount: int):
        if (amount <= 0):
            raise AmountTooSmallError()
        if (amount > player.money):
            raise AmountTooLargeError()
        raceHorse: Horse
        flag = 0
        for raceHorse in self.race.horses:
            if raceHorse.name == horse.name:
                flag = 1
        if flag == 0:
            raise HorseMissingError()
        bet: Bet
        for bet in self.bets:
            if bet.player.name == player.name:
                raise MultipleBetError()
        newBet = Bet(player, horse, amount)
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