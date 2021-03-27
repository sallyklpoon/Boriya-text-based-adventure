from unittest import TestCase
from unittest.mock import patch

from game import flee_boss, FLEE_SUCCEED_CHANCE


class Test(TestCase):

    @patch('random.randint', side_effect=[FLEE_SUCCEED_CHANCE()-1, 2])
    def test_flee_boss_character_takes_damage_if_under_flee_succeed_chances(self, mock_randint):
        boss = {"name": "Bob", "attacks": ["Attack1", "Attack2"]}
        character = {"HP": 10}
        expected = character["HP"] - 2
        flee_boss(character, boss)
        self.assertEqual(expected, character["HP"])

    @patch('random.randint', side_effect=[FLEE_SUCCEED_CHANCE()+1])
    def test_flee_boss_character_takes_no_damage_if_flee_succeeds(self, mock_randint):
        boss = {"name": "Bob", "attacks": ["Attack1", "Attack2"]}
        character = {"HP": 10}
        expected = character["HP"]
        flee_boss(character, boss)
        self.assertEqual(expected, character["HP"])
