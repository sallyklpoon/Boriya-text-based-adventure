from unittest import TestCase
from unittest.mock import patch

from game import check_for_foe, ENCOUNTER_CHANCE


class TestCheckForFoe(TestCase):

    @patch('builtins.input', side_effect=["1"])   # Engage in Combat
    @patch('random.randint', side_effect=[ENCOUNTER_CHANCE(), 1, 100, 1, 15, 10])
    # Side_effects: EncounterChance, Select foe, char initiative, foe initiative, atk roll, damage
    def test_check_for_foe_roll_within_encounter_chance_character_engages_in_combat(self, mock_randint, mock_input):
        character = {"name": "Zola", "HP": 10, "max-HP": 10, "damage": (1, 10), "level": 1,
                     "atk_modifier": 0, "attacks": ["Jump"], "EXP": 0, "initiative_modifier": 0,
                     "dmg_modifier": 5, "crit_chance": [20]}
        board = {"x-location": 5, "y-location": 6}
        expected = {"name": "Zola", "HP": 10, "max-HP": 10, "damage": (1, 10), "level": 1,
                    "atk_modifier": 0, "attacks": ["Jump"], "EXP": 50, "initiative_modifier": 0,
                    "dmg_modifier": 5, "crit_chance": [20]}
        check_for_foe(character, False, board)
        self.assertEqual(expected, character)

    @patch('random.randint', side_effect=[ENCOUNTER_CHANCE()+1, 3])
    def test_check_for_foe_heals_if_not_achieved_goal_and_roll_above_encounter_chance(self, mock_randint):
        character = {"name": "Rocket", "HP": 2, "max-HP": 10, "hit_dice": (1, 6)}
        achieved_goal = False
        board = {"x-location": 5, "y-location": 6}
        expected = {"name": "Rocket", "HP": 5, "max-HP": 10, "hit_dice": (1, 6)}
        check_for_foe(character, achieved_goal, board)
        self.assertEqual(expected, character)

    @patch('random.randint', side_effect=[5])
    def test_check_for_foe_heals_if_achieved_goal(self, mock_randint):
        character = {"name": "BMO", "HP": 15, "max-HP": 20, "hit_dice": (1, 6)}
        achieved_goal = True
        board = {"x-location": 5, "y-location": 6}
        expected = {"name": "BMO", "HP": 20, "max-HP": 20, "hit_dice": (1, 6)}
        check_for_foe(character, achieved_goal, board)
        self.assertEqual(expected, character)
