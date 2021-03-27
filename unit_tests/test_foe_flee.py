from unittest import TestCase
from unittest.mock import patch

from game import foe_flee, FOE_FLEE_CHANCE


class TestFoeFlee(TestCase):

    @patch('random.randint', return_value=FOE_FLEE_CHANCE())
    def test_foe_flee_if_roll_within_foe_flee_chance(self, mock_randint):
        foe = {"flee": False, "name": "Some Foe"}
        foe_flee(foe)
        self.assertTrue(foe["flee"])

    @patch('random.randint', return_value=FOE_FLEE_CHANCE()+2)
    def test_foe_flee_false_if_roll_beyond_foe_flee_chance(self, mock_randint):
        foe = {"flee": False, "name": "Some Foe"}
        foe_flee(foe)
        self.assertFalse(foe["flee"])
