from horse import Horse
from payout import Payout

class Bet:
    NUM_HORSES = 3

    # TODO: initialize the horses and add them to the list
    def __init__(self):
        self.horses = []
        self.winner = None
        self.payout = Payout()

    # choose a winner based on probabilities and return them
    # then call payout.payoutPlayers
    # then call leaderboard.sortLeaderboard
    def startGame():
        pass