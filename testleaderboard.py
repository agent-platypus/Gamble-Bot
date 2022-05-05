from re import X
import unittest
from leaderboard import Leaderboard

from player import Player

class TestLeaderboard(unittest.TestCase):

    def setUp(self) -> None:
        playerlist = [Player('ken'), Player('ray'), Player('mau'), Player('david'), Player('brandon')]
        playerlist[0].subtractMoney(10)
        playerlist[1].subtractMoney(25)
        playerlist[2].subtractMoney(15)
        playerlist[3].subtractMoney(5)
        playerlist[4].subtractMoney(30)
        self.leaderboard = Leaderboard(playerlist)

    def testSortMoney(self):
        #sorting expected: david, ken, mau, ray, brandon

        # testing number 1 standing
        self.assertEqual(self.leaderboard.players[0].money, 200)
    
    def testSortNames(self):
        # testing proper standing with corresponding names
        self.assertEqual(self.leaderboard.players[0].name, 'david')
        self.assertEqual(self.leaderboard.players[1].name, 'ken')
        self.assertEqual(self.leaderboard.players[2].name, 'mau')
        self.assertEqual(self.leaderboard.players[3].name, 'ray')
        self.assertEqual(self.leaderboard.players[4].name, 'brandon')

    def testAddplayer(self):
        self.leaderboard.addPlayer(Player('nancy'))
        self.assertEqual(self.leaderboard.players[0].name, 'nancy')
    


if __name__ == '__main__':
    unittest.main()
