"""
Your name: Marti Gatchev & Sally Poon
Your student number: A01232177

This module includes code to run the game, 'Avocado Toast'.

"""
import doctest
import pprint

import random
import itertools
import time
from string import ascii_letters, punctuation, whitespace


# ======================================================================================================================
#                                                     CONSTANTS
# ======================================================================================================================

# ===== MAP CONSTANTS ==================================================================================================


def MAX_MAP_X_LVL1() -> int:
    """Return maximum map x-dimension at level 1.

    :return: the dimension as an integer"""
    return 10


def MAX_MAP_Y_LVL1() -> int:
    """Return maximum map y-dimension at level 1.

    :return: the dimension as an integer"""
    return 10


def MAX_MAP_X_LVL2() -> int:
    """Return maximum map x-dimension at level 2.

    :return: the dimension as an integer"""
    return 17


def MAX_MAP_Y_LVL2() -> int:
    """Return maximum map y-dimension at level 2.

    :return: the dimension as an integer"""
    return 17


def MAX_MAP_X_LVL3() -> int:
    """Return maximum map x-dimension at level 3.

    :return: the dimension as an integer"""
    return 25


def MAX_MAP_Y_LVL3() -> int:
    """Return maximum map y-dimension at level 3.

    :return: the dimension as an integer"""
    return 25


def MAP_SCRIPTS() -> tuple:
    """Return a tuple of map scripts.

    :return: a tuple of map scripts"""
    map_scripts = \
        ("You sense a horrid presence around you, but you see nothing with your eyes.",
         "A fresh corpse lays in front of you, as the sound of giggling fills the air.",
         "Walking through a shroud of darkness, you smell a deep and stagnant stench.",
         "Ancient trees stand before you like castles, their magnanimity giving you the strength to continue.",
         "All around you sway disoriented shadows, each one whispering, 'Death will offer you no peace'.",
         "Searching through the sky you see no sign on light, only a velvety pool of darkness.",
         "A bed of feathery moss lays before you, offering you a moment of peace in this abyss.",
         "An inescapable power calls out to you, beckoning you to give in to it's influence. "
         "How much longer before you give in?",
         "Nothing stirs, nothing shines, and nothing sings. "
         "You only hear a hollow echoing, like the hushed tones of a great, slabbed cathedral.",
         "Coils of vaporous void writhe around you like a smoke from a fire, stealing the warmth from your body.",
         "A small pond appears before you, it's shore gurgling as water meets stone; "
         "a swish, a clunk, a swell and a clop.",
         "A pair of black dogs eye you as you make your way through the forest. Will they ever leave you?")
    return map_scripts


def MAP_FILLERS() -> tuple:
    """Return a tuple of map fillers for print_map.

    :return: tuple"""
    return " ,✾◞", " ⁕. ", " ◟'〟", " ⋄ ☨", " ⚘⚘ ", " `⁂ ", " ✼. ", "♮`, ", " ~'.", "〟❈ "


# ===== START GAME CONSTANTS ===========================================================================================

def START_X() -> int:
    """Return character's starting x-location = 0.

    :return: START_X location as an integer"""
    return 0


def START_Y() -> int:
    """Return character's starting y-location = 0.

    :return: START_Y location as an integer"""
    return 0


def HERO_START_EXP() -> int:
    """Return character's starting EXP as an integer.

    :return: an integer"""
    return 0


def HERO_START_LEVEL() -> int:
    """Return the character's starting level = 1.

    :return: an integer, representing the starting level of a character as defined above"""
    return 1


def GOAL_LOCATION() -> tuple:
    """Return goal coordinates = (24, 24)

    :return: GOAL() coordinates as a tuple (x, y)"""
    return 24, 24


def START_GAME_MSG() -> str:
    """Return the message to start the game.

    :return: a string, the start game message"""
    return "༺═─────────────────────────────────────────────────────────────────────────────────────────═༻\n" \
           "\n" \
           "\n" \
           "                                   /_  _,_ ,_   .      __, \n" \
           "                                 _/_)_(_/_/ (__/__(_/_(_/(_\n" \
           "                                                  _/_      \n" \
           "                                                 (/        \n" \
           "\n" \
           "༺═─────────────────────────────────────────────────────────────────────────────────────────═༻\n" \
           "\n" \
           "Many, many years ago, the Forest of Bóriya was home to an order of druids known as the Prirod. \n" \
           "Protectors of the forest and worshippers of the night, the Prirod watched over the land with \n" \
           "the help of the nearby town of Cakopone. Their efforts ensured that the people and the land \n" \
           "could both prosper, and for many years the peace was upheld.\n" \
           "\n" \
           "However, a century ago, the Prirod vanished completely, and with their disappearance a blight \n" \
           "spread across Bóriya. As the years passed, the darkness and plague expanded further and further  \n" \
           "until nearly the entire kingdom was effected. In response to the expanding blight, a new religion \n" \
           "appeared who's followers worshipped the void that had taken over Bóriya, their cult members flocking \n" \
           "in droves back to the blight's source. None ever returned. \n" \
           "\n" \
           "As a child, you lost your family to the blight, and swore to end it's dominion over the land. Over \n" \
           "the years, you gathered rumours and searched for wisdom in order to end the land's suffering. A \n" \
           "powerful being named Erebus is said to be the creator of this blight; a being so powerful, some \n" \
           "consider a god. If one were to kill Erebus, perhaps the land would feel peace once more... \n" \
           "\n" \
           "༺═─────────────────────────────────────────────────────────────────────────────────────────═༻\n"


def PROLOGUE() -> str:
    """Return the prologue of the game.

    :return: a string, the prologue of the game"""
    return "\n༺═─────────────────────────────────────────────────────────────────────────────────────────═༻\n" \
           "\n" \
           "Your journey has finally brought you back to the source of it all. As you look forward, the \n" \
           "void that has taken over the Forest of Bóriya stares you right in the eyes. Will this be the end? \n" \
           "\n" \
           "You must grow more powerful, for the void that lays ahead of you will tear apart weak souls. It would \n" \
           "be wise to approach carefully, for the closer you get to the heart of the abyss, the stronger your \n" \
           "enemies will become. You must reach the great temple where the old Prirod druids used to worship the  \n" \
           "night, for it is there that Erebus spreads his deep darkness.\n" \
           "\n༺═─────────────────────────────────────────────────────────────────────────────────────────═༻\n"


def CLASS_INFO() -> str:
    """Return class information string, formatted with class information.

    :return: a string, class information to be printed to user"""
    return "\033[1m<< ILLUSIONIST >>\033[0m The Illusionist is a magic user that is a master of deception,\n" \
           "light, and shadows. Utilizing spells of great power, they create figments and phantasms to deceive, \n" \
           "influence, and trick their foes in mind-altering ways. This class has a very weak early game, \n" \
           "but a god-like late game.\n" \
           "STATS: \033[32mArmour Class (AC): 14\033[0m  | " \
           "\033[34m Maximum HP: 10\033[0m  | " \
           "\033[36m Damage Die: (1, 8) \033[0m\n"\
           "\n" \
           "\033[1m<< ROGUE >>\033[0m The Rogue is a versatile character, capable of sneaky combat and nimble \n" \
           "tricks. Utilizing their stealth and dexterity, Rogues sacrifice brute strength for a nimble dodging \n" \
           "ability, and a consistent output of damage. This class has a neutral early and late game.\n"\
           "STATS: " \
           "\033[32mArmour Class (AC): 16\033[0m  | " \
           "\033[34m Maximum HP: 10\033[0m  | " \
           "\033[36m Damage Die: (2, 4) \033[0m\n" \
           "\n" \
           "\033[1m<< RANGER >>\033[0m The Ranger is a hunter and woodsman who lives by not only their sword, \n" \
           "but also their wits. Utilizing an assortment of weapons, poisons, and magic, Rangers relentlessly \n" \
           "chase down their prey in order to secure a kill. This class has a strong early game, and a \n" \
           "weak late game.\n" \
           "STATS: " \
           "\033[32mArmour Class (AC): 16\033[0m  | " \
           "\033[34m Maximum HP: 12\033[0m  | " \
           "\033[36m Damage Die: (1, 12) \033[0m\n" \
           "\n" \
           "\033[1m<< PALADIN >>\033[0m The Paladin swears to uphold justice and righteousness above all else. \n" \
           "They are proficient with heavy arms and armor, while also using divine powers to augment their combat \n" \
           "capabilities. This class has a weak early game, and a strong late game.\n" \
           "STATS: " \
           "\033[32mArmour Class (AC): 15\033[0m  | " \
           "\033[34m Maximum HP: 12\033[0m  | " \
           "\033[36m Damage Die: (1, 8) \033[0m\n" \


# ===== MENU CONSTANTS =================================================================================================


def MOVE_OPTIONS() -> tuple:
    """Return tuple of move options as a list of string directions.

    :return: tuple of direction options"""
    return "go North", "go South", "go West", "go East", "Quit Game"


def ENGAGE_OPTIONS() -> tuple:
    """Return engage options as a tuple of strings.

    :return: tuple of engagement options"""
    return "Attack", "Flee"


def CLASS_OPTIONS() -> tuple:
    """Return class options as a tuple of strings.

    :return: tuple of class options """
    return "Illusionist", "Rogue", "Ranger", "Paladin"

# ===== LEVEL-UP CONSTANTS =============================================================================================


def LVL2_EXP_OUTSET() -> int:
    """Return the EXP threshold for Level 2 level up.

    :return: an integer"""
    return 200


