from player import Player
import errors

class Leaderboard:
    def __init__(self, players: list[Player]):
        self.players = players
        self.sortLeaderboard()
    

    # sort leaderboard by money
    def sortLeaderboard(self):
        self.players.sort(key=lambda x: x.money, reverse=True)

    def addPlayer(self, pushinp: Player):
        # O(n)
        for x in self.players:
            if x.name == pushinp.name:
                raise errors.RedundantPlayerError()        
        #self.players.append(pushinp)
        for i in range (len(self.players)-1):
            # checking player money, from greatest to least
            if pushinp.money >= self.players[i].money:
                self.players.insert(i,pushinp)
                break
            


        
    
    #deez
    # def printLeaderBoard(self):