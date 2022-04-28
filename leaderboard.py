class Leaderboard:
    def __init__(self, players):
        self.players = []
        for player in players:
            self.players.append(player)
        self.players.sort(key=lambda x: x.money, reverse=True)