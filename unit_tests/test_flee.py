from unittest import TestCase
from unittest.mock import patch

from game import flee, FLEE_SUCCEED_CHANCE


class TestFlee(TestCase):

    @patch('random.randint', side_effect=[FLEE_SUCCEED_CHANCE(), 2])
    def test_flee_damages_character_if_unsuccessful(self, mock_randint):
        character = {"HP": 10}
        foe = {"name": "Pablo Picasso", "attacks": ["Cubism", "Modern Art"], "boss": False}
        expected = {"HP": 8}
        flee(character, foe)
        self.assertEqual(expected, character)

    @patch('random.randint', return_value=FLEE_SUCCEED_CHANCE() + 1)
    def test_flee_does_not_affect_character_if_successful(self, mock_randint):
        character = {"HP": 20}
        foe = {"name": "Van Gogh", "attacks": ["Impressionism", "Painting"], "boss": False}
        expected = character
        flee(character, foe)
        self.assertEqual(expected, character)

    def test_flee_does_not_affect_character_if_foe_is_boss(self):
        character = {"HP": 20}
        foe = {"name": "Keith", "attacks": ["Dancing", "Skateboarding"], "boss": True}
        expected = character
        flee(character, foe)
        self.assertEqual(expected, character)
