from player import Player

class Leaderboard:
    def __init__(self, players: list[Player]):
        self.players = players
        self.sortLeaderboard()
    

    # sort leaderboard by money
    def sortLeaderboard(self):
        self.players.sort(key=lambda x: x.money, reverse=True)

    def addPlayer(self, pushinp: Player):
        # O(n)
        self.players.append(pushinp)
    

    # def printLeaderBoard(self):