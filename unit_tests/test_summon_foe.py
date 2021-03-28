from unittest import TestCase
from unittest.mock import patch

from game import summon_foe, HARD_FOE_CHANCE,\
    WEAK_FOE_3, WEAK_FOE_1, WEAK_FOES, STRONG_FOE_2, STRONG_FOES, EPIC_FOE_3, EPIC_FOES


class TestSummonFoe(TestCase):

    @patch('random.choice', return_value=WEAK_FOE_3())
    def test_summon_foe_level_1_summons_weak_foe(self, mock_choice):
        character = {"level": 1}
        expected = {'AC': 8, 'EXP': 50, 'HP': 10, 'atk_modifier': 0,
                    'attacks': ['\x1b[33mFury of Blows\x1b[0m', '\x1b[33mReckless Swing\x1b[0m'],
                    'boss': False, 'crit_chance': [20], 'crit_modifier': 2, 'damage': (1, 8), 'dmg_modifier': 0,
                    'flee': False, 'initiative_modifier': 3, 'max-HP': 10, 'name': '\x1b[33mBerserker\x1b[0m'}
        actual = summon_foe(character)
        expected_no_format = {'AC': 8, 'EXP': 50, 'atk_modifier': 0,
                              'attacks': ['Fury of Blows', 'Reckless Swing'],
                              'boss': False, 'crit_chance': [20],
                              'crit_modifier': 2, 'damage': (1, 8), 'dmg_modifier': 0, 'flee': False,
                              'initiative_modifier': 3, 'max-HP': 10, 'name': 'Berserker'}
        self.assertEqual(expected, actual)
        self.assertIn(expected_no_format, WEAK_FOES())

    @patch('random.choice', return_value=STRONG_FOE_2())
    @patch('random.randint', side_effect=[HARD_FOE_CHANCE()])
    def test_summon_foe_level_2_summon_strong_foe_roll_in_hard_foe_chance(self, mock_randint, mock_choice):
        character = {"level": 2}
        expected = {'AC': 15, 'EXP': 200, 'atk_modifier': 3,
                    'attacks': ['\x1b[33mLife Drain\x1b[0m', '\x1b[33mCurse\x1b[0m'],
                    'boss': False, 'crit_chance': [20], 'crit_modifier': 2, 'damage': (2, 6), 'dmg_modifier': 2,
                    'flee': False, 'initiative_modifier': 5, 'HP': 16, 'max-HP': 16, 'name': '\x1b[33mShadow\x1b[0m'}
        actual = summon_foe(character)
        expected_no_format = {'AC': 15, 'EXP': 200, 'atk_modifier': 3,
                              'attacks': ['Life Drain', 'Curse'],
                              'boss': False, 'crit_chance': [20], 'crit_modifier': 2, 'damage': (2, 6),
                              'dmg_modifier': 2,
                              'flee': False, 'initiative_modifier': 5, 'max-HP': 16, 'name': 'Shadow'}
        self.assertEqual(expected, actual)
        self.assertIn(expected_no_format, STRONG_FOES())

    @patch('random.choice', return_value=WEAK_FOE_1())
    @patch('random.randint', side_effect=[HARD_FOE_CHANCE()+ 1])
    def test_summon_foe_level_2_summon_weak_foe_if_roll_beyond_hard_foe_chance(self, mock_randint, mock_choice):
        character = {"level": 2}
        expected = {"name": "\x1b[33mFanatic\x1b[0m", "AC": 10, "HP": 6,
                    "max-HP": 6, "attacks": ["\x1b[33mtheir Dagger\x1b[0m", "\x1b[33mPurge\x1b[0m"],
                    "atk_modifier": 3, "damage": (1, 6), "dmg_modifier": 1, "crit_chance": [20],
                    "crit_modifier": 2, "initiative_modifier": 1, "EXP": 50, "flee": False, "boss": False}
        actual = summon_foe(character)
        expected_no_format = {"name": "Fanatic", "AC": 10, "max-HP": 6,
                              "attacks": ["their Dagger", "Purge"],
                              "atk_modifier": 3, "damage": (1, 6), "dmg_modifier": 1, "crit_chance": [20],
                              "crit_modifier": 2, "initiative_modifier": 1, "EXP": 50, "flee": False, "boss": False}
        self.assertEqual(expected, actual)
        self.assertIn(expected_no_format, WEAK_FOES())

    @patch('random.choice', return_value=EPIC_FOE_3())
    @patch('random.randint', side_effect=[HARD_FOE_CHANCE()])
    def test_summon_foe_level_3_summons_epic_foe3_if_roll_in_hard_foe_chance(self, mock_randint, mock_choice):
        character = {"level": 3}
        expected = {"name": "\x1b[33mNightwalker\x1b[0m", "AC": 20, "HP": 24,
                    "max-HP": 24, "attacks": ["\x1b[33mAnnihilating Aura\x1b[0m",
                                              "\x1b[33mTouch of Death\x1b[0m", "\x1b[33mCircle of Death\x1b[0m"],
                    "atk_modifier": 4, "damage": (3, 6), "dmg_modifier": 4, "crit_chance": [20],
                    "crit_modifier": 2, "initiative_modifier": 4, "EXP": 500, "flee": False, "boss": False}
        actual = summon_foe(character)
        expected_no_format = {"name": "Nightwalker", "AC": 20, "max-HP": 24,
                              "attacks": ["Annihilating Aura", "Touch of Death", "Circle of Death"],
                              "atk_modifier": 4, "damage": (3, 6), "dmg_modifier": 4, "crit_chance": [20],
                              "crit_modifier": 2, "initiative_modifier": 4, "EXP": 500, "flee": False, "boss": False}
        self.assertEqual(expected, actual)
        self.assertIn(expected_no_format, EPIC_FOES())
