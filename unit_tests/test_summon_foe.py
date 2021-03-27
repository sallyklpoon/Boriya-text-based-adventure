from unittest import TestCase
from unittest.mock import patch

from game import summon_foe


class TestSummonFoe(TestCase):

    @patch('random.randint', return_value=3)
    def test_summon_foe_character_level_1_summons_weak_foe_from_select_foe_if_roll_3(self, mock_randint):
        character = {"level": 1}
        expected = {'AC': 8,
                    'EXP': 50,
                    'HP': 10,
                    'atk_modifier': 0,
                    'attacks': ['\x1b[33mFury of Blows\x1b[0m', '\x1b[33mReckless Swing\x1b[0m'],
                    'boss': False,
                    'crit_chance': [20],
                    'crit_modifier': 2,
                    'damage': (1, 8),
                    'dmg_modifier': 0,
                    'flee': False,
                    'initiative_modifier': 3,
                    'max-HP': 10,
                    'name': '\x1b[33mBerserker\x1b[0m'}
        actual = summon_foe(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[70, 2])
    def test_summon_foe_character_level_2_summon_strong_foe2_if_roll_less_than_70_then_2(self, mock_randint):
        character = {"level": 2}
        expected = {'AC': 15,
                    'EXP': 200,
                    'atk_modifier': 3,
                    'attacks': ['\x1b[33mLife Drain\x1b[0m', '\x1b[33mCurse\x1b[0m'],
                    'boss': False,
                    'crit_chance': [20],
                    'crit_modifier': 2,
                    'damage': (2, 6),
                    'dmg_modifier': 2,
                    'flee': False,
                    'initiative_modifier': 5,
                    'HP': 16,
                    'max-HP': 16,
                    'name': '\x1b[33mShadow\x1b[0m'}
        actual = summon_foe(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[71, 1])
    def test_summon_foe_character_level_2_summon_weak_foe1_if_roll_more_than_70_then_1(self, mock_randint):
        character = {"level": 2}
        expected = {"name": "\x1b[33mFanatic\x1b[0m",
                    "AC": 10,
                    "HP": 6,
                    "max-HP": 6,
                    "attacks": ["\x1b[33mtheir Dagger\x1b[0m", "\x1b[33mPurge\x1b[0m"],
                    "atk_modifier": 3,
                    "damage": (1, 6),
                    "dmg_modifier": 1,
                    "crit_chance": [20],
                    "crit_modifier": 2,
                    "initiative_modifier": 1,
                    "EXP": 50,
                    "flee": False,
                    "boss": False}
        actual = summon_foe(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[65, 3])
    def test_summon_foe_character_level_3_epic_foe3_if_roll_less_than_70_then_3(self, mock_randint):
        character = {"level": 3}
        expected = {"name": "\x1b[33mNightwalker\x1b[0m",
                    "AC": 20,
                    "HP": 24,
                    "max-HP": 24,
                    "attacks": ["\x1b[33mAnnihilating Aura\x1b[0m",
                                "\x1b[33mTouch of Death\x1b[0m", "\x1b[33mCircle of Death\x1b[0m"],
                    "atk_modifier": 4,
                    "damage": (3, 6),
                    "dmg_modifier": 4,
                    "crit_chance": [20],
                    "crit_modifier": 2,
                    "initiative_modifier": 4,
                    "EXP": 500,
                    "flee": False,
                    "boss": False}
        actual = summon_foe(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[80, 3])
    def test_summon_foe_character_level_3_strong_foe3_if_roll_more_than_70_then_3(self, mock_randint):
        character = {"level": 3}
        expected = {"name": "\x1b[33mZealot\x1b[0m",
                    "AC": 16,
                    "HP": 12,
                    "max-HP": 12,
                    "attacks": ["\x1b[33mNecrotic Touch\x1b[0m", "\x1b[33mInflict Wounds\x1b[0m"],
                    "atk_modifier": 2,
                    "damage": (2, 8),
                    "dmg_modifier": 2,
                    "crit_chance": [20],
                    "crit_modifier": 2,
                    "initiative_modifier": 1,
                    "EXP": 200,
                    "flee": False,
                    "boss": False}
        actual = summon_foe(character)
        self.assertEqual(expected, actual)
