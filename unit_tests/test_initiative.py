from unittest import TestCase
from unittest.mock import patch

from game import initiative


class TestInitiative(TestCase):

    @patch('random.randint', side_effect=[38, 35, 66, 33])
    def test_initiative_only_returns_if_no_initiative_draw(self, mock_randint):
        character = {"initiative_modifier": 2}
        foe = {"initiative_modifier": 5}
        self.assertTrue(initiative(character, foe))

    @patch('random.randint', side_effect=[10, 11])
    def test_initiative_false_if_foe_rolls_higher_than_character(self, mock_randint):
        character = {"initiative_modifier": 3}
        foe = {"initiative_modifier": 3}
        self.assertFalse(initiative(character, foe))

    @patch('random.randint', side_effect=[100, 33])
    def test_initiative_true_if_character_rolls_higher_than_foe(self, mock_randint):
        character = {"initiative_modifier": 10}
        foe = {"initiative_modifier": 6}
        self.assertTrue(initiative(character, foe))
