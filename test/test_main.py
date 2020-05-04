import unittest 
from Game import Game

class Test_Game(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for i in range(n): 
            self.g.roll(pins)

    def roll_many_spares(self, n, ball_one, ball_two):
        for i in range(n):
            self.g.roll(ball_one)
            self.g.roll(ball_two)

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

    def roll_strike(self):
        self.g.roll(10)

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.g.get_score())

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(300, self.g.get_score())

    def test_highest_spare(self):
        self.roll_many_spares(10, 9, 1)
        self.g.roll(9)
        self.assertEqual(190, self.g.get_score())


    
if __name__ == '__main__':
    unittest.main()
