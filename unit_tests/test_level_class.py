from unittest import TestCase

from game import level_class, \
    ILLUSIONIST_LEVELS, ILLUSIONIST_STATS_LVL2, RANGER_LEVELS, RANGER_STATS_LVL3, \
    hero_colour


class TestLevelClass(TestCase):

    def test_level_class_chooses_correct_level_2_stats_from_class_lvl(self):
        sample_hero = {"level": 2}
        expected = {"level": 2}
        expected.update(ILLUSIONIST_STATS_LVL2())
        expected["attacks"] = list(map(hero_colour, expected["attacks"]))
        level_class(sample_hero, ILLUSIONIST_LEVELS())
        self.assertEqual(expected, sample_hero)

    def test_level_class_chooses_correct_level_3_stats_from_a_class_lvl(self):
        sample_hero = {"level": 3}
        expected = {"level": 3}
        expected.update(RANGER_STATS_LVL3())
        expected["attacks"] = list(map(hero_colour, expected["attacks"]))
        level_class(sample_hero, RANGER_LEVELS())
        self.assertEqual(expected, sample_hero)