def LVL3_EXP_OUTSET() -> int:
    """Return the minimum EXP for Level 3 level up.

    :return: an integer"""
    return 1000


# ===== CLASS CONSTANTS ================================================================================================
# ----- ILLUSIONIST ----------------------------------------------------------------------------------------------------

def ILLUSIONIST_STATS_LVL1() -> dict:
    """Return Illusionist class level 1 stats.

    :return: a dictionary of Illusionist level 1 stats"""
    return {"class": "Illusionist", "level_name": "Trickster",
            "AC": 14, "HP": 10, "max-HP": 10, "hit_dice": (1, 4),
            "attacks": ["Colour Spray", "Phantasmal Force", "Shadow Blade"],
            "atk_modifier": 2, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2, "initiative_modifier": 1}


def ILLUSIONIST_STATS_LVL2() -> dict:
    """Return Illusionist class level 2 stats.

    :return: a dictionary of Illusionist level 2 stats"""
    return {"level_name": "Mesmer", "AC": 15,  "max-HP": 18, "hit_dice": (1, 6),
            "attacks": ["Hypnotic Pattern", "Shatter", "Mind Spike"],
            "atk_modifier": 4, "damage": (2, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 1}


def ILLUSIONIST_STATS_LVL3() -> dict:
    """Return Illusionist class level 3 stats.

    :return: a dictionary of Illusionist level 3 stats"""
    return {"level_name": "Creator", "AC": 22,  "max-HP": 48, "hit_dice": (1, 8),
            "attacks": ["Psychic Scream", "Mental Prison", "Ravenous Void"],
            "atk_modifier": 12, "damage": (2, 16), "dmg_modifier": 12,
            "crit_chance": [19, 20], "crit_modifier": 4, "initiative_modifier": 2}


def ILLUSIONIST_LEVELS() -> tuple:
    """Return a tuple of Illusionist level-up starting from lvl 2.

    :return: tuple"""
    return ILLUSIONIST_STATS_LVL2(), ILLUSIONIST_STATS_LVL3()


# ----- ROGUE ----------------------------------------------------------------------------------------------------------

def ROGUE_STATS_LVL1() -> dict:
    """Return Rogue class level 1 stats.

    :return: a dictionary of Rogue level 1 stats"""
    return {"class": "Rogue", "level_name": "Cutpurse",
            "AC": 16, "max-HP": 10, "hit_dice": (1, 6),
            "attacks": ["Sneak Attack", "their Dagger", "their Hand-Crossbow"],
            "atk_modifier": 4, "damage": (2, 4), "dmg_modifier": 4,
            "crit_chance": [19, 20], "crit_modifier": 2, "initiative_modifier": 3}


def ROGUE_STATS_LVL2() -> dict:
    """Return Rogue class level 2 stats.

    :return: a dictionary of Rogue level 2 stats"""
    return {"level_name": "Assassin", "AC": 18, "max-HP": 20, "hit_dice": (1, 6),
            "attacks": ["a cheap-shot", "their Double Blade", "Smoke Bomb"],
            "atk_modifier": 6, "damage": (2, 8), "dmg_modifier": 6, "crit_chance": [19, 20],
            "crit_modifier": 2, "initiative_modifier": 4}


def ROGUE_STATS_LVL3() -> dict:
    """Return Rogue class level 3 stats.

    :return: a dictionary of Rogue level 3 stats"""
    return {"level_name": "Shadow Master", "AC": 20,  "max-HP": 48, "hit_dice": (1, 8),
            "attacks": ["Soul Blade", "Fan of Blades", "Culling"],
            "atk_modifier": 8, "damage": (3, 10), "dmg_modifier": 8, "crit_chance": [19, 20],
            "crit_modifier": 2, "initiative_modifier": 6}


def ROGUE_LEVELS() -> tuple:
    """Return a tuple of Rogue level-up starting from lvl 2.

    :return: tuple"""
    return ROGUE_STATS_LVL2(), ROGUE_STATS_LVL3()


# ----- RANGER ---------------------------------------------------------------------------------------------------------

def RANGER_STATS_LVL1() -> dict:
    """Return Ranger class level 1 stats.

    :return: a dictionary of Ranger level 1 stats"""
    return {"class": "Ranger", "level_name": "Scout",
            "AC": 16, "max-HP": 12, "hit_dice": (1, 8),
            "attacks": ["Ensnaring Strike", "Hail of Thorns", "Thorn Whip"],
            "atk_modifier": 6, "damage": (1, 12), "dmg_modifier": 4,
            "crit_chance": [20], "crit_modifier": 2, "initiative_modifier": 2}


def RANGER_STATS_LVL2() -> dict:
    """Return Ranger class level 2 stats.

    :return: a dictionary of Ranger level 2 stats"""
    return {"level_name": "Pathfinder", "AC": 18, "max-HP": 24, "hit_dice": (1, 8),
            "attacks": ["Flame Arrows", "Conjure Barrage", "Grasping Vine"],
            "atk_modifier": 6, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 3}


def RANGER_STATS_LVL3() -> dict:
    """Return Ranger class level 3 stats.

    :return: a dictionary of Ranger level 3 stats"""
    return {"level_name": "Far Wanderer", "AC": 20, "max-HP": 54, "hit_dice": (1, 10),
            "attacks": ["Steel Wind Strike", "Swift Quiver", "Wrath of Nature"],
            "atk_modifier": 8, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 4}


def RANGER_LEVELS() -> tuple:
    """Return a tuple of Ranger level-up starting from lvl 2.

    :return: tuple"""
    return RANGER_STATS_LVL2(), RANGER_STATS_LVL3()


# ----- PALADIN --------------------------------------------------------------------------------------------------------

def PALADIN_STATS_LVL1() -> dict:
    """Return Paladin class level 1 stats.

    :return: a dictionary of Paladin level 1 stats"""
    return {"class": "Paladin", "level_name": "Protector",
            "AC": 15, "max-HP": 12, "hit_dice": (1, 4),
            "attacks": ["Branding Smite", "Thunderous Smite", "Shield Bash"],
            "atk_modifier": 3, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2, "initiative_modifier": 1}


def PALADIN_STATS_LVL2() -> dict:
    """Return Paladin class level 2 stats.

    :return: a dictionary of Paladin level 2 stats"""
    return {"level_name": "Guardian", "AC": 18, "max-HP": 24, "hit_dice": (1, 6),
            "attacks": ["Divine Word", "Forbiddance", "Staggering Smite"],
            "atk_modifier": 6, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2, "initiative_modifier": 2}


def PALADIN_STATS_LVL3() -> dict:
    """Return Paladin class level 3 stats.

    :return: a dictionary of Paladin level 3 stats"""
    return {"level_name": "Justiciar", "AC": 22, "max-HP": 62, "hit_dice": (1, 10),
            "attacks": ["Sunburst", "Divine Smite", "Banishing Smite"],
            "atk_modifier": 10, "damage": (3, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 3, "initiative_modifier": 3}


def PALADIN_LEVELS() -> tuple:
    """Return a tuple of Paladin level-up starting from lvl 2.

    :return: tuple"""
    return PALADIN_STATS_LVL2(), PALADIN_STATS_LVL3()


# ===== FOE CONSTANTS ==================================================================================================

def GOD() -> dict:
    return {"name": foe_colour("Erebus"),
            "AC": 16,
            "max-HP": 100,
            "attacks": list(map(foe_colour, ["Time Ravage", "Imprisonment", "Power Word: Kill", "Tear Soul"])),
            "atk_modifier": 6,
            "damage": (3, 6),
            "dmg_modifier": 4,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 4,
            "EXP": 500,
            "flee": False,
            "boss": True}


def WEAK_FOE_1() -> dict:
    """Return the statistics of a weak foe.

    :return: a dictionary"""
    return {"name": "Fanatic",
            "AC": 10,
            "max-HP": 6,
            "attacks": ["their Dagger", "Purge"],
            "atk_modifier": 3,
            "damage": (1, 6),
            "dmg_modifier": 1,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 1,
            "EXP": 50,
            "flee": False,
            "boss": False}


def WEAK_FOE_2() -> dict:
    """Return the statistics of a weak foe.

    :return: a dictionary"""
    return {"name": "Cultist",
            "AC": 12,
            "max-HP": 8,
            "attacks": ["Necrotic Touch", "Decompose"],
            "atk_modifier": 2,
            "damage": (1, 4),
            "dmg_modifier": 2,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 0,
            "EXP": 50,
            "flee": False,
            "boss": False}


def WEAK_FOE_3() -> dict:
    """Return the statistics of a weak foe.

    :return: a dictionary"""
    return {"name": "Berserker",
            "AC": 8,
            "max-HP": 10,
            "attacks": ["Fury of Blows", "Reckless Swing"],
            "atk_modifier": 0,
            "damage": (1, 8),
            "dmg_modifier": 0,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 3,
            "EXP": 50,
            "flee": False,
            "boss": False}


def WEAK_FOES() -> tuple:
    """Return collection of weak foes.

    :return: tuple of weak foes"""
    return WEAK_FOE_1(), WEAK_FOE_2(), WEAK_FOE_3()


# <<----------- strong foes ---------------------------->>

def STRONG_FOE_1() -> dict:
    """Return the statistics of a strong foe.

    :return: a dictionary"""
    return {"name": "Wraith",
            "AC": 14,
            "max-HP": 18,
            "attacks": ["Ray of Sickness", "Ray of Enfeeblement"],
            "atk_modifier": 2,
            "damage": (2, 4),
            "dmg_modifier": 4,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 2,
            "EXP": 200,
            "flee": False,
            "boss": False}


def STRONG_FOE_2() -> dict:
    """Return the statistics of a strong foe.

    :return: a dictionary"""
    return {"name": "Shadow",
            "AC": 15,
            "max-HP": 16,
            "attacks": ["Life Drain", "Curse"],
            "atk_modifier": 3,
            "damage": (2, 6),
            "dmg_modifier": 2,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 5,
            "EXP": 200,
            "flee": False,
            "boss": False}


def STRONG_FOE_3() -> dict:
    """Return the statistics of a strong foe.

    :return: a dictionary"""
    return {"name": "Zealot",
            "AC": 16,
            "max-HP": 12,
            "attacks": ["Necrotic Touch", "Inflict Wounds"],
            "atk_modifier": 2,
            "damage": (2, 8),
            "dmg_modifier": 2,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 1,
            "EXP": 200,
            "flee": False,
            "boss": False}


def STRONG_FOES() -> tuple:
    """Return collection of strong foes.

    :return: tuple of strong foes"""
    return STRONG_FOE_1(), STRONG_FOE_2(), STRONG_FOE_3()


# <<----------- epic foes ---------------------------->>

def EPIC_FOE_1() -> dict:
    """Return the statistics of a epic foe.

    :return: a dictionary"""
    return {"name": foe_colour("Death Knight"),
            "AC": 16,
            "max-HP": 18,
            "attacks": list(map(foe_colour, ["Vampiric Touch", "Chilling Smite", "Eye-bite"])),
            "atk_modifier": 6,
            "damage": (2, 4),
            "dmg_modifier": 4,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 2,
            "EXP": 500,
            "flee": False,
            "boss": False}


def EPIC_FOE_2() -> dict:
    """Return the statistics of a epic foe.

    :return: a dictionary"""
    return {"name": "Devourer",
            "AC": 18,
            "max-HP": 20,
            "attacks": ["Devour", "Blight", "Enervation"],
            "atk_modifier": 8,
            "damage": (2, 6),
            "dmg_modifier": 2,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 1,
            "EXP": 500,
            "flee": False,
            "boss": False}


def EPIC_FOE_3() -> dict:
    """Return the statistics of a epic foe.

    :return: a dictionary"""
    return {"name": "Nightwalker",
            "AC": 20,
            "max-HP": 24,
            "attacks": ["Annihilating Aura", "Touch of Death", "Circle of Death"],
            "atk_modifier": 4,
            "damage": (3, 6),
            "dmg_modifier": 4,
            "crit_chance": [20],
            "crit_modifier": 2,
            "initiative_modifier": 4,
            "EXP": 500,
            "flee": False,
            "boss": False}


def EPIC_FOES() -> tuple:
    """Return collection of epic foes.

    :return: tuple of epic foes"""
    return EPIC_FOE_1(), EPIC_FOE_2(), EPIC_FOE_3()


# ===== COMBAT CONSTANTS ===============================================================================================


def ONE_D100() -> tuple:
    """Return 1d100 as a tuple.

    :return: a tuple (rolls, number_of_sides)"""
    return 1, 100


def ENCOUNTER_CHANCE() -> int:
    """Return the percent chance that an encounter with foe will occur.

    :return: an integer """
    return 35


def HARD_FOE_CHANCE() -> int:
    """Return the percent chance that an encounter with more difficult foe will occur.

    :return: an integer """
    return 70


def FLEE_SUCCEED_CHANCE() -> int:
    """Return the percent chance that an encounter with foe will occur.

    :return: an integer """
    return 20


def FOE_FLEE_CHANCE() -> int:
    """Return the chance that an encounter with foe will occur.

    Value must be based on the the percent chance divided by 10

    :return: an integer """
    return 20


def FLEE_DAMAGE_DIE() -> tuple:
    """Return the foe damage die when a character flees as a tuple, 1d4 = (1, 4)

    :return: a foe's damage die when a character flees unsuccessfully as a tuple (rolls, number_of_sides)
    """
    return 1, 4


def FOE_CLASS_DIE() -> tuple:
    """Return the die to determine foe class, 1d3 (1, 3)

    :return: a foe class die as a tuple (rolls, number_of_sides)"""
    return 1, 3


def ATTACK_DIE() -> tuple:
    """Return the attack roll die, 1d20 = (1, 20)

    :return: the attack roll die as a tuple, (rolls, number_of_sides)
    """
    return 1, 20


# ======================================================================================================================
#                                              FUNCTIONS START HERE
# ======================================================================================================================


# ===== COMMON FUNCTIONS ===============================================================================================

def hero_colour(text: str) -> str:
    """Colour the given text in the hero colour (cyan).

    :param text: a string
    :precondition: text is a string
    :postcondition: returns the text wrapped with ASCII escape code for cyan
    :return: a string, wrapping original text in ASCII escape code for cyan

    >>> print(hero_colour('hello'))
    \033[36mhello\033[0m
    """
    return f"\033[36m{text}\033[0m"


def foe_colour(text: str) -> str:
    """Colour the given text in the foe colour (yellow).

    :param text: a string
    :precondition: text is a string
    :postcondition: returns the text wrapped with ASCII escape code for yellow
    :return: a string, wrapping original text in ASCII escape code for yellow

    >>> print(foe_colour('hello'))
    \033[33mhello\033[0m
    """
    return f"\033[33m{text}\033[0m"


def format_character(format_style: "a function", character: dict) -> None:
    """Format a character properly with the given format style.

    :param character: a dictionary
    :param format_style: a function for colour formatting
    :precondition: format_style is a defined colour styling such as hero_colour or foe_colour
    :precondition: character is a dictionary containing the keys "name" and "attacks"
    :precondition: value of "name" is a string
    :precondition: value of "attacks" is a list of strings
    :postcondition: all strings from "name" and "attacks" are formatted with the passed format_style
    :return: nothing, a character's dictionary is modified

    >>> sample_foe = {"name": "Sarah", "attacks": ["Jump", "Crawl"]}
    >>> format_character(foe_colour, sample_foe)
    >>> print(sample_foe['name'])
    \033[33mSarah\033[0m
    >>> print(sample_foe['attacks'][0])
    \033[33mJump\033[0m
    >>> print(sample_foe['attacks'][1])
    \033[33mCrawl\033[0m
    """
    character["name"] = format_style(character["name"])
    character["attacks"] = list(map(format_style, character["attacks"]))


def roll(die: tuple) -> int:
    """Roll a die with the specified number of sides the specified number of times.

    :param die: a tuple
    :precondition: the accepted die must be a tuple with two integers (rolls, sides)
    :precondition: rolls must be an int >= 1, represents the number of rolls for the die
    :precondition: sides must be an int >= 1, represents the number of sides on the die being rolled
    :postcondition: calculate the sum of the die rolled a specified number of times
    :return: the sum of rolled numbers

    No doctests, function uses random.int()
    """
    rolls, sides = die
    return random.randint(1, sides * rolls)


def get_menu(menu_type: str) -> None:
    """Print menu options for a given menu type of either "move", "engage", or "class".

    :param menu_type: a non-empty string, either "move", "engage", or "class"
    :precondition: menu_type is a string asking for the correct menu
    :precondition: menu_type argument is either the string "move", "engage", or "class"
    :postcondition: print enumerated MOVE_OPTIONS() if menu_type is "move"
    :postcondition: print enumerated ENGAGE_OPTIONS() if menu_type is "engage"
    :postcondition: print enumerated CLASS_OPTIONS() if menu_type is "class"
    :postcondition: enumerated list starts from 1
    :return: prints enumerated options as strings starting from 1

    >>> get_menu("move")
    <BLANKLINE>
    [1] go North
    [2] go South
    [3] go West
    [4] go East
    [5] Quit Game
    >>> get_menu("engage")
    <BLANKLINE>
    [1] Attack
    [2] Flee
    >>> get_menu("class")
    <BLANKLINE>
    [1] Illusionist
    [2] Rogue
    [3] Ranger
    [4] Paladin
    """
    print("")
    if menu_type == "move":
        menu = MOVE_OPTIONS()
    elif menu_type == "engage":
        menu = ENGAGE_OPTIONS()
    else:
        menu = CLASS_OPTIONS()
    for number, option in enumerate(menu, 1):
        print(f"[{number}] {option}")


def get_user_choice(decision_type: str) -> str:
    """Return user's valid input for choice of class

    :param decision_type: a string
    :precondition: decision_type is a string that will customize the input prompt
    :postcondition: the user will be asked for their choice
    :postcondition: user's input for choice will be returned
    :return: a string, the user's input for choice of class

    No doctests, requires user input
    """
    return input(f"\n\033[1mEnter the number of your {decision_type} choice: \033[0m")


def assign_hp(creature: dict) -> None:
    """Assign the HP key for a creature.

    :param creature: a dictionary
    :precondition: creature includes the ['max-HP'] key, an integer > 0
    :postcondition: an ['HP'] key will be added to the creature's dictionary
    :postcondition: creature['HP'] == creature['max-HP']
    :return: nothing, the creature dictionary passed will have a new 'HP' key

    >>> hero = {"max-HP": 12}
    >>> assign_hp(hero)
    >>> hero
    {'max-HP': 12, 'HP': 12}
    """
    creature['HP'] = creature['max-HP']


def is_not_digit(element: str) -> bool:
    """Determine if string contains non-digits.

    :param element: a single character from a string
    :precondition: element is a single character from a string, that is, len(element) == 1
    :precondition: element is not an empty string
    :postcondition: return a Boolean if the element is a non-digit string character
    :postcondition: if element is any ASCII letter, whitespace, or punctuation, return True
    :return: Boolean

    >>> is_not_digit("1")
    False
    >>> is_not_digit("A")
    True
    >>> is_not_digit("z")
    True
    >>> is_not_digit("&")
    True
    >>> is_not_digit(" ")
    True
    """
    if element in ascii_letters or element in punctuation or element in whitespace:
        return True
    else:
        return False


def get_valid_input(decision_type: str, menu_type: tuple) -> str:
    """Return a input from user that is valid.

    An invalid answer is when user inputs nothing or inputs something other than a number or their
    input is not within the given options of a menu given to them.

    :param decision_type: a string
    :param menu_type: a tuple
    :precondition: decision_type is any string
    :precondition: menu_type is a tuple of choices for a given menu, this may be selected from one of the
                   menu options defined as constants such as CLASS_OPTIONS(), ENGAGE_OPTIONS(), or MOVE_OPTIONS()
    :postcondition: return the user's choice only if it is a valid choice
    :postcondition: a user's choice is only valid if it is not empty, does not contain non-digit characters
                    and is an integer within the range of the menu_type tuple length
    :return: a string, a valid user input given the menu_type

    No doctests, get_user_choice() uses input function
    """
    user_choice = get_user_choice(decision_type)
    while user_choice == "" or list(filter(is_not_digit, user_choice)) \
            or int(user_choice) not in range(1, len(menu_type) + 1):
        print('\nChoice is invalid, adventurer...\nPlease input a number within the menu selection.')
        user_choice = get_user_choice(decision_type)
    return user_choice


# ===== START GAME =====================================================================================================


def lvl_board_max(level: int) -> tuple:
    """Return the game board dimensions for the appropriate level.

    Board will expand at each level as a part of level-up experience.

    :param level: an integer of the player's level
    :precondition: level is an integer [1, 3] representing the player's current level
    :precondition: level is an integer >= CHARACTER_START_LEVEL() constant
    :postcondition: return the accurate board dimensions for a given level
    :postcondition: return is a tuple that contains MAX_MAP_X_LVL#, MAX_MAP_X_LVL# where # is
                    an integer, representing the level number
    :return: a tuple of the current level's board dimensions

    >>> lvl_board_max(HERO_START_LEVEL())
    (10, 10)
    >>> lvl_board_max(2)
    (17, 17)
    >>> lvl_board_max(3)
    (25, 25)
    """
    if level == 1:
        return MAX_MAP_X_LVL1(), MAX_MAP_Y_LVL1()
    elif level == 2:
        return MAX_MAP_X_LVL2(), MAX_MAP_Y_LVL2()
    else:
        return MAX_MAP_X_LVL3(), MAX_MAP_Y_LVL3()


def make_board(level: int) -> dict:
    """Create a dictionary to represent a board with given map_dimensions.

    For key:value pairs in the dictionary, coordinates will be keys and descriptions will be values.

    :param level: an integer
    :precondition: level is an integer >= CHARACTER_START_LEVEL()
    :postcondition: returns a dictionary data structure of the game's board at the character's current level
    :postcondition: the keys in the dictionary are coordinates represented in tuples (x, y)
    :postcondition: the value of tuple coordinate keys are strings of location descriptions
    :postcondition: the returned dictionary will include two keys 'max-x' and 'max-y' which have values of
                    the maximum x-coordinate and maximum y-coordinate of the board as integers, respectively
    :return: a dictionary of the game board

    >>> sample_board = make_board(1)
    >>> type(sample_board)
    <class 'dict'>
    >>> pp = pprint.PrettyPrinter()
    >>> pp.pprint(sample_board)
    {'max-x': 10,
     'max-y': 10,
     (0, 0): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (0, 1): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (0, 2): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (0, 3): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (0, 4): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (0, 5): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (0, 6): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (0, 7): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (0, 8): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (0, 9): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (1, 0): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (1, 1): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (1, 2): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (1, 3): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (1, 4): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (1, 5): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (1, 6): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (1, 7): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (1, 8): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (1, 9): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (2, 0): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (2, 1): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (2, 2): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (2, 3): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (2, 4): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (2, 5): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (2, 6): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (2, 7): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (2, 8): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (2, 9): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (3, 0): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (3, 1): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (3, 2): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (3, 3): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (3, 4): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (3, 5): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (3, 6): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (3, 7): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (3, 8): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (3, 9): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (4, 0): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (4, 1): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (4, 2): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (4, 3): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (4, 4): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (4, 5): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (4, 6): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (4, 7): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (4, 8): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (4, 9): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (5, 0): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (5, 1): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (5, 2): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (5, 3): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (5, 4): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (5, 5): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (5, 6): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (5, 7): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (5, 8): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (5, 9): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (6, 0): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (6, 1): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (6, 2): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (6, 3): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (6, 4): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (6, 5): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (6, 6): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (6, 7): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (6, 8): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (6, 9): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (7, 0): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (7, 1): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (7, 2): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (7, 3): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (7, 4): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (7, 5): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (7, 6): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (7, 7): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (7, 8): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (7, 9): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (8, 0): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (8, 1): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (8, 2): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (8, 3): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (8, 4): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (8, 5): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (8, 6): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (8, 7): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.',
     (8, 8): "All around you sway disoriented shadows, each one whispering, 'Death "
             "will offer you no peace'.",
     (8, 9): 'Searching through the sky you see no sign on light, only a velvety '
             'pool of darkness.',
     (9, 0): 'A bed of feathery moss lays before you, offering you a moment of '
             'peace in this abyss.',
     (9, 1): 'An inescapable power calls out to you, beckoning you to give in to '
             "it's influence. How much longer before you give in?",
     (9, 2): 'Nothing stirs, nothing shines, and nothing sings. You only hear a '
             'hollow echoing, like the hushed tones of a great, slabbed cathedral.',
     (9, 3): 'Coils of vaporous void writhe around you like a smoke from a fire, '
             'stealing the warmth from your body.',
     (9, 4): "A small pond appears before you, it's shore gurgling as water meets "
             'stone; a swish, a clunk, a swell and a clop.',
     (9, 5): 'A pair of black dogs eye you as you make your way through the '
             'forest. Will they ever leave you?',
     (9, 6): 'You sense a horrid presence around you, but you see nothing with '
             'your eyes.',
     (9, 7): 'A fresh corpse lays in front of you, as the sound of giggling fills '
             'the air.',
     (9, 8): 'Walking through a shroud of darkness, you smell a deep and stagnant '
             'stench.',
     (9, 9): 'Ancient trees stand before you like castles, their magnanimity '
             'giving you the strength to continue.'}
    """
    map_script = itertools.cycle(MAP_SCRIPTS())
    lvl_max_x, lvl_max_y = lvl_board_max(level)
    board = {(x_location, y_location): next(map_script)
             for x_location in range(lvl_max_x)
             for y_location in range(lvl_max_y)}
    board['max-x'], board['max-y'] = lvl_max_x, lvl_max_y
    return board


def print_map(character: dict, board: dict) -> None:
    """Print a map of where the character is located on a board.

    :param character: a dictionary of character stats
    :param board: a dictionary of the board
    :precondition: board is a dictionary that contains a 'max-x' and 'max-y' key
    :precondition: the board values of the 'max-x' and 'max-y' key are integers that are >= 1, representing the
                   maximum x and y value of the board (i.e. the dimensions)
    :precondition: character is a dictionary of stats with keys, "x-location" and "y-location"
    :precondition: the values of "x-location" and "y-location" are both integers that are >= 0
                   and less than the board['max-x'] and board['max-y'] values, respectively
    :postcondition: print out a visual map with the correct location as to where the character is on a board
    :return: printed map

    No doctest, print_map uses random module
    """
    print("")
    for row in range(board['max-y']):
        for column in range(board['max-x']):
            if (column, row) == (character["x-location"], character["y-location"]):
                print(f"({hero_colour('웃')})", end="")
            elif (column, row) == GOAL_LOCATION():
                print("\033[31m( ☩ )\033[0m", end="")
            else:
                print(random.choice(MAP_FILLERS()), end="")
        print("")


def choose_class() -> dict:
    """Return the character class statistics selected by the user.

    Class choices include Illusionist, Rogue, Ranger, and Paladin.

    :postcondition: available class options will be printed to user
    :postcondition: return the accurate class statistics as a dictionary based on user's input
    :postcondition: return dictionary contains the keys "class", "level_name", "AC", "HP", "max-HP", "hit_dice",
                    "attacks", "atk_modifier", "damage", "dmg_modifier", "crit_chance", "crit_modifier"
    :postcondition: value of "class" key with string value
    :postcondition: value of "level_name" with string value
    :postcondition: value of "AC" key with with integer value for Armour Class
    :postcondition: value of "HP" key with with integer value for current HP
    :postcondition: value of "max-HP" key with with integer value for character's maximum HP
    :postcondition: value of "hit_dice" key with with tuple value two integers for hit dice
    :postcondition: value of "attacks" key with with list value of attacks
    :postcondition: value of "atk_modifier" key with with integer value for attack modifier
    :postcondition: value of "damage" key with with tuple value of two integers for damage dice
    :postcondition: value of "dmg_modifier" key with with integer for damage modifier
    :postcondition: value of "crit_chance" key with with list value of critical roll chances
    :postcondition: value of "crit_modifier" key with with integer value for critical roll modifier
    :return: a dictionary of a chosen class' statistics

    No doctest, get_valid_input calls upon another helper function that requires input
    """
    print("\n\033[1mWhat kind of adventurer are you?\033[0m\n\n" + CLASS_INFO())
    get_menu("class")
    chosen_class = get_valid_input('class', CLASS_OPTIONS())
    if chosen_class == "1":
        return ILLUSIONIST_STATS_LVL1()
    elif chosen_class == "2":
        return ROGUE_STATS_LVL1()
    elif chosen_class == "3":
        return RANGER_STATS_LVL1()
    elif chosen_class == "4":
        return PALADIN_STATS_LVL1()


def get_name() -> str:
    """Return user's input for their character name.

    :postcondition: return the user's input name as a string
    :return: string of character name

    No doctest, input required
    """
    return input("\033[1mWhat's your name? \033[0m")


def make_character() -> dict:
    """Create a hero dictionary with hero details.

    :postcondition: returns a complete hero dictionary
    :postcondition: hero dictionary contains keys "name", "x-location", "y-location", "EXP", "level", "quit",
                    "class", "level_name", "AC", "HP", "max-HP", "hit_dice", "attacks", "atk_modifier", "damage",
                    "dmg_modifier", "crit_chance", "crit_modifier"
    :postcondition: value of "name" is a string input by the user
    :postcondition: value of "x-location" is an integer, determined by START_X()
    :postcondition: value of "y-location" is an integer, determined by START_Y()
    :postcondition: value of "EXP" is 0
    :postcondition: value of "level" is integer, determined by CHARACTER_START_LEVEL()
    :postcondition: value of "quit" is False
    :postcondition: value of "AC" is an integer, the hero's armour class
    :postcondition: value of "HP" is an integer > 0
    :postcondition: value of "max-HP" is an integer > 0
    :postcondition: value of "damage" is a tuple, the damage die
    :postcondition: value of "attacks" is a list, determined by hero's chosen
    :postcondition: value of "class" key with string value
    :postcondition: value of "level_name" with string value
    :postcondition: value of "AC" key with with integer value for Armour Class
    :postcondition: value of "HP" key with with integer value for current HP
    :postcondition: value of "max-HP" key with with integer value for hero's maximum HP
    :postcondition: value of "hit_dice" key with with tuple value two integers for hit dice
    :postcondition: value of "attacks" key with with list value of attacks
    :postcondition: value of "atk_modifier" key with with integer value for attack modifier
    :postcondition: value of "damage" key with with tuple value of two integers for damage dice
    :postcondition: value of "dmg_modifier" key with with integer for damage modifier
    :postcondition: value of "crit_chance" key with with list value of critical roll chances
    :postcondition: value of "crit_modifier" key with with integer value for critical roll modifier
    :postcondition: value of "initiative_modifier" is an integer
    :return: a complete hero dictionary

    No doctests, input is required
    """
    hero = {"name": hero_colour(get_name()),
            "x-location": START_X(),
            "y-location": START_Y(),
            "EXP": HERO_START_EXP(),
            "level": HERO_START_LEVEL(),
            "quit": False}
    hero.update(choose_class())
    hero["attacks"] = list(map(hero_colour, hero['attacks']))
    assign_hp(hero)
    return hero


def start_game() -> tuple:
    """Start up the game by returning map and character information.

    :postcondition: prints START_GAME_MSG()
    :postcondition: collects result of the map as a dictionary
    :postcondition: collects result of the character as a dictionary
    :postcondition: produces a tuple of both map and character data structures in the order (map, character)
    :return: map and character data structures as a tuple (map, character)

    No doctests. Calls make_character(), which requires user input.
    """
    print(START_GAME_MSG())
    hero = make_character()
    print(PROLOGUE())
    time.sleep(5)
    return make_board(hero['level']), hero


# ===== NEXT MOVE (VALIDATE AND MOVE) ==================================================================================


def valid_move(direction: str, x_location: int, y_location: int, board: dict) -> bool:
    """Validate the character's movement is valid (in the board).

    Return Boolean True for valid move and False for invalid move.

    :param direction: a string of an integer between [1, 4]
    :param x_location: an integer representing character's current x-location
    :param y_location: an integer representing chraracter's current y-location
    :param board: a dictionary of the board
    :precondition: direction is a string of an integer representative of moving
    :precondition: direction == '1' is moving north, or y - 1
    :precondition: direction == '2' is moving south, or y + 1
    :precondition: direction == '3' is moving west, or x - 1
    :precondition: direction == '4' is moving east, or x + 1
    :precondition: x_location and y_location are integers representing character's
                   current x and y location respectively
    :precondition: board is a non-empty dictionary containing the keys "max-x" and "max-y"
    :postcondition: accurately determine if the character's move is valid (within the board space) or invalid
                    (hits the board's limits)
    :return: Boolean True or False

    >>> sample_board = {"max-x": 5, "max-y": 5}
    >>> valid_move("1", 0, 0, sample_board)
    False
    >>> valid_move("3", 0, 0, sample_board)
    False
    >>> valid_move("2", sample_board["max-x"], sample_board["max-y"], sample_board)
    False
    >>> valid_move("4", sample_board["max-x"], sample_board["max-y"], sample_board)
    False
    >>> valid_move("1", sample_board["max-x"] // 2, sample_board["max-y"] // 2, sample_board)
    True
    """
    if direction == "1":
        y_location -= 1
    elif direction == "2":
        y_location += 1
    elif direction == "3":
        x_location -= 1
    else:
        x_location += 1
    return x_location in range(board['max-x']) and y_location in range(board['max-y'])


def move_character(direction: str, character: dict) -> None:
    """Move the character in the direction indicated.

    :param direction: a string of an integer representing where character will move
    :param character: a dictionary, the character's dictionary
    :precondition: the character dictionary contains an "x_location" and "y_location" key
    :precondition: the values of the "x_location" and "y_location" key in the character dictionary are
                   integers representing coordinates x and y of the character at the current moment
    :precondition: the direction being moved has been validated and is a valid move for the character
    :postcondition: accurately move the character by updating the character's x and y coordinates
    :precondition: direction == '1' is moving north, will change character's current y-coordinate to y - 1
    :precondition: direction == '2' is moving south, will change character's current y-coordinate to y + 1
    :precondition: direction == '3' is moving west, will change character's current x-coordinate to x - 1
    :precondition: direction == '4' is moving east, will change character's current x-coordinate to x + 1
    :return: character's "x-location" or "y-location" value modified appropriately

    >>> sample_character = {"x-location": 1, "y-location": 2}
    >>> move_character("1", sample_character)
    >>> sample_character["x-location"]
    1
    >>> sample_character["y-location"]
    1
    >>> sample_character = {"x-location": 1, "y-location": 2}
    >>> move_character("2", sample_character)
    >>> sample_character["x-location"]
    1
    >>> sample_character["y-location"]
    3
    >>> sample_character = {"x-location": 1, "y-location": 2}
    >>> move_character("3", sample_character)
    >>> sample_character["x-location"]
    0
    >>> sample_character["y-location"]
    2
    >>> sample_character = {"x-location": 1, "y-location": 2}
    >>> move_character("4", sample_character)
    >>> sample_character["x-location"]
    2
    >>> sample_character["y-location"]
    2
    """
    if direction == "1":
        character["y-location"] -= 1
    elif direction == "2":
        character["y-location"] += 1
    elif direction == "3":
        character["x-location"] -= 1
    else:
        character["x-location"] += 1


def next_move(character: dict, board: dict) -> None:
    """Move the character to a valid position on the board as requested by user.

    :param character: a dictionary, the character's dictionary
    :param board: a dictionary, the board's representation
    :precondition: the character dictionary contains a "x_location" and "y_location" key
    :precondition: the values of the "x_location" and "y_location" key in the character dictionary are
                   integers representing coordinates x and y of the character at the current moment
    :precondition: the board dictionary contains a "max-x" and "max-y" key
    :precondition: the values of "max-x" and "max-y" keys are integers >= 0
    :postcondition: character is moved to a valid spot on the board
    :postcondition: character "x_location" and "y_location" is updated

    No doctests, requires user input
    """
    move_valid = False
    print("\033[1mWhich direction would you like to go?\033[0m")
    get_menu("move")
    while not move_valid:
        direction = get_valid_input('direction', MOVE_OPTIONS())
        if direction == "5":
            move_valid, character["quit"] = True, True
        else:
            if valid_move(direction, character["x-location"], character["y-location"], board):
                move_valid = True
                move_character(direction, character)
            else:
                print("\nYou've reached the limits of the map, adventurer...")


# ===== CHECK FOR MONSTERS =============================================================================================


def heal(character: dict) -> None:
    """Heal a character if necessary, notifying them that they have been healed to new HP.

    Heal a character by modifying their current HP to CHARACTER_HEAL(),
    but without exceeding CHARACTER_MAX_HP().

    :param character: a dictionary of the character's stats
    :precondition: character is a dictionary of the character's stats
    :precondition: character dictionary contains the keys, "HP",  "hit-dice", and "max-HP"
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :precondition: the value of character["hit_dice"] is a tuple representing the hit dice that will be rolled
                   to determine the healing HP amount
    :precondition: the value of character["max-HP"] is an integer, the maximum character may have
    :postcondition: accurately modify the current character's 'HP' to a quantity specified by rolling the character's
                    hit dice without exceeding the maximum HP
    :return: character["HP"] healed by CHARACTER_HEAL() amount and printed statement of character healing,
             no actual value returned

    No doctests, roll() uses random module
    """
    if character["HP"] == character["max-HP"]:
        print("")
    else:
        heal_points = roll(character["hit_dice"])
        if character["HP"] + heal_points <= character["max-HP"]:
            character["HP"] += heal_points
        else:
            character["HP"] = character["max-HP"]
        print("\n\033[32m✣ As you venture through the darkness, you take a moment to rest your weary soul. ✣\n"
              f"✣ Your health has been healed to {character['HP']} points. ✣\n\033[0m")
    time.sleep(0.5)


def summon_foe(character: dict) -> dict:
    """Summon a random foe.

    :postcondition: a random foe is summoned based on character's level
    :postcondition: the return is a dictionary of foe's stats
    :postcondition: foe is randomly selected from specific level selection of foes
    :postcondition: characters at level 1 will be summoned a weak foe from WEAK_FOES()
    :postcondition: characters at level 2 may summon a foe from STRONG_FOES() or WEAK_FOES()
    :postcondition: characters at level 3 may summon a foe from STRONG_FOES() or EPIC_FOES()
    :return: a dictionary containing summoned foe's stats

    No doctests, random used
    """
    foe = {}
    if character["level"] == 1:
        foe = select_foe(WEAK_FOES())
    if character["level"] == 2:
        foe = select_foe(STRONG_FOES()) if roll(ONE_D100()) <= HARD_FOE_CHANCE() else select_foe(WEAK_FOES())
    if character["level"] == 3:
        foe = select_foe(EPIC_FOES()) if roll(ONE_D100()) <= HARD_FOE_CHANCE() else select_foe(STRONG_FOES())
    format_character(foe)
    assign_hp(foe)
    return foe


def select_foe(foe_selection: tuple) -> dict:
    """Return a foe from a certain selection of foes by chance.

    :param foe_selection: a tuple
    :precondition: foe_selection is a tuple containing dictionaries of possible foes to select from by chance
    :postcondition: the return dictionary includes keys-- "name", "AC", "attacks", "atk_modifier", "HP", "max-HP",
                    "damage", "dmg_modifier", "crit_chance", "crit_modifier", "initiative_modifier", "EXP", "flee"
    :postcondition: value of "name" is a string
    :postcondition: value of "AC" is an integer, the character's armour class
    :postcondition: value of "HP" is an integer > 0
    :postcondition: value of "max-HP" is an integer > 0
    :postcondition: value of "attacks" key with with list value of attacks
    :postcondition: value of "atk_modifier" key with with integer value for attack modifier
    :postcondition: value of "damage" key with with tuple value of two integers for damage dice
    :postcondition: value of "dmg_modifier" key with with integer for damage modifier
    :postcondition: value of "crit_chance" key with with list value of critical roll chances
    :postcondition: value of "crit_modifier" key with with integer value for critical roll modifier
    :postcondition: value of "initiative_modifier" is an integer
    :postcondition: value of "EXP" is an integer > 0, he EXP points that can be gained by defeating foe
    :postcondition: value of "flee" is False, indicator if foe has decided to flee
    :return: a dictionary of foe statistics

    No doctests, roll() helper uses random.randint
    """
    random_class = roll(FOE_CLASS_DIE())
    summoned = {}
    if random_class == 1:
        summoned = foe_selection[0]
    elif random_class == 2:
        summoned = foe_selection[1]
    elif random_class == 3:
        summoned = foe_selection[2]
    return summoned


def check_for_foe(character: dict, game_end: bool, board: dict) -> None:
    """Check if character meets a foe or heals.

    Character will either encounter a foe or, if they do not encounter a foe,
    heal HP at CHARACTER_HEAL() amount. If character has reached their goal, they will not encounter a foe

    :param character: a dictionary of the character's stats
    :param game_end: a Boolean of whether or not goal was achieved
    :param board: a dictionary representing the game board
    :precondition: character is a dictionary of character's stats
    :precondition: character dictionary contains keys "name", "HP", "damage", "attacks", "x-location", "y-location"
                   "atk_modifier", "dmg_modifier", "EXP", "initiative_modifier", "crit_chance", and "hit_dice"
    :precondition: value of "name" is a string input by the user in make_character() function
    :precondition: value of "HP" is an integer > 0
    :precondition: value of "damage" and "hit_dice" is a tuple
    :precondition: value of "attacks" is a list of strings
    :precondition: value of "crit_chance" is a list of integers
    :precondition: value of "x-location" and "y-location" is an integer >= 0
    :precondition: value of "atk-modifier", "dmg_modifier", "EXP", and "initiative modifier" is an integer
    :precondition: achieved_goal is a Boolean of whether or not goal was achieved; True means goal has been achieved
    :precondition: param board contains the keys "max-x" and "max-y" with integer values >= 0
    :postcondition: character's "HP" value will be appropriately be affected by either healing if there is no foe
                    or taking possible damage if they encounter a foe and fight to the death
    :return: character's HP modified by either damage or heal, no actual return value

    No doctest, helper roll() uses random module
    """
    if not game_end:
        if roll(ONE_D100()) <= ENCOUNTER_CHANCE():
            encounter(character, summon_foe(character), board)
        else:
            heal(character)


# ===== FOE ENCOUNTER ==================================================================================================


def engage() -> bool:
    """Ask character if they would like to engage with or flee from foe.

    :postcondition: determine, based on character's decision, if they will engage in combat or flee
    :postcondition: if user's input is 1, result of engage is True (engage)
    :postcondition: if user's input is 2, result of engage is False (flee)
    :return: Boolean value of whether or not character will engage

    No doctests, user input required
    """
    print("\n\033[1mWhat will you do next, adventurer?\033[0m")
    get_menu("engage")
    engage_choice = get_valid_input('engage', ENGAGE_OPTIONS())
    return engage_choice == "1"


def flee(character: dict, foe: dict) -> None:
    """Determine character takes damage when fleeing a normal foe.

    If successful, print message will tell character they left the encounter successfully,
    if unsuccessful, print message will show damage that character has taken.

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: character contains the key "HP"
    :precondition: foe contains the keys, 'name', 'attacks', and 'boss'
    :precondition: the value of foe['name'] is a string and the value of foe['attacks'] is a list of strings
    :precondition: the value of foe['boss'] is a boolean, determining if the foe is a boss
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :postcondition: accurately modify the current character's 'HP' if they are unsuccessful fleeing
    :postcondition: informative messages are printed to confirm if character can successfully flee or has taken damage
    :return: possible modified character["HP"]
    :return: informative printed messages of flee success

    No doctests, uses random module
    """
    if foe['boss']:
        return
    else:
        if roll(ONE_D100()) <= FLEE_SUCCEED_CHANCE():
            damage = roll(FLEE_DAMAGE_DIE())
            character["HP"] -= damage
            print(f"As you attempt to flee from the {foe['name']}, they catch up to you,\n"
                  f"using {random.choice(foe['attacks'])} to deal \033[31m{damage}\033[0m damage.\n")
            time.sleep(0.5)
            print(f"Your health is now at \033[34m{character['HP']}\033[0m points.\n")

        else:
            print(f"\nQuickly evading your foe, you leave the {foe['name']}'s view range.\n"
                  f"You've escaped violence this time.\n")
    time.sleep(0.5)


def foe_flee(foe: dict) -> None:
    """Determine if foe will flee.

    :param foe: a dictionary representing the foe stats
    :precondition: the foe dictionary is non-empty and contains a key, "flee"
    :precondition: the value of the key, "flee" is the Boolean False
    :postcondition: accurately modify the "flee" key to True if the foe flees given specific chances
    :return: nothing, foe's 'flee' key updated if they manage to flee

    No doctests, random module required
    """
    foe["flee"] = True if roll(ONE_D100()) <= FOE_FLEE_CHANCE() else False


def initiative(character, foe) -> bool:
    """Determine if character has initiative in battle.

    :param character: a dictionary representing the character stats
    :param foe: a dictionary representing the foes stats
    :precondition: foe and character dictionaries must contain initiative_modifier key
    :precondition: the value of "initiative_modifier" key is an integer
    :postcondition: determine if character has initiative first in a combat round by comparing character
                    and foe rolls for initiative
    :postcondition: returns True if character initiative roll > foe's initiative roll using ONE_D100()
    :postcondition: returns False if character initiative roll < foe's initiative roll using ONE_D100()
    :return: a Boolean of whether or not character has initiative

    No doctests, random module used
    """
    initiative_roll = {}
    draw = True
    while draw:
        initiative_roll["character"] = roll(ONE_D100()) + character["initiative_modifier"]
        initiative_roll["foe"] = roll(ONE_D100()) + foe["initiative_modifier"]
        if initiative_roll["character"] != initiative_roll["foe"]:
            draw = False
    return initiative_roll["character"] > initiative_roll["foe"]


def combat_round(attacker: dict, opposition: dict) -> None:
    """Complete one round of combat between an attacker and opposition.

    :param attacker: a dictionary of either character or foe stats
    :param opposition: a dictionary of either character or foe stats
    :precondition: both attacker and opposition dictionaries include keys-- "name", "attacks", "HP", and "damage"
                   "crit_chance", "atk_modifier", "crit_modifier", "dmg_modifier", "max-HP", "AC"
    :precondition: value of "name" is a string, the name of attacker or opposition
    :precondition: value of "attacks" is a list of string elements
    :precondition: value of "max-HP", "AC", "HP", "atk_modifier", "crit_modifier", "dmg_modifier" is an integer
    :precondition: value of "damage" is a tuple, the damage die for attacker or opposition
    :precondition: value of "crit_chance" is a list of integers
    :postcondition: amount of damage from attacker to foe is determined
    :postcondition: opposition takes damage from attacker["damage"] die, their HP will be modified to reflect the change
    :return: no value, but opposition's HP modified by damage from attacker

    No doctests, uses random module
    """
    initial_roll = roll(ATTACK_DIE())
    attack_roll = initial_roll + attacker["atk_modifier"]
    print(f"\n{attacker['name']} attacks using {random.choice(attacker['attacks'])}!")
    time.sleep(0.5)
    if attack_roll >= opposition["AC"]:
        if initial_roll in attacker["crit_chance"]:
            attack_damage = (roll(attacker["damage"]) * attacker["crit_modifier"]) + attacker["dmg_modifier"]
            print(f"It's a \033[35mcritical\033[0m hit!\n")
        else:
            attack_damage = roll(attacker["damage"]) + attacker["dmg_modifier"]
        opposition["HP"] -= attack_damage
        print(f"{opposition['name']} takes \033[31m{attack_damage}\033[0m damage.\n"
              f"{opposition['name']}'s health level is now "
              f"\033[34m{opposition['HP']}/{opposition['max-HP']}\033[0m...")
    else:
        print(f"{opposition['name']} dodges the attack successfully.")
    time.sleep(0.5)


def enter_combat(character: dict, foe: dict) -> None:
    """Battle character and foe in combat until character or foe dies (HP == 0),
    or foe flees, or user chooses to disengage.

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: both character and foe dictionaries include keys-- "name", "attacks", "HP", and "damage"
                   "crit_chance", "atk_modifier", "crit_modifier", "dmg_modifier", "max-HP", "AC", "initiative_modifier"
    :precondition: value of "name" is a string, the name of attacker or opposition
    :precondition: value of "attacks" is a list of string elements
    :precondition: value of "max-HP", "AC", "HP", "atk_modifier", "initiative_modifier", "crit_modifier",
                   "dmg_modifier" is an integer
    :precondition: value of "damage" is a tuple, the damage die for attacker or opposition
    :precondition: value of "crit_chance" is a list of integers
    :postcondition: both character and foe may take damage to their "HP" key value
    :postcondition: combat will continue until either character or foe has "HP" = 0, or if foe flees, or if
                    user chooses to disengage/flee
    :return: no value, but modified effects of key value "HP" for both character and foe after end of combat

    No doctests, called functions, combat_round() and initiative() uses random module
    """
    while not foe["flee"] and character["HP"] > 0 and foe["HP"] > 0:
        if engage():
            if initiative(character, foe):
                attacker, opposition = character, foe
            else:
                attacker, opposition = foe, character
            combat_round(attacker, opposition)
            if opposition["HP"] > 0:
                combat_round(opposition, attacker)
            if not foe["boss"] and opposition["HP"] > 0 and attacker["HP"] > 0:
                foe_flee(foe)
        else:
            return flee(character, foe)


def encounter(character: dict, foe: dict, board: dict) -> None:
    """Send character into an encounter with foe, including EXP gain.

    Encounter ends by character's choice to flee or by character and foe's fight to death
    (either character or foe's "HP" key value is 0).

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :param board: a dictionary, representing the current game map
    :precondition: both character and foe dictionaries include keys-- "name", "attacks", "HP", and "damage"
                   "crit_chance", "atk_modifier", "crit_modifier", "dmg_modifier", "max-HP", "AC",
                   "initiative_modifier", and "EXP"
    :precondition: value of "name" is a string, the name of attacker or opposition
    :precondition: value of "attacks" is a list of string elements
    :precondition: value of "max-HP", "AC", "HP", "atk_modifier", "initiative_modifier", "crit_modifier",
                   "dmg_modifier" is an integer
    :precondition: value of "damage" is a tuple, the damage die for attacker or opposition
    :precondition: value of "crit_chance" is a list of positive integers
    :precondition: value of "EXP is a positive integer >= 0
    :precondition: board contains the keys "max-x" and "max-y" with integer values >= 0
    :postcondition: character either engages in battle to the death or attempts to flee
    :postcondition: character's "HP" key value may be affected by damage from flee or by entering combat
    :postcondition: foe's "HP" key value may be affected by damage from combat
    :postcondition: character may gain "EXP" from encounter if foe chooses to flee or foe is killed
    :return: no value, but accurately modifies "HP" of character depending on fight or flee decision and random rolls

    No doctests, called enter_combat() and flee() uses random module
    """
    print(f"\nA {foe['name']} has showed up!")
    enter_combat(character, foe)
    if foe["HP"] <= 0:
        print(f"\nYou stand in triumph as you look down on the {foe['name']}'s slain body.\n"
              f"There are yet more foes to encounter, {character['name']}. Your journey must continue.\n")
        gain_exp(character, foe["EXP"], board)

    if foe["flee"]:
        print(f"\n{foe['name']} ran away.")
        gain_exp(character, foe["EXP"] // 4, board)
    time.sleep(0.5)


# ===== CHECK LEVELING UP ==============================================================================================


def gain_exp(character: dict, experience_gain: int, board: dict) -> None:
    """Increase the EXP of the character, sends character to level up levelled up if threshold achieved

    :param character: a dictionary of the character's stats
    :param experience_gain: an EXP value gained from an encounter with a foe
    :param board: a dictionary representing the current board
    :precondition: character contains the key "EXP" and "level"
    :precondition: board is a non-empty dictionary containing coordinate keys and "max-x"/"max-y" values
    :postcondition: character gains exp, leveling up if they meet a level-up threshold
    :return: nothing, character dictionary and board may be modified

    >>> sample_character = {"EXP": 0, "level": 1}
    >>> sample_board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
    >>> gain_exp(sample_character, 10, sample_board)
    \033[36mYou've earned 10 experience points. Current EXP: 10\033[0m
    >>> sample_character["EXP"]
    10
    >>> sample_character = {"EXP": 0, "level": 1}
    >>> sample_character.update(ILLUSIONIST_STATS_LVL1())
    >>> sample_board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
    >>> gain_exp(sample_character, LVL2_EXP_OUTSET(), sample_board)
    \033[36mYou've earned 200 experience points. Current EXP: 200\033[0m
    <BLANKLINE>
    \033[35mYou feel your power grow, you've levelled up. You're now able to explore new horizons!\033[0m
    You are now a \033[35mMesmer\033[0m.
    >>> sample_character["EXP"]
    200
    >>> sample_character["level"]
    2
    >>> sample_board["max-x"] == MAX_MAP_X_LVL2()
    True
    >>> sample_board["max-y"] == MAX_MAP_Y_LVL2()
    True
    """
    character["EXP"] += experience_gain
    print(hero_colour(f"You've earned {experience_gain} experience points. Current EXP: {character['EXP']}"))
    if character["EXP"] >= LVL2_EXP_OUTSET() and character['level'] == 1:
        level_up(character, board)
    if character["EXP"] >= LVL3_EXP_OUTSET() and character['level'] == 2:
        level_up(character, board)


def level_up(character: dict, board: dict) -> None:
    """Levels up the game!

    A function that levels up the game board and character

    :param character: a dictionary of character stats
    :param board: a dictionary of map stats
    :precondition: character is a dictionary of character stats containing the keys "level", "class"
    :precondition: "level" value is an integer >= 1 indicating the current level character is at
    :precondition: board is a non-empty dictionary
    :postcondition: the game is leveled up (including the character and board map)
    :return: no return value, modifies the game and character dictionaries corresponding to new character level.

    >>> sample_character = {"level": 1, "class": "Illusionist"}
    >>> sample_board = {"max-x": MAX_MAP_X_LVL1(), "max-y": MAX_MAP_Y_LVL1()}
    >>> level_up(sample_character, sample_board)
    <BLANKLINE>
    \033[35mYou feel your power grow, you've levelled up. You're now able to explore new horizons!\033[0m
    You are now a \033[35mMesmer\033[0m.
    >>> sample_character["level"]
    2
    >>> sample_character["level_name"] == ILLUSIONIST_STATS_LVL2()["level_name"]
    True
    >>> sample_character["max-HP"] == ILLUSIONIST_STATS_LVL2()["max-HP"]
    True
    >>> sample_board["max-x"] == MAX_MAP_X_LVL2()
    True
    >>> sample_board["max-y"] == MAX_MAP_Y_LVL2()
    True
    """
    character["level"] += 1
    print(f"\n\033[35mYou feel your power grow, you've levelled up. You're now able to explore new horizons!\033[0m")

    if character["class"] == "Illusionist":
        level_class(character, ILLUSIONIST_LEVELS())
    elif character["class"] == "Rogue":
        level_class(character, ROGUE_LEVELS())
    elif character["class"] == "Ranger":
        level_class(character, RANGER_LEVELS())
    elif character["class"] == "Paladin":
        level_class(character, PALADIN_LEVELS())
    board.update(make_board(character['level']))


def level_class(character: dict, class_lvl: tuple) -> None:
    """Update the character's class stats based on the class_lvl collections passed and character level.

    :param character: a dictionary of the character stats
    :param class_lvl: a tuple containing dictionaries of class level
    :precondition: the character dictionary contains the key, "level", an integer [2, 3]
    :precondition: the correct class_lvl selection is passed based on the character's class (i.e. a character
                   of the Rogue class would be passed with ROGUE_LEVELS() set of class dictionaries
    :precondition: class_lvl is a tuple of dictionaries for each class level in a specific class, in order
    :precondition: the value of the character's "class" key is either "Illusionist", "Rogue", "Ranger", "Paladin"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: no return value, character dictionary is updated

    >>> sample_hero = {"level": 2}
    >>> expected = {"level": 2}
    >>> expected.update(ILLUSIONIST_STATS_LVL2())
    >>> expected["attacks"] = list(map(hero_colour, expected["attacks"]))
    >>> level_class(sample_hero, ILLUSIONIST_LEVELS())
    You are now a \033[35mMesmer\033[0m.
    >>> expected == sample_hero
    True
    """
    level_character = {}
    if character["level"] == 2:
        level_character = class_lvl[0]
    elif character["level"] == 3:
        level_character = class_lvl[1]
    character.update(level_character)
    character['attacks'] = list(map(hero_colour, character['attacks']))
    print(f"You are now a \033[35m{character['level_name']}\033[0m.")


# ===== CHECK IF GOAL ATTAINED =========================================================================================

def goal_attained(character: dict) -> bool:
    """Check if character has completed endgame requirements to win the game

    :param character: a dictionary containing character stats
    :precondition: x_location is an integer representing character's current x-location
    :precondition: y_location is an integer representing character's current y-location
    :postcondition: accurately checks if a character's current x and y-location matches the goal location
    :postcondition: returns a Boolean True if character is at the goal location based on GOAL_LOCATION()
                    and the boss has been defeated (i.e. boss['HP'] == 0)
    :postcondition: returns a Boolean False if character is not at the goal location based on GOAL_LOCATION()
                    or if character
    :postcondition: returns a Boolean False if boss not killed, or character has fled or died
    :return: a Boolean value

    No doctests, final_boss_encounters uses random module
    """
    if (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        boss = summon_god()
        final_boss_encounter(character, boss)
        if boss["HP"] <= 0:
            return True
        else:  # boss not killed, character either flee or died
            return False
    else:
        return False


def summon_god() -> dict:
    """Summon the final boss of the game.

    :postcondition: the return is a dictionary of the boss' stats
    :postcondition: boss dictionary is properly formatted with colour_map
    :postcondition: boss dictionary is assigned proper hp values
    :return: a dictionary containing summoned foe's stats

    >>> expected = GOD()
    >>> expected["name"] = foe_colour(GOD()["name"])
    >>> expected["attacks"] = list(map(foe_colour, expected["attacks"]))
    >>> expected["HP"] = GOD()["max-HP"]
    >>> expected == summon_god()
    True
    """
    boss = GOD()
    format_character(boss)
    assign_hp(boss)
    return boss


def final_boss_encounter(character: dict, boss: dict) -> None:
    """Send character into an encounter with boss.

    Encounter ends by character's choice to flee or by character and boss' fight to the death
    (either character or boss' "HP" key value is 0).

    :param character: a dictionary containing character stats
    :param boss: a dictionary containing boss stats
    :precondition: both character and boss dictionaries include keys-- "name", "attacks", "HP", and "damage"
    :precondition: value of "name" is a string, the name of character or boss
    :precondition: value of "attacks" is a list of string elements, attack types from character or boss
    :precondition: value of "HP" is an integer, the current health points character or boss
    :precondition: value of "damage" is a tuple, the damage die for character or boss
    :precondition: board contains the keys "max-x" and "max-y" with integer values >= 0
    :postcondition: character either engages in battle to the death or attempts to flee
    :postcondition: character's "HP" key value may be affected by damage from flee or by entering combat
    :postcondition: boss' "HP" key value may be affected by damage from combat
    :postcondition: if boss has been defeated, print message to indicate end of encounter
    :return: print message that character has met boss
    :return: no value, but accurately modified "HP" of character depending on fight or flee decision and random rolls


    No doctests, called enter_combat() and flee() uses random module
    """
    print("\nYou arrive at the source of the darkness. Standing before you is an incomprehensible being made \n"
          "entirely of unending nothingness. Are you ready to die?")
    enter_combat(character=character, foe=boss)
    if boss["HP"] <= 0:
        print(f"\n{boss['name']} is dead.")
    elif character['HP'] > 0 and boss['HP'] > 0:
        flee_boss(character, boss)


def flee_boss(character: dict, boss: dict) -> None:
    """Determine if character takes damage when fleeing from boss.

    If successful, character will not take damage,
    if unsuccessful, character will take damage of rolled FLEE_DAMAGE_DIE().

    :param character: a dictionary containing character stats
    :param boss: a dictionary containing boss stats
    :precondition: character contains the key "HP"
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :postcondition: accurately modify the current character's 'HP' if they are unsuccessful fleeing
    :return: possible modified character["HP"]
    :return: informative printed messages of flee success

    No doctests, uses random module
    """
    if roll(ONE_D100()) <= FLEE_SUCCEED_CHANCE():
        damage = roll(FLEE_DAMAGE_DIE())
        character["HP"] -= damage
        print(f"As you attempt to flee from {boss['name']}, he crawls towards you\n"
              f"using {random.choice(boss['attacks'])} to deal \033[31m{damage}\033[0m damage.\n")
        time.sleep(0.5)
        print(f"Your health is now at \033[34m{character['HP']}\033[0m points.\n")

    print(f"\n{boss['name']}' blank eyes follow you as you cower away in fear."
          f"\nYou will never rid the blight from this land as long as he lives.\n"
          f"\nYou have successfully evaded violence for now, but the truth remains\n"
          f"that you must defeat this darkness at some point.")
    time.sleep(1)


# ===== END GAME =======================================================================================================


def end_game(character: dict) -> None:
    """Print appropriate end-game message depending on ending.

    :param character: a dictionary containing character stats
    :precondition: character dictionary includes keys-- "name", "HP", "x-location", and "y-location"
    :precondition: value of "HP" is an integer, representing character's current health points
    :postcondition: value of "x-location" is an integer, representing character's current x-coordinate
    :postcondition: value of "y-location" is an integer, representing character's current y-coordinate
    :postcondition: print appropriate game-over message if character's HP is 0
    :postcondition: print appropriate game-over message if character has reached GOAL_LOCATION()
    :postcondition: print appropriate quit-came message if neither of above two postconditions are true
    :return: printed end-game message

    >>> sample_character = {"name": "Suzie", "HP": 2, "x-location": 0, "y-location": 1}
    >>> end_game(sample_character)
    <BLANKLINE>
    ༺═──────────────────────────────────────────────────═༻
    The Forest of Bóriya has taken it's toll on your soul.
    You can no longer continue. Goodbye, Suzie.
    ༺═──────────────────────────────────────────────────═༻
    <BLANKLINE>
    Thank you for playing, Suzie! - Marti & Sally
    """
    if character["HP"] <= 0:
        print(f"\n༺═────────────────────────────────────────────────────────────────────────────────────────═༻\n\n"
              "Falling down to the cold ground, you feel your soul slowly being devoured by the darkness around you.\n"
              f"As you breathe your last breath, you see a sliver of moonlight appear in the sky above you, \n"
              f"but it only lasts for an instant, before being swallowed by the infinite nothingness around you.\n"
              f"\nGoodbye, {character['name']}.\n"
              f"\n༺═────────────────────────────────────────────────────────────────────────────────────────═༻\n")
    elif (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        print(f"\n༺═────────────────────────────────────────────────────────────────────────────═༻\n"
              f"\nAs you look down at Erebus' lifeless body, you see an inkling of light appear through \n"
              f"the darkened clouds above. You feel the blight slowly leave the forest, as the moonlight\n"
              f"begins to pour in through the shadows. Your journey has finally come to an end.\n"
              f"\nMay you rest easy now, {character['name']}, the Forest of Bóriya is finally rid of its\n"
              f"blight.\n"
              f"\n༺═────────────────────────────────────────────────────────────────────────────═༻\n")
    else:  # quit ending
        print(f"\n༺═──────────────────────────────────────────────────═༻\n"
              f"The Forest of Bóriya has taken it's toll on your soul.\n"
              f"You can no longer continue. Goodbye, {character['name']}.\n"
              f"༺═──────────────────────────────────────────────────═༻\n")
    print(f"Thank you for playing, {character['name']}! - Marti & Sally")


# ======================================================================================================================
#                                              MAIN GAME FUNCTION
# ======================================================================================================================


def game() -> None:
    """Run the game until user quits, character attains the goal, or character dies.

    Game will continue as long as none of the above conditions are met.

    :precondition: the game() function is called
    :precondition: user will only provide valid input when game() prompts with menu options
    :postcondition: user will be prompted appropriately with valid options to move
    :postcondition: user will be prompted with valid options to engage in or flee from combat
    :postcondition: throughout the game, user will be informed of where they are, their health
                    status, and battle progress
    :postcondition: the game will run properly without breaking until one of the following
                    post-conditions are met
    :postcondition: game ends if user decides to "quit" instead of moving their character
    :postcondition: game ends if user's character has attained the goal
    :postcondition: game ends if user's character has died (character's HP is 0)
    :postcondition: an appropriate end-game message is printed to notify character of game's end
    :return: printed statements throughout the game informing the user's decisions, actions, location,
             battle progress, and end-game message
    """
    board, hero = start_game()
    end = False
    while not end and hero["HP"] > 0:
        print_map(hero, board)
        print(f"\nYou're now at ({hero['x-location']}, {hero['y-location']}),"
              f"\033[35m Level {hero['level']}: {hero['level_name']}\033[0m, "
              f"\033[34m HP: {hero['HP']}/{hero['max-HP']}\033[0m, "
              f"\033[36m EXP: {hero['EXP']}\033[0m \n\n"
              f"{board[(hero['x-location'], hero['y-location'])]} \n")
        next_move(hero, board)
        end = True if hero["quit"] else goal_attained(hero)
        check_for_foe(hero, end, board)
    end_game(hero)


def main():
    """Execute doctest."""
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    # Run main() if module is being run as a program
    main()
