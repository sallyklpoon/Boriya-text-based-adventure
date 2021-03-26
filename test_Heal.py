from unittest import TestCase
from unittest.mock import patch

from game import heal


class TestHeal(TestCase):

    @patch('game.roll', return_value=3)
    def test_heal_no_change_if_at_max_health(self, mock_roll):
        sample_character = {"HP": 20, "hit_dice": (1, 4), "max-HP": 20}
        heal(sample_character)
        self.assertEqual(sample_character["HP"], sample_character["HP"])

    @patch('game.roll', return_value=4)
    def test_heal_does_not_heal_over_max_health(self, mock_roll):
        sample_character = {"HP": 17, "hit_dice": (1, 4), "max-HP": 20}
        expected_hp = 20
        heal(sample_character)
        self.assertEqual(expected_hp, sample_character["HP"])

    @patch('game.roll', return_value=6)
    def test_heal_adds_rolled_hit_dice_to_HP(self, mock_roll):
        sample_character = {"HP": 2, "hit_dice": (1, 8), "max-HP": 20}
        expected_hp = 8
        heal(sample_character)
        self.assertEqual(expected_hp, sample_character["HP"])
