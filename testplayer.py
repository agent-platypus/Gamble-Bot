import unittest

from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player('jett')

    def testConstructor(self):
        self.assertEqual(self.player.name, 'jett')
        self.assertEqual(self.player.money, 100)

if __name__ == '__main__':
    unittest.main()