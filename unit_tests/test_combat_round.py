from unittest import TestCase
from unittest.mock import patch

from game import combat_round


class TestCombatRound(TestCase):

    @patch('random.randint', side_effect=[20, 2])
    def test_combat_round_crit_hit_damage_modified(self, mock_randint):
        attacker = {"AC": 12, "name": "Tyler", "attacks": ["Slice", "Sword"],
                    "atk_modifier": 0, "max-HP": 20, "damage": (1, 10), "HP": 15,
                    "crit_chance": [20], "crit_modifier": 2, "dmg_modifier": 1}
        opposition = {"AC": 15, "name": "Erika", "attacks": ["Hop", "Skip"],
                      "atk_modifier": 0, "max-HP": 12, "HP": 12, "damage": (1, 10),
                      "crit_chance": [20], "crit_modifier": 0, "dmg_modifier": 0}
        expected_opposition_health = opposition['HP'] - 5
        combat_round(attacker, opposition)
        self.assertEqual(expected_opposition_health, opposition['HP'])

    @patch('random.randint', side_effect=[14])
    def test_combat_round_initial_roll_under_opposition_AC_is_a_miss(self, mock_randint):
        attacker = {"AC": 9, "name": "Marti", "attacks": ["Slice", "Sword"],
                    "atk_modifier": 0, "max-HP": 20, "damage": (1, 10), "HP": 15,
                    "crit_chance": [19], "crit_modifier": 2, "dmg_modifier": 1}
        opposition = {"AC": 15, "name": "Sally", "attacks": ["Hop", "Skip"],
                      "atk_modifier": 0, "max-HP": 12, "HP": 12, "damage": (1, 10),
                      "crit_chance": [20], "crit_modifier": 0, "dmg_modifier": 0}
        expected = opposition
        combat_round(attacker, opposition)
        self.assertEqual(expected, opposition)

    @patch('random.randint', side_effect=[15, 5])
    def test_combat_round_attacker_initial_roll_equal_to_opposition_AC(self, mock_randint):
        attacker = {"AC": 8, "name": "Chris", "attacks": ["Slice", "Sword"],
                    "atk_modifier": 0, "max-HP": 20, "damage": (1, 10), "HP": 15,
                    "crit_chance": [20], "crit_modifier": 2, "dmg_modifier": 1}
        opposition = {"AC": 15, "name": "Sophie", "attacks": ["Hop", "Skip"],
                      "atk_modifier": 0, "max-HP": 16, "HP": 15, "damage": (1, 10),
                      "crit_chance": [20], "crit_modifier": 0, "dmg_modifier": 0}
        expected = opposition['HP'] - (5 + 1)
        combat_round(attacker, opposition)
        self.assertEqual(expected, opposition['HP'])

    @patch('random.randint', side_effect=[25, 2])
    def test_combat_round_attacker_initial_roll_greater_than_opposition_AC(self, mock_randint):
        attacker = {"AC": 10, "name": "Chris", "attacks": ["Slice", "Sword"],
                    "atk_modifier": 0, "max-HP": 20, "damage": (1, 10), "HP": 15,
                    "crit_chance": [20], "crit_modifier": 0, "dmg_modifier": 3}
        opposition = {"AC": 23, "name": "Sophie", "attacks": ["Hop", "Skip"],
                      "atk_modifier": 0, "max-HP": 15, "HP": 14, "damage": (1, 10),
                      "crit_chance": [20], "crit_modifier": 0, "dmg_modifier": 0}
        expected = opposition['HP'] - (2 + 3)
        combat_round(attacker, opposition)
        self.assertEqual(expected, opposition['HP'])
