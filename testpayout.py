from multiprocessing.pool import INIT
import unittest
from payout import Payout
from player import INIT_MONEY, Player
from bet import Bet
from horse import Horse
import errors

class TestPlayer(unittest.TestCase):
    
    def setUp(self) -> None:
        self.payout = Payout()

    def testConstructor(self):
        self.assertTrue(len(self.payout.bets) == 0)

    def testAddBetOneBet(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        self.payout.addBet(player, horse, INIT_MONEY / 2)
        self.assertTrue(len(self.payout.bets) == 1)
        bet = self.payout.bets[0]
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, INIT_MONEY / 2)
    
    def testAddBetMinBet(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        self.payout.addBet(player, horse, 1)
        self.assertTrue(len(self.payout.bets) == 1)
        bet = self.payout.bets[0]
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, 1)
    
    def testAddBetMaxBet(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        self.payout.addBet(player, horse, INIT_MONEY)
        self.assertTrue(len(self.payout.bets) == 1)
        bet = self.payout.bets[0]
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, INIT_MONEY)

    def testAddBetTwoBets(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        self.payout.addBet(player, horse, INIT_MONEY / 2)
        self.assertTrue(len(self.payout.bets) == 1)
        bet = self.payout.bets[0]
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, INIT_MONEY / 2)

        player2 = Player('reyna')
        horse2 = Horse('donkey', 0.5)
        self.payout.addBet(player, horse, INIT_MONEY)
        self.assertTrue(len(self.payout.bets) == 2)
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, INIT_MONEY / 2)
        bet2 = self.payout.bets[1]
        self.assertEqual(bet2.player, 'reyna')
        self.assertEqual(bet2.horse, 'donkey')
        self.assertEqual(bet2.money, INIT_MONEY)

    def testAddBetZero(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        with self.assertRaises(errors.BetTooSmallError):
            self.payout.addBet(player, horse, 0)
        self.assertTrue(len(self.payout.bets) == 0)

    def testAddBetNegativeBet(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        with self.assertRaises(errors.BetTooSmallError):
            self.payout.addBet(player, horse, -1)
        self.assertTrue(len(self.payout.bets) == 0)
    
    def testAddBetTooBig(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        with self.assertRaises(errors.BetTooLargeError):
            self.payout.addBet(player, horse, INIT_MONEY + 1)
        self.assertTrue(len(self.payout.bets) == 0)
    
    def testAddBetWayTooBig(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        with self.assertRaises(errors.BetTooSmallError):
            self.payout.addBet(player, horse, INIT_MONEY + 5000)
        self.assertTrue(len(self.payout.bets) == 0)
    
    def testAddBetSamePlayerTwoBets(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        self.payout.addBet(player, horse, INIT_MONEY / 2)
        self.assertTrue(len(self.payout.bets) == 1)
        bet = self.payout.bets[0]
        self.assertEqual(bet.player, 'jett')
        self.assertEqual(bet.horse, 'horsey')
        self.assertEqual(bet.money, INIT_MONEY / 2)

        with self.assertRaises(errors.MultipleBetError):
            self.payout.addBet(player, horse, INIT_MONEY / 2)
        self.assertTrue(len(self.payout.bets) == 1)

    def testPayoutPlayersOneBetOneWinner(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        betAmount = INIT_MONEY / 2
        self.payout.addBet(player, horse, betAmount)
        balanceAfterBet = player.money
        self.payout.payoutPlayers(horse)
        self.assertEqual(player.money, balanceAfterBet + (betAmount * 2))

    def testPayoutPlayersThreeToOneOdds(self):
        player = Player('jett')
        horse = Horse('horsey', 0.25)
        betAmount = INIT_MONEY / 2
        self.payout.addBet(player, horse, betAmount)
        balanceAfterBet = player.money
        self.payout.payoutPlayers(horse)
        self.assertEqual(player.money, balanceAfterBet + (betAmount * 4))

    def testPayoutPlayersOneBetNoWinners(self):
        player = Player('jett')
        horse = Horse('horsey', 0.5)
        betAmount = INIT_MONEY / 2
        self.payout.addBet(player, horse, betAmount)
        balanceAfterBet = player.money
        horse2 = Horse('donkey', 0.5)
        self.payout.payoutPlayers(horse2)
        self.assertEqual(player.money, balanceAfterBet)

if __name__ == '__main__':
    unittest.main()