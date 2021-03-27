from unittest import TestCase
from unittest.mock import patch

from game import final_boss_encounter, GOD, FLEE_SUCCEED_CHANCE


class TestFinalBossEncounter(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('random.randint', side_effect=[100, 1, GOD()["AC"], GOD()["max-HP"]])
    def test_final_boss_encounter_combat_until_boss_dies_hero_wins(self, mock_randint, mock_input):
        boss = GOD()
        boss["HP"] = GOD()["max-HP"]
        hero = {"name": "Donald", "HP": 10, "max-HP": 10, "damage": (1, 20), "level": 3,
                "atk_modifier": 0, "attacks": ["Move1", "Move2"], "EXP": 80, "initiative_modifier": 1,
                "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        final_boss_encounter(character=hero, boss=boss)
        self.assertTrue(boss["HP"] <= 0 < hero["HP"])   # boss dead, hero alive

    @patch('builtins.input', side_effect=["1", "1"])    # User chooses to continue attack, 2 rounds
    @patch('random.randint', side_effect=[23, 30, 20, 1, GOD()["AC"], 8, 32, 40, 21, 20])
    def test_final_boss_encounter_combat_until_character_dies(self, mock_randint, mock_input):
        boss = GOD()
        boss["HP"] = GOD()["max-HP"]
        hero = {"name": "Jackson", "HP": 20, "max-HP": 20, "damage": (1, 20), "level": 1,
                "atk_modifier": 0, "attacks": ["Move1", "Move2"], "EXP": 60, "initiative_modifier": 2,
                "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        final_boss_encounter(character=hero, boss=boss)
        self.assertTrue(hero["HP"] <= 0 < boss["HP"])   # hero dead, boss alive

    @patch('builtins.input', side_effect=["1", "2"])    # User chooses to fight, then flee
    @patch('random.randint', side_effect=[23, 30, 12, 1, FLEE_SUCCEED_CHANCE(), 3])
    def test_final_boss_encounter_combat_character_chooses_to_flee(self, mock_randint, mock_input):
        boss = GOD()
        boss["HP"] = GOD()["max-HP"]
        hero = {"name": "April", "HP": 50, "max-HP": 50, "damage": (1, 50), "level": 10,
                "atk_modifier": 1, "attacks": ["Move1", "Move2"], "EXP": 1000, "initiative_modifier": 10,
                "dmg_modifier": 5, "crit_chance": [20], "AC": 19}
        final_boss_encounter(character=hero, boss=boss)
        self.assertTrue(hero["HP"] > 0 < boss["HP"])    # both hero and boss survived, but user chose to flee
