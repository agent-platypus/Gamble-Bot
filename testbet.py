import unittest
from player import Player
from horse import Horse 
from bet import Bet

class TestBet(unittest.TestCase):

    def setUp(self) -> None:
        self.bet = Bet()

    def testConstructor(self):
        self.assertIsNone(self.bet.player)
        self.assertIsNone(self.bet.money)
        self.assertIsNone(self.bet.horse)

    def testMakeBet(self):
        player = Player('jett')
        horse = Horse('horseman', 0.5)
        self.bet.makeBet(player, horse, 25)
        self.assertEqual(self.bet.player, player)
        self.assertEqual(self.bet.horse, horse)
        self.assertEqual(self.bet.money, 25)
        self.assertEqual(self.bet.player.money, Player.INIT_MONEY - 25)


    
if __name__ == '__main__':
    unittest.main()