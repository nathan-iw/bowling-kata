import unittest 
from Game import Game

class Test_Game(unittest.TestCase):

    def test_gutter_game(self):
        g = Game()
        for i in range(20): 
            g.roll(0)
        self.assertEqual(0, g.get_score())

    
    def test_all_one(self):
        g = Game()
        for i in range(20):
            g.roll(1)
        self.assertEqual(20, g.get_score())

    
if __name__ == '__main__':
    unittest.main()
