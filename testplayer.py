import unittest

from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player('jett')

    def testConstructor(self):
        self.assertEqual(self.player.name, 'jett')
        self.assertEqual(self.player.money, 100)
    
    def testSubtractMoneyRegularInput(self):
        self.player.subtractMoney(50)
        self.assertEqual(self.player.money, 50)

    def testSubtractMoneyMaxInput(self):
        self.player.subtractMoney(100)
        self.assertEqual(self.player.money, 0) 
    
    def testSubtractMoneyMinInput(self):
        self.player.subtractMoney(1)
        self.assertEqual(self.player.money, 99)

    def testSubtractMoneyTwice(self):
        self.player.subtractMoney(25)
        self.player.subtractMoney(50)
        self.assertEqual(self.player.money, 25)

if __name__ == '__main__':
    unittest.main()