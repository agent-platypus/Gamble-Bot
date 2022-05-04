from leaderboard import Leaderboard
from payout import Payout
from race import Race

class Game:

    def __init__(self, leaderboard: Leaderboard):
        self.race = Race()
        self.leaderboard = leaderboard
        self.payout = Payout()

    # Start race, then payout players, then update leaderboard
    def startGame(self):
        pass