from unittest import TestCase
from unittest.mock import patch

from game import goal_attained, GOAL_LOCATION, GOD, FLEE_CHANCE


class TestGoalAttained(TestCase):

    def test_goal_attained_False_if_character_wrong_location(self):
        character = {"x-location": GOAL_LOCATION()[0] - 2, "y-location": GOAL_LOCATION()[1] + 1}
        self.assertFalse(goal_attained(character))

    @patch("builtins.input", return_value="1")     # User chooses to engage
    @patch("random.randint", side_effect=[100, 10, GOD()["AC"], GOD()["max-HP"]])
    def test_goal_attained_True_if_at_goal_location_and_boss_defeated(self, mock_randint, mock_input):
        character = {"name": "Merlin", "HP": 43,
                     "max-HP": 43, "damage": (1, 20),
                     "level": 3, "atk_modifier": 0,
                     "attacks": ["Magic!", "Huzzah"], "EXP": 0,
                     "initiative_modifier": 0, "dmg_modifier": 5,
                     "crit_chance": [20], "AC": 19,
                     "x-location": GOAL_LOCATION()[0], "y-location": GOAL_LOCATION()[1]}
        self.assertTrue(goal_attained(character))

    @patch("builtins.input", return_value="1")     # User chooses to engage
    @patch("random.randint", side_effect=[2, 100, 33, 45])
    def test_goal_attained_False_if_at_goal_location_boss_kills_character(self, mock_randint, mock_input):
        character = {"name": "Monty", "HP": 43,
                     "max-HP": 43, "damage": (1, 20),
                     "level": 3, "atk_modifier": 0,
                     "attacks": ["Slashing", "Ice"], "EXP": 100,
                     "initiative_modifier": 0, "dmg_modifier": 5,
                     "crit_chance": [20], "AC": 20,
                     "x-location": GOAL_LOCATION()[0], "y-location": GOAL_LOCATION()[1]}
        self.assertFalse(goal_attained(character))

    @patch("builtins.input", return_value="2")     # User chooses to flee / does not engage boss
    @patch("random.randint", return_value=FLEE_CHANCE() + 1)
    def test_goal_attained_False_if_at_goal_location_character_flee(self, mock_randint, mock_input):
        character = {"name": "Pepe", "HP": 32,
                     "max-HP": 35, "damage": (1, 10),
                     "level": 2, "atk_modifier": 2,
                     "attacks": ["Frog Jump", "Okay"], "EXP": 200,
                     "initiative_modifier": 1, "dmg_modifier": 5,
                     "crit_chance": [20], "AC": 30,
                     "x-location": GOAL_LOCATION()[0], "y-location": GOAL_LOCATION()[1]}
        self.assertFalse(goal_attained(character))
