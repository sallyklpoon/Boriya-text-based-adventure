import io
from unittest import TestCase
from unittest.mock import patch

from game import choose_class, CLASS_INFO


class TestChooseClass(TestCase):

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_choose_class_prints_class_information_and_options(self, mock_output, mock_side_effect):
        expected_output = "\n\033[1mWhat kind of adventurer are you?\033[0m\n\n" + CLASS_INFO() + "\n" +\
            "\n[1] Illusionist\n[2] Rogue\n[3] Ranger\n[4] Paladin\n"
        choose_class()
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("builtins.input", side_effect=["1"])
    def test_choose_class_returns_dict_containing_required_keys_class_option_1(self, mock_chosen_class):
        required_keys = ["class", "level_name", "AC", "HP", "max-HP",
                         "hit_dice", "attacks", "atk_modifier", "damage",
                         "dmg_modifier", "crit_chance", "crit_modifier"]
        actual = choose_class()
        for element in required_keys:
            self.assertIn(element, actual.keys())

    @patch("builtins.input", side_effect=["apple", "!", "2"])
    def test_choose_class_returns_dict_containing_required_keys_class_option_2(self, mock_chosen_class):
        required_keys = ["class", "level_name", "AC", "HP", "max-HP",
                         "hit_dice", "attacks", "atk_modifier", "damage",
                         "dmg_modifier", "crit_chance", "crit_modifier"]
        actual = choose_class()
        for element in required_keys:
            self.assertIn(element, actual.keys())

    @patch("builtins.input", side_effect=["not valid input", " ", "3"])
    def test_choose_class_returns_dict_containing_required_keys_class_option_3(self, mock_chosen_class):
        required_keys = ["class", "level_name", "AC", "HP", "max-HP",
                         "hit_dice", "attacks", "atk_modifier", "damage",
                         "dmg_modifier", "crit_chance", "crit_modifier"]
        actual = choose_class()
        for element in required_keys:
            self.assertIn(element, actual.keys())

    @patch("builtins.input", side_effect=["2 ", "4"])
    def test_choose_class_returns_dict_containing_required_keys_class_option_4(self, mock_chosen_class):
        required_keys = ["class", "level_name", "AC", "HP", "max-HP",
                         "hit_dice", "attacks", "atk_modifier", "damage",
                         "dmg_modifier", "crit_chance", "crit_modifier"]
        actual = choose_class()
        for element in required_keys:
            self.assertIn(element, actual.keys())

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_class_value_is_string(self, mock_chosen_class):
        expected_instance = str
        actual = choose_class()
        self.assertIsInstance(actual["class"], expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_level_name_is_string(self, mock_chosen_class):
        expected_instance = str
        actual = choose_class()
        self.assertIsInstance(actual["level_name"], expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_AC_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["AC"], expected_instance)

    @patch("builtins.input", side_effect=["3"])
    def test_choose_class_dict_HP_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["HP"], expected_instance)

    @patch("builtins.input", side_effect=["2"])
    def test_choose_class_dict_max_HP_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["max-HP"], expected_instance)

    @patch("builtins.input", side_effect=["1"])
    def test_choose_class_hit_dice_is_tuple(self, mock_chosen_class):
        expected_instance = tuple
        actual = choose_class()
        self.assertIsInstance(actual["hit_dice"], expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_hit_dice_tuple_contains_integers(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        for element in actual["hit_dice"]:
            self.assertIsInstance(element, expected_instance)

    @patch("builtins.input", side_effect=["3"])
    def test_choose_class_dict_hit_dice_tuple_is_length_2(self, mock_chosen_class):
        expected_length = 2
        actual = choose_class()
        self.assertEqual(len(actual["hit_dice"]), expected_length)

    @patch("builtins.input", side_effect=["2"])
    def test_choose_class_dict_attacks_is_list(self, mock_chosen_class):
        expected_instance = list
        actual = choose_class()
        self.assertIsInstance(actual["attacks"], expected_instance)

    @patch("builtins.input", side_effect=["1"])
    def test_choose_class_dict_attacks_is_list_contains_strings(self, mock_chosen_class):
        expected_instance = str
        actual = choose_class()
        for element in actual["attacks"]:
            self.assertIsInstance(element, expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_atk_modifier_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["atk_modifier"], expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_damage_dice_is_tuple(self, mock_chosen_class):
        expected_instance = tuple
        actual = choose_class()
        self.assertIsInstance(actual["damage"], expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_damage_dice_tuple_contains_integers(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        for element in actual["damage"]:
            self.assertIsInstance(element, expected_instance)

    @patch("builtins.input", side_effect=["2"])
    def test_choose_class_dict_damage_dice_tuple_is_length_2(self, mock_chosen_class):
        expected_length = 2
        actual = choose_class()
        self.assertEqual(len(actual["damage"]), expected_length)

    @patch("builtins.input", side_effect=["3"])
    def test_choose_class_dict_dmg_modifier_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["dmg_modifier"], expected_instance)

    @patch("builtins.input", side_effect=["1"])
    def test_choose_class_dict_crit_chance_is_list(self, mock_chosen_class):
        expected_instance = list
        actual = choose_class()
        self.assertIsInstance(actual["crit_chance"], expected_instance)

    @patch("builtins.input", side_effect=["2"])
    def test_choose_class_dict_crit_chance_list_contains_integers(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        for element in actual["crit_chance"]:
            self.assertIsInstance(element, expected_instance)

    @patch("builtins.input", side_effect=["4"])
    def test_choose_class_dict_crit_modifier_is_integer(self, mock_chosen_class):
        expected_instance = int
        actual = choose_class()
        self.assertIsInstance(actual["crit_modifier"], expected_instance)