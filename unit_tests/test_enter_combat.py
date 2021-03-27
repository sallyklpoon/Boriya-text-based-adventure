from unittest import TestCase
from unittest.mock import patch

from game import enter_combat, FLEE_SUCCEED_CHANCE, FOE_FLEE_CHANCE


class TestEnterCombat(TestCase):

    def test_enter_combat_does_not_run_if_character_HP_0(self):
        character = {"HP": 0}
        foe = {"HP": 10, "flee": False}
        expected_character, expected_foe = character, foe
        enter_combat(character, foe)
        self.assertTrue(expected_foe == foe and expected_character == character)

    def test_enter_combat_does_not_run_if_foe_HP_0(self):
        character = {"HP": 13}
        foe = {"HP": 0, "flee": False}
        expected_character, expected_foe = character, foe
        enter_combat(character, foe)
        self.assertTrue(expected_foe == foe and expected_character == character)

    def test_enter_combat_does_not_run_if_foe_flee_is_True(self):
        character = {"HP": 2}
        foe = {"flee": True, "HP": 9}
        expected_character, expected_foe = character, foe
        enter_combat(character, foe)
        self.assertTrue(expected_foe == foe and expected_character == character)

    @patch('builtins.input', return_value="2")  # User chooses to flee
    @patch('random.randint', return_value=FLEE_SUCCEED_CHANCE() + 1)
    def test_enter_combat_does_not_continue_if_user_chooses_to_flee(self, mock_randint, mock_input):
        character = {"HP": 3}
        foe = {"flee": False, "HP": 20, "boss": False, "name": "Berserker"}
        expected_character, expected_foe = character, foe
        enter_combat(character, foe)
        self.assertTrue(expected_foe == foe and expected_character == character)

    @patch('builtins.input', side_effect=["1", "2"])  # User chooses to engage, then flee
    @patch('random.randint', side_effect=[90, 76, 15, 2, 17, FOE_FLEE_CHANCE() + 1, FLEE_SUCCEED_CHANCE(), 2])
    def test_enter_combat_runs_round_of_combat_if_engage(self, mock_randint, mock_input):
        character = {"name": "Lou", "HP": 10, "max-HP": 10, "damage": (1, 10), "level": 1,
                     "atk_modifier": 0, "attacks": ["Jump"], "EXP": 0, "initiative_modifier": 0,
                     "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        foe = {"name": "Lou", "HP": 15, "max-HP": 15, "damage": (1, 4), "AC": 14,
               "atk_modifier": 0, "attacks": ["Jump"], "EXP": 100, "initiative_modifier": 0,
               "dmg_modifier": 2, "crit_chance": [19], "flee": False, "boss": False}
        expected_foe = {"name": "Lou", "HP": 8, "max-HP": 15, "damage": (1, 4), "AC": 14,
                        "atk_modifier": 0, "attacks": ["Jump"], "EXP": 100, "initiative_modifier": 0,
                        "dmg_modifier": 2, "crit_chance": [19], "flee": False, "boss": False}
        expected_character = {"name": "Lou", "HP": 8, "max-HP": 10, "damage": (1, 10), "level": 1,
                              "atk_modifier": 0, "attacks": ["Jump"], "EXP": 0, "initiative_modifier": 0,
                              "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        enter_combat(character, foe)
        self.assertTrue(expected_foe == foe and expected_character == character)
