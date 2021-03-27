from unittest import TestCase
from unittest.mock import patch

from game import goal_attained, GOAL_LOCATION, summon_god, final_boss_encounter

"""
    :postcondition: accurately checks if a character's current x and y-location matches the goal location
    :postcondition: returns a Boolean True if character is at the goal location based on GOAL_LOCATION()
                    and the boss has been defeated (i.e. boss['HP'] == 0)
    :postcondition: returns a Boolean False if character is not at the goal location based on GOAL_LOCATION()
                    or if character
    :postcondition: returns a Boolean False if boss not killed, or character has fled or died

def goal_attained(character: dict) -> bool:

    if (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        boss = summon_god()
        final_boss_encounter(character, boss)
        if boss["HP"] <= 0:
            return True
        else:  # boss not killed, character either flee or died
            return False
    else:
        return False
"""

class TestGoalAttained(TestCase):
    def test_goal_attained_if_boss_defeated(self):
        character = {"x-location": 24

        }

    @patch('random.randint', side_effect=[38, 35, 66, 33])
    def test_initiative_only_returns_if_no_initiative_draw(self, mock_randint):
        character = {"initiative_modifier": 2}
        foe = {"initiative_modifier": 5}
        self.assertTrue(initiative(character, foe))

    def test_goal_attained_if_character_dead_or_fled(self):
        self.fail()

    def test_goal_attained_if_character_wrong_location(self):
        self.fail()
