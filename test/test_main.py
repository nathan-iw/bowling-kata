import unittest 
from Game import Game
from unittest.mock import Mock, patch, call, MagicMock


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

    def get_many_user_rolls(self, num):
        for i in range(num):
            self.g.get_user_roll()

    @patch("builtins.input")
    def test_current_score(self, pinput):
        # arrange

        pinput.side_effect = ["1", "1", "1", "1"]
        expected = [2, 2]
        exp_total = 4
        # act
        self.get_many_user_rolls(4)
        actual = self.g.get_current_score()
        act_total = self.g.total
        #  [2, 2] Total: 4
        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(exp_total, act_total)

    @patch("builtins.input")
    def test_current_score_spares(self, pinput):
        # arrange

        pinput.side_effect = ["9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9", "1", "9"]
        expected = [19, 19, 19, 19, 19, 19, 19, 19, 19, "/"]
        exp_total = 171
        # act
        self.get_many_user_rolls(20)
        actual = self.g.get_current_score()
        act_total = self.g.total
        #  [2, 2] Total: 4
        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(exp_total, act_total)
        
        
if __name__ == '__main__':
    unittest.main()
