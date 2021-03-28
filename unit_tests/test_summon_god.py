from unittest import TestCase

from game import summon_god, GOD, foe_colour


class TestSummonGod(TestCase):

    def test_summon_god_returns_dict(self):
        expected = dict
        self.assertIsInstance(summon_god(), expected)

    def test_summon_god_returns_GOD_constant_dict_with_HP_and_formatted_name_attacks(self):
        expected = GOD()
        expected["name"] = foe_colour(GOD()["name"])
        expected["attacks"] = list(map(foe_colour, expected["attacks"]))
        expected["HP"] = GOD()["max-HP"]
        self.assertEqual(expected, summon_god())
