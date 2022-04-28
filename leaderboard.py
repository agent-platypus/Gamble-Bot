from player import Player

class Leaderboard:
    def __init__(self, players: list[Player]):
        self.players = []
        for player in players:
            self.players.append(player)
        self.sortLeaderboard()

    # sort leaderboard by money
    def sortLeaderboard(self):
        self.players.sort(key=lambda x: x.money, reverse=True)