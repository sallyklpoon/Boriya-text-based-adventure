from unittest import TestCase
from unittest.mock import patch

from game import roll


class TestRoll(TestCase):

    def test_roll_1_die_1_side(self):
        die = (1, 1)
        expected = range(1, die[1] * die[0] + 1)
        actual = roll(die)
        self.assertIn(actual, expected)

    def test_roll_1_die_6_sides(self):
        die = (1, 6)
        expected = range(1, die[1] * die[0] + 1)
        actual = roll(die)
        self.assertIn(actual, expected)

    def test_roll_2_dice_20_sides(self):
        die = (2, 20)
        expected = range(1, die[1] * die[0] + 1)
        actual = roll(die)
        self.assertIn(actual, expected)

    @patch ('random.randint', return_value=16)
    def test_roll_3_dice_8_sides(self, mock_randint):
        dice = (3, 8)
        actual = roll(dice)
        self.assertEqual(actual, 16)
