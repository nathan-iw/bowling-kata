import unittest 
from Game import Game

class Test_Game(unittest.TestCase):


    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for i in range(n): 
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.g.get_score())

    
    def test_all_one(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.g.get_score())

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(17,0)
        self.assertEqual(16, self.g.get_score())

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)


    
if __name__ == '__main__':
    unittest.main()
