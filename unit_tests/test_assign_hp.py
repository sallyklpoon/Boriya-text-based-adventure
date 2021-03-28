from unittest import TestCase

from game import assign_hp


class TestAssignHp(TestCase):

    def test_assign_hp_creates_hp_key(self):
        character = {"max-HP": 20}
        assign_hp(character)
        self.assertIn("HP", character.keys())

    def test_assign_hp_creates_hp_same_value_as_max_hp(self):
        character = {"max-HP": 20}
        expected = character["max-HP"]
        assign_hp(character)
        actual = character["HP"]
        self.assertEqual(expected, actual)

    def test_assign_hp_dictionary_with_existing_HP_key_updates_HP(self):
        character = {"HP": 5, "max-HP": 20}
        expected = character["max-HP"]
        assign_hp(character)
        actual = character["HP"]
        self.assertEqual(expected, actual)

    def test_assign_hp_dictionary_other_keys(self):
        character = {"something": "something", "max-HP": 20, "number": 5, "stuff": ["thing", "thing"]}
        expected = character["max-HP"]
        assign_hp(character)
        actual = character["HP"]
        self.assertEqual(expected, actual)
