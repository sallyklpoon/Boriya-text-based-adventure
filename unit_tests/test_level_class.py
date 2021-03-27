from unittest import TestCase

from game import level_up, level_class, ILLUSIONIST_LVL_UP, ILLUSIONIST_STATS_LVL2, ILLUSIONIST_STATS_LVL3

"""Level up the character by its given class class.

    :param character: a dictionary of the character stats
    :param class_lvl: a tuple containing dictionaries of class level
    :precondition: the character dictionary is non-empty
    :precondition: the value of the character's "class" key is either "Illusionist", "Rogue", "Ranger", "Paladin"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: no return value, character dictionary is updated

    level_character = {}
    if character["level"] == 2:
        level_character = class_lvl[0]
    elif character["level"] == 3:
        level_character = class_lvl[1]
    character.update(level_character)
    character['attacks'] = list(map(hero_colour, character['attacks']))
    print(f"You are now a {character['level_name']}.")
    
    
    {"class": "Illusionist", "level_name": "Trickster",
            "AC": 14, "HP": 10, "max-HP": 10, "hit_dice": (1, 4),
            "attacks": ["Colour Spray", "Phantasmal Force", "Shadow Blade"],
            "atk_modifier": 2, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2, "initiative_modifier": 1}


{"level_name": "Mesmer", "AC": 15,  "max-HP": 18, "hit_dice": (1, 6),
            "attacks": ["Hypnotic Pattern", "Shatter", "Mind Spike"],
            "atk_modifier": 4, "damage": (2, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 1}


{"level_name": "Creator", "AC": 22,  "max-HP": 48, "hit_dice": (1, 8),
            "attacks": ["Psychic Scream", "Mental Prison", "Ravenous Void"],
            "atk_modifier": 12, "damage": (2, 16), "dmg_modifier": 12,
            "crit_chance": [19, 20], "crit_modifier": 4, "initiative_modifier": 2}
    
    expected = {"class": "Illusionist", "level_name": "Mesmer", "AC": 15,  "max-HP": 18, "hit_dice": (1, 6),
            "attacks": ["Hypnotic Pattern", "Shatter", "Mind Spike"],
            "atk_modifier": 4, "damage": (2, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 1, "level": 2}
    
    """

class TestLevelClass(TestCase):
    def test_level_class_levelone_to_leveltwo(self):

        character = {"class": "Illusionist", "level_name": "Trickster",
            "AC": 14, "HP": 10, "max-HP": 10, "hit_dice": (1, 4),
            "attacks": ["Colour Spray", "Phantasmal Force", "Shadow Blade"],
            "atk_modifier": 2, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2, "initiative_modifier": 1,
            "level": 1}

        board =

        level_up(character, board)
        level_class(character, character['level'])

        print(character)


        self.assertEqual(expected, actual)