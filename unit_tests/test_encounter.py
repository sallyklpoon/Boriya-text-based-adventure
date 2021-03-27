from unittest import TestCase
from unittest.mock import patch

from game import encounter, FOE_FLEE_CHANCE, FLEE_CHANCE


class TestEncounter(TestCase):

    @patch('builtins.input', side_effect=["1", "2"])  # User chooses to engage, then flee
    @patch('random.randint', side_effect=[86, 62, 15, 2, 17, FOE_FLEE_CHANCE()+1, FLEE_CHANCE(), 2])
    def test_encounter_runs_full_combat_round_character_no_EXP_gain_HP_modified(self, mock_randint, mock_input):
        character = {"name": "Nao", "HP": 10, "max-HP": 10, "damage": (1, 10), "level": 1,
                     "atk_modifier": 0, "attacks": ["Stab"], "EXP": 0, "initiative_modifier": 0,
                     "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        foe = {"name": "Rex", "HP": 15, "max-HP": 15, "damage": (1, 4), "AC": 14,
               "atk_modifier": 0, "attacks": ["Kick"], "EXP": 100, "initiative_modifier": 0,
               "dmg_modifier": 2, "crit_chance": [19], "flee": False, "boss": False}
        board = {"max-x": 5, "max-y": 5}
        expected_character = {"name": "Nao", "HP": 8, "max-HP": 10, "damage": (1, 10), "level": 1,
                              "atk_modifier": 0, "attacks": ["Stab"], "EXP": 0, "initiative_modifier": 0,
                              "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        expected_foe = {"name": "Rex", "HP": 8, "max-HP": 15, "damage": (1, 4), "AC": 14,
                        "atk_modifier": 0, "attacks": ["Kick"], "EXP": 100, "initiative_modifier": 0,
                        "dmg_modifier": 2, "crit_chance": [19], "flee": False, "boss": False}
        encounter(character, foe, board)
        self.assertEqual(expected_character, character)
        self.assertEqual(expected_foe, foe)

    @patch('builtins.input', side_effect=["1"])  # User chooses to engage
    @patch('random.randint', side_effect=[12, 9, 11, 10, 17])   # User rolls damage killing foe
    def test_encounter_runs_and_modifies_EXP_gain_when_foe_killed(self, mock_randint, mock_input):
        character = {"name": "Sally", "HP": 10, "max-HP": 10, "damage": (1, 10), "level": 1,
                     "atk_modifier": 0, "attacks": ["Stab"], "EXP": 0, "initiative_modifier": 0,
                     "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        foe = {"name": "Goldie", "HP": 12, "max-HP": 12, "damage": (1, 5), "AC": 10,
               "atk_modifier": 0, "attacks": ["Cut"], "EXP": 100, "initiative_modifier": 0,
               "dmg_modifier": 2, "crit_chance": [19], "flee": False, "boss": False}
        board = {"max-x": 5, "max-y": 5}
        expected_character_exp = 100
        expected_foe_hp = -3
        encounter(character, foe, board)
        self.assertEqual(expected_character_exp, character["EXP"])
        self.assertEqual(expected_foe_hp, foe["HP"])
