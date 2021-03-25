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
    return 20


def MAX_MAP_Y_LVL2() -> int:
    """Return maximum map y-dimension at level 2.

    :return: the dimension as an integer"""
    return 20


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
        ("The sun is beaming and birds are chirping -- finally getting some Vitamin D!",
         "A pudgy doggo passes by and uses its sniffer to sniff you from afar, cute!",
         "Strolling through a quaint park, you see people jogging and meeting up with friends- how nice!",
         "You pass by yet another Starbucks in the neighbourhood. These are everywhere!",
         "A squirrel finds an acorn and scurries up a tree as it sees you approaching.",
         "Nothing exciting at this corner of the neighbourhood.",
         "A snake jumps out of a bush. Did you just hear it say, 'Python's the besssst...', as it slithered by?!",
         "A slight breeze picks up, you can hear the leaves in the trees rustle gently.",
         "Colourful wild flowers are growing in the patches of grass by the sidewalk.")
    return map_scripts


def START_X() -> int:
    """Return character's starting x-location = 0.

    :return: START_X location as an integer"""
    return 0


def START_Y() -> int:
    """Return character's starting y-location = 0.

    :return: START_Y location as an integer"""
    return 0


def CHARACTER_START_EXP() -> int:
    """Return character's starting EXP as an integer.

    :return: an integer"""
    return 0


def CHARACTER_START_LEVEL() -> int:
    """Return the character's starting level = 1.

    :return: an integer, representing the starting level of a character as defined above"""
    return 1


def GOAL_LOCATION() -> tuple:
    """Return goal coordinates = (25, 25)

    :return: GOAL() coordinates as a tuple (x, y)"""
    return 24, 24


def START_GAME_MSG() -> str:
    """Return the message to start the game.

    :return: a string, the start game message"""
    return "========================❋✿❀✿❋❋✿❀✿❋❋✿❀✿❋===========================\n"\
           "Your journey has brought you deep into the heartland of Vosynia as you reach the entrance of \n"\
           "the Forest of Bória.\n" \
           "You've just completed a 7-hour hackathon and you've spent the last\n"\
           "few days pent up in your room studying for midterms. It could be nice to\n"\
           "get outside and enjoy the Spring weather. Maybe hit the grocery store\n"\
           "to grab some ingredients for a soothing baking session this evening.\n"\
           "========================❋✿❀✿❋❋✿❀✿❋❋✿❀✿❋===========================\n"


def PROLOGUE() -> str:
    """Return the prologue of the game.

    :return: a string, the prologue of the game"""
    return "\n<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n" \
           "PROLOGUE SPACE." \
           "\n<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>\n"


def CLASS_INFO() -> str:
    """Return class information string, formatted with class information.

    :return: a string, class information to be printed to user"""
    return "\033[1m<< ILLUSIONIST >>\033[0m The Illusionist is a magic user that is a master of deception,\n" \
           "light, and shadows. Utilizing spells of great power, they create figments and phantasms to deceive, \n" \
           "influence, and trick their foes in mind-altering ways. This class has a very weak early game, \n" \
           "but a god-like late game.\n" \
           "STATS: \033[32mArmour Class (AC): XXX\033[0m  | " \
           "\033[34m Maximum HP: XXX\033[0m  | " \
           "\033[36m Damage Die: XXX \033[0m\n"\
           "\n" \
           "\033[1m<< ROGUE >>\033[0m The Rogue is a versatile character, capable of sneaky combat and nimble \n" \
           "tricks. Utilizing their stealth and dexterity, Rogues sacrifice brute strength for a nimble dodging \n" \
           "ability, and a consistent output of damage. This class has a neutral early and late game.\n"\
           "STATS: " \
           "\033[32mArmour Class (AC): XXX\033[0m  | " \
           "\033[34m Maximum HP: XXX\033[0m  | " \
           "\033[36m Damage Die: XXX \033[0m\n" \
           "\n" \
           "\033[1m<< RANGER >>\033[0m The Ranger is a hunter and woodsman who lives by not only their sword, \n" \
           "but also their wits. Utilizing an assortment of weapons, poisons, and magic, Rangers relentlessly \n" \
           "chase down their prey in order to secure a kill. This class has a strong early game, and a \n" \
           "weak late game.\n" \
           "STATS: " \
           "\033[32mArmour Class (AC): XXX\033[0m  | " \
           "\033[34m Maximum HP: XXX\033[0m  | " \
           "\033[36m Damage Die: XXX \033[0m\n" \
           "\n" \
           "\033[1m<< PALADIN >>\033[0m The Paladin swears to uphold justice and righteousness above all else. \n" \
           "They are proficient with heavy arms and armor, while also using divine powers to augment their combat \n" \
           "capabilities. This class has a weak early game, and a strong late game.\n" \
           "STATS: " \
           "\033[32mArmour Class (AC): XXX\033[0m  | " \
           "\033[34m Maximum HP: XXX\033[0m  | " \
           "\033[36m Damage Die: XXX \033[0m\n" \


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


# ===== CLASS CONSTANTS ================================================================================================
# ----- ILLUSIONIST ----------------------------------------------------------------------------------------------------

def ILLUSIONIST_STATS_LVL1() -> dict:
    """Return Illusionist class level 1 stats.

    :return: a dictionary of Illusionist level 1 stats"""
    return {"class": "Illusionist", "level_name": "Trickster",
            "AC": 14, "HP": 10, "max-HP": 10, "hit_dice": (1, 4),
            "attacks": ["Colour Spray", "Phantasmal Force", "Shadow Blade"],
            "atk_modifier": 2, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2}


def ILLUSIONIST_STATS_LVL2() -> dict:
    """Return Illusionist class level 2 stats.

    :return: a dictionary of Illusionist level 2 stats"""
    return {"level_name": "Mesmer", "AC": 15,  "max-HP": 18, "hit_dice": (1, 6),
            "attacks": ["Hypnotic Pattern", "Shatter", "Mind Spike"],
            "atk_modifier": 4, "damage": (2, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 2}


def ILLUSIONIST_STATS_LVL3() -> dict:
    """Return Illusionist class level 3 stats.

    :return: a dictionary of Illusionist level 3 stats"""
    return {"level_name": "Creator", "AC": 22,  "max-HP": 48, "hit_dice": (1, 8),
            "attacks": ["Psychic Scream", "Mental Prison", "Ravenous Void"],
            "atk_modifier": 12, "damage": (2, 16), "dmg_modifier": 12,
            "crit_chance": [19, 20], "crit_modifier": 4}


# ----- ROGUE ----------------------------------------------------------------------------------------------------------

def ROGUE_STATS_LVL1() -> dict:
    """Return Rogue class level 1 stats.

    :return: a dictionary of Rogue level 1 stats"""
    return {"class": "Rogue", "level_name": "Cutpurse",
            "AC": 16, "HP": 10, "max-HP": 10, "hit_dice": (1, 6),
            "attacks": ["Sneak Attack", "their Dagger", "their Hand-Crossbow"],
            "atk_modifier": 4, "damage": (2, 4), "dmg_modifier": 4,
            "crit_chance": [19, 20], "crit_modifier": 2}


def ROGUE_STATS_LVL2() -> dict:
    """Return Rogue class level 2 stats.

    :return: a dictionary of Rogue level 2 stats"""
    return {"level_name": "Assassin", "AC": 18,  "max-HP": 20, "hit_dice": (1, 6),
            "attacks": ["a cheapshot", "their Double Blade", "Smoke Bomb"],
            "atk_modifier": 6, "damage": (2, 8), "dmg_modifier": 6, "crit_chance": [19, 20],
            "crit_modifier": 2}


def ROGUE_STATS_LVL3() -> dict:
    """Return Rogue class level 3 stats.

    :return: a dictionary of Rogue level 3 stats"""
    return {"level_name": "Assassin", "AC": 18,  "max-HP": 20, "hit_dice": (1, 6),
            "attacks": ["a cheapshot", "their Double Blade", "Smoke Bomb"],
            "atk_modifier": 6, "damage": (2, 8), "dmg_modifier": 6, "crit_chance": [19, 20],
            "crit_modifier": 2}


# ----- RANGER ---------------------------------------------------------------------------------------------------------

def RANGER_STATS_LVL1() -> dict:
    """Return Ranger class level 1 stats.

    :return: a dictionary of Ranger level 1 stats"""
    return {"class": "Ranger", "level_name": "Scout",
            "AC": 16, "HP": 12, "max-HP": 12, "hit_dice": (1, 8),
            "attacks": ["Ensnaring Strike", "Hail of Thorns", "Thorn Whip"],
            "atk_modifier": 6, "damage": (1, 12), "dmg_modifier": 4,
            "crit_chance": [20], "crit_modifier": 2}


def RANGER_STATS_LVL2() -> dict:
    """Return Ranger class level 2 stats.

    :return: a dictionary of Ranger level 2 stats"""
    return {"level_name": "Pathfinder", "AC": 18,  "max-HP": 24, "hit_dice": (1, 8),
            "attacks": ["Flame Arrows", "Conjure Barrage", "Grasping Vine"],
            "atk_modifier": 6, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2}


def RANGER_STATS_LVL3() -> dict:
    """Return Ranger class level 3 stats.

    :return: a dictionary of Ranger level 3 stats"""
    return {"level_name": "Far Wanderer", "AC": 20, "max-HP": 54, "hit_dice": (1, 10),
            "attacks": ["Steel Wind Strike", "Swift Quiver", "Wrath of Nature"],
            "atk_modifier": 8, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2}


# ----- PALADIN --------------------------------------------------------------------------------------------------------

def PALADIN_STATS_LVL1() -> dict:
    """Return Paladin class level 1 stats.

    :return: a dictionary of Paladin level 1 stats"""
    return {"class": "Paladin", "level_name": "Protector",
            "AC": 15, "HP": 12, "max-HP": 12, "hit_dice": (1, 4),
            "attacks": ["Branding Smite", "Thunderous Smite", "Shield Bash"],
            "atk_modifier": 3, "damage": (1, 8), "dmg_modifier": 2,
            "crit_chance": [20], "crit_modifier": 2}


def PALADIN_STATS_LVL2() -> dict:
    """Return Paladin class level 2 stats.

    :return: a dictionary of Paladin level 2 stats"""
    return {"level_name": "Guardian", "AC": 18,  "max-HP": 24, "hit_dice": (1, 6),
            "attacks": ["Divine Word", "Forbiddance", "Staggering Smite"],
            "atk_modifier": 6, "damage": (2, 12), "dmg_modifier": 6, "crit_chance": [20],
            "crit_modifier": 2}


def PALADIN_STATS_LVL3() -> dict:
    """Return Paladin class level 3 stats.

    :return: a dictionary of Paladin level 3 stats"""
    return {"level_name": "Justiciar", "AC": 22,  "max-HP": 62, "hit_dice": (1, 10),
            "attacks": ["Sunburst", "Divine Smite", "Banishing Smite"],
            "atk_modifier": 10, "damage": (3, 10), "dmg_modifier": 10, "crit_chance": [20],
            "crit_modifier": 3}


# ===== COMBAT CONSTANTS ===============================================================================================


def INITIATIVE_DIE() -> tuple:
    """Return the initiative die, 1d100 = (1, 100)

    :return: an initiative die as a tuple (rolls, number_of_sides)
    """
    return 1, 100


def ENCOUNTER_FOE_DIE() -> tuple:
    """Return the summon foe die, 1d10 = (1, 10)

    :return: an encounter foe die as a tuple (rolls, number_of_sides)
    """
    return 1, 10


def FLEE_DAMAGE_DIE() -> tuple:
    """Return the foe damage die when a character flees as a tuple, 1d4 = (1, 4)

    :return: a foe's damage die when a character flees unsuccessfully as a tuple (rolls, number_of_sides)
    """
    return 1, 4


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
    while user_choice == "" \
            or list(filter(is_not_digit, user_choice)) \
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

    >>> lvl_board_max(CHARACTER_START_LEVEL())
    (10, 10)
    >>> lvl_board_max(2)
    (25, 20)
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

    # >>> board = make_board()
    # >>> type(board)
    # <class 'dict'>
    # >>> pp = pprint.PrettyPrinter()
    # >>> pp.pprint(board)
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

    >>> sample_character = {"x-location": 0, "y-location": 0}
    >>> sample_board = {"max-x": 3, "max-y": 3}
    >>> print_map(sample_character, sample_board)
    [\033[36m웃\033[0m][  ][  ]
    [  ][  ][  ]
    [  ][  ][  ]
    """
    for row in range(board['max-y']):
        for column in range(board['max-x']):
            print(f"[{hero_colour('웃')}]", end="") \
                if (column, row) == (character["x-location"], character["y-location"])\
                else print("[  ]", end="")
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
    """Create a character dictionary with character details

    :postcondition: returns a complete character dictionary
    :postcondition: character dictionary contains keys "name", "x-location", "y-location", "EXP", "level", "quit",
                    "class", "level_name", "AC", "HP", "max-HP", "hit_dice", "attacks", "atk_modifier", "damage",
                    "dmg_modifier", "crit_chance", "crit_modifier"
    :postcondition: value of "name" is a string input by the user
    :postcondition: value of "x-location" is an integer, determined by START_X()
    :postcondition: value of "y-location" is an integer, determined by START_Y()
    :postcondition: value of "EXP" is 0
    :postcondition: value of "level" is integer, determined by CHARACTER_START_LEVEL()
    :postcondition: value of "quit" is False
    :postcondition: value of "HP" is an integer, determined by CHARACTER_MAX_HP()
    :postcondition: value of "damage" is a tuple, determined by CHARACTER_DAMAGE_DIE()
    :postcondition: value of "attacks" is a list, determined by character's chosen
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
    :return: a complete character dictionary

    No doctests, input is required
    """
    character = {"name": hero_colour(get_name()),
                 "x-location": START_X(),
                 "y-location": START_Y(),
                 "EXP": CHARACTER_START_EXP(),
                 "level": CHARACTER_START_LEVEL(),
                 "quit": False}
    character.update(choose_class())
    character["attacks"] = list(map(hero_colour, character["attacks"]))
    return character


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
    character = make_character()
    print(f"\nWELCOME TO VOSYNIA, {character['name']}" + PROLOGUE())
    return make_board(character['level']), character


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
                    (moved off board or is not one of the precondition indicated moves)
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
    :postcondition: character is moved to a valid spot on the board
    :postcondition: character "x_location" and "y_location" is updated

    No doctests, requires user input
    """
    move_valid = False
    print("\n\033[1mWhich direction would you like to go?\033[0m")
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


# ===== CHECK IF GOAL ATTAINED =========================================================================================



def check_goal_attained(character: dict) -> bool:
    """Check if character has arrived at goal location.

    :param x_location: an integer, the character's current x-location
    :param y_location: an integer, the character's current y-location
    :precondition: x_location is an integer representing character's current x-location
    :precondition: y_location is an integer representing character's current y-location
    :postcondition: accurately checks if a character's current x and y-location matches the goal location
    :postcondition: returns a Boolean True if character is at the goal location based on GOAL_LOCATION()
    :postcondition: returns a Boolean False if character is not at the goal location based on GOAL_LOCATION()
    :return: a Boolean value

    >>> check_goal_attained(0, 0)
    False
    >>> check_goal_attained(7, 1)
    False
    >>> check_goal_attained(GOAL_LOCATION()[0], GOAL_LOCATION()[1])
    True
    """
    if (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        foe = summon_god()
        if final_boss_encounter(character, foe):
            if foe["HP"] <= 0:
                print(f"God is dead.\n")
                character["boss_defeat"] = True
                return True
            elif character["HP"] <= 0:
                print(f"You are dead.")
                return True
    else:
        return False


# ===== CHECK FOR MONSTERS =============================================================================================


def heal(character: dict) -> None:
    """Heal a character if necessary, notifying them that they have been healed to new HP.

    Heal a character by modifying their current HP to CHARACTER_HEAL(),
    but without exceeding CHARACTER_MAX_HP().

    :param character: a dictionary of the character's stats
    :precondition: character is a dictionary of the character's stats
    :precondition: character dictionary contains the key, "HP"
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :postcondition: accurately modify the current character's 'HP' to heal CHARACTER_HEAL() amount without
                    exceeding CHARACTER_MAX_HP()
    :postcondition: print a message to notify character that they have been healed to new HP
    :return: character["HP"] healed by CHARACTER_HEAL() amount and printed statement of character healing,
             no actual value returned

    >>> sample_character = {"name": "Ikki Ooli", "HP": 10, "max-HP": 10}
    >>> heal(sample_character)
    <BLANKLINE>
    Nothing happens.
    >>> sample_character["HP"]
    10
    >>> sample_character = {"name": "Norm", "HP": 18, "max-HP": 20, "attacks": ["short sword"]}
    >>> heal(sample_character)
    <BLANKLINE>
    \x1b[32m.・。.・゜ As you take a step, you suddenly feel reinvigorated by the decent day you're having.・゜・。.
    .・。.・゜Your health has been healed to 20 points. (◡‿◡✿)・゜・。.
    \x1b[0m
    >>> sample_character["HP"]
    20
    >>> sample_character = {"name": "Bob", "HP": 1, "max-HP": 10}
    >>> heal(sample_character)
    <BLANKLINE>
    \x1b[32m.・。.・゜ As you take a step, you suddenly feel reinvigorated by the decent day you're having.・゜・。.
    .・。.・゜Your health has been healed to 5 points. (◡‿◡✿)・゜・。.
    \x1b[0m
    >>> sample_character["HP"]
    5
    """
    threshold = character["max-HP"] - character["hit_dice"][1]
    if character["HP"] == character["max-HP"]:
        print("\nNothing happens.")
    else:
        if character["HP"] < threshold:
            character["HP"] += roll(character["hit_dice"])
        else:
            character["HP"] = character["max-HP"]
        print("\n\033[32m.・。.・゜ As you take a step, you suddenly feel "
              "reinvigorated by the decent day you're having.・゜・。.\n"
              f".・。.・゜Your health has been healed to {character['HP']} points. (◡‿◡✿)・゜・。.\n\033[0m")
    time.sleep(0.5)


def summon_foe(character: dict) -> dict:
    """Summon a random foe.

    :postcondition: a random foe is summoned
    :postcondition: the return is a dictionary of foe's stats
    :postcondition: foe is randomly selected from FOE_LIBRARY()
    :postcondition: the dictionary includes keys-- "name", "attacks", "HP", and "damage"
    :postcondition: value of "name" is a string, determined by randomly selected from the FOE_LIBRARY()
    :postcondition: value of "attacks" is a list, determined by the randomly selected foe from FOE_LIBRARY()
    :postcondition: value of "HP" is an integer, determined by FOE_MAX_HP()
    :postcondition: value of "damage" is a tuple, determined by FOE_DAMAGE_DIE()
    :return: a dictionary containing summoned foe's stats

    No doctests, random used
    """
    foe_chance = random.randint(1, 10)

    if character["level"] == 1:
        return summon_weak_foe()
    if character["level"] == 2:
        if foe_chance > 3:
            return summon_strong_foe()
        else:
            return summon_weak_foe()
    if character["level"] == 3:
        if foe_chance > 3:
            return summon_epic_foe()
        else:
            return summon_strong_foe()


def summon_weak_foe() -> dict:
    random_class = str(random.randint(1, 3))
    list(map(foe_colour, ["attacks"]))

    if random_class == "1":
        return {"name": foe_colour("Fanatic"),
                "AC": 10,
                "HP": 6,
                "max-HP": 6,
                "attacks": list(map(foe_colour, ["their Dagger", "Purge"])),
                "atk_modifier": 3,
                "damage": (1, 6),
                "dmg_modifier": 1,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 50,
                "flee": False}
    elif random_class == "2":
        return {"name": foe_colour("Cultist"),
                "AC": 12,
                "HP": 8,
                "max-HP": 8,
                "attacks": list(map(foe_colour, ["Necrotic Touch", "Decompose"])),
                "atk_modifier": 2,
                "damage": (1, 4),
                "dmg_modifier": 2,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 50,
                "flee": False}
    elif random_class == "3":
        return {"name": foe_colour("Berserker"),
                "AC": 8,
                "HP": 10,
                "max-HP": 10,
                "attacks": list(map(foe_colour, ["Fury of Blows", "Reckless Swing"])),
                "atk_modifier": 0,
                "damage": (1, 8),
                "dmg_modifier": 0,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 50,
                "flee": False}


def summon_strong_foe():
    random_class = str(random.randint(1, 3))
    if random_class == "1":
        return {"name": foe_colour("Wraith"),
                "AC": 14,
                "HP": 18,
                "max-HP": 18,
                "attacks": list(map(foe_colour, ["Ray of Sickness", "Ray of Enfeeblement"])),
                "atk_modifier": 2,
                "damage": (2, 4),
                "dmg_modifier": 4,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 200,
                "flee": False}
    elif random_class == "2":
        return {"name": foe_colour("Shadow"),
                "AC": 15,
                "HP": 16,
                "max-HP": 16,
                "attacks": list(map(foe_colour, ["Life Drain", "Curse"])),
                "atk_modifier": 3,
                "damage": (2, 6),
                "dmg_modifier": 2,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 200,
                "flee": False}
    elif random_class == "3":
        return {"name": foe_colour("Zealot"),
                "AC": 16,
                "HP": 12,
                "max-HP": 12,
                "attacks": list(map(foe_colour, ["Necrotic Touch", "Inflict Wounds"])),
                "atk_modifier": 2,
                "damage": (2, 8),
                "dmg_modifier": 2,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 200,
                "flee": False}


def summon_epic_foe():
    random_class = str(random.randint(1, 3))
    if random_class == "1":
        return {"name": foe_colour("Death Knight"),
                "AC": 16,
                "HP": 18,
                "max-HP": 18,
                "attacks": list(map(foe_colour, ["Vampiric Touch", "Chilling Smite", "Eyebite"])),
                "atk_modifier": 6,
                "damage": (2, 4),
                "dmg_modifier": 4,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 500,
                "flee": False}
    elif random_class == "2":
        return {"name": foe_colour("Devourer"),
                "AC": 18,
                "HP": 20,
                "max-HP": 20,
                "attacks": list(map(foe_colour, ["Devour", "Blight", "Enervation"])),
                "atk_modifier": 8,
                "damage": (2, 6),
                "dmg_modifier": 2,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 500,
                "flee": False}
    elif random_class == "3":
        return {"name": foe_colour("Nightwalker"),
                "AC": 20,
                "HP": 24,
                "max-HP": 24,
                "attacks": list(map(foe_colour, ["Annihilating Aura", "Touch of Death", "Circle of Death"])),
                "atk_modifier": 4,
                "damage": (3, 6),
                "dmg_modifier": 4,
                "crit_chance": [20],
                "crit_modifier": 2,
                "EXP": 500,
                "flee": False}


def summon_god():
    return {"name": foe_colour("Erebus"),
            "AC": 16,
            "HP": 100,
            "max-HP": 100,
            "attacks": list(map(foe_colour, ["Time Ravage", "Imprisonment", "Power Word: Kill", "Tear Soul"])),
            "atk_modifier": 6,
            "damage": (3, 6),
            "dmg_modifier": 4,
            "crit_chance": [20],
            "crit_modifier": 2,
            "EXP": 500,
            "flee": False}


def check_for_foe(character: dict, achieved_goal: bool, board: dict) -> None:
    """Check if character meets a foe or heals.

    Character will either encounter a foe or, if they do not encounter a foe,
    heal HP at CHARACTER_HEAL() amount. If character has reached their goal, they will not encounter a foe

    :param character: a dictionary of the character's stats
    :param achieved_goal: a Boolean of whether or not goal was achieved
    :param board: a dictionary representing the game board
    :precondition: character is a dictionary of character's stats
    :precondition: character dictionary contains keys "name", "HP", "damage", "attacks", "x-location", "y-location"
    :precondition: value of "name" is a string input by the user in make_character() function
    :precondition: value of "HP" is an integer > 0
    :precondition: value of "damage" is a tuple
    :precondition: value of "attacks" is a list
    :precondition: value of "x-location" is an integer >= 0
    :precondition: value of "y-location" is an integer >= 0
    :precondition: achieved_goal is a Boolean of whether or not goal was achieved; True means goal has been achieved
    :precondition: param board contains the keys "max-x" and "max-y" with integer values >= 0
    :postcondition: character's "HP" value will be appropriately be affected by either healing if there is no foe
                    or taking possible damage if they encounter a foe and fight to the death
    :return: character's HP modified by either damage or heal, no actual return value

    No doctest, called roll() uses random module
    """
    if not achieved_goal:
        if roll(ENCOUNTER_FOE_DIE()) in range(1, 5):
            encounter(character, summon_foe(character), board)
        else:
            heal(character)
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
    """Determine character takes damage when fleeing, print message to notify character if successful.

    If successful, print message will tell character they left the encounter successfully,
    if unsuccessful, print message will show damage that character has taken.

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: character contains the key "HP"
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :postcondition: accurately modify the current character's 'HP' if they are unsuccessful fleeing
    :postcondition: informative messages are printed to confirm if character can successfully flee or has taken damage
    :return: possible modified character["HP"]
    :return: informative printed messages of flee success

    No doctests, uses random module
    """
    if roll(ENCOUNTER_FOE_DIE()) in range(1, 3):
        damage = roll(FLEE_DAMAGE_DIE())
        character["HP"] -= damage
        print(f"As you attempt to flee from the {foe['name']}, they catch up to you,\n"
              f"using {random.choice(foe['attacks'])} dealing \033[31m{damage}\033[0m damage.\n")
        time.sleep(0.5)
        print(f"You came out here to have a good time\n"
              f"but you're feeling pretty attacked right now.\n"
              f"Your health is now at \033[34m{character['HP']}\033[0m points.\n")
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
    foe["flee"] = True if roll((1, 10)) <= 2 else False


def initiative() -> bool:
    """Determine if character has initiative in battle.

    :postcondition: determine if character has initiative first in a combat round by comparing character
                    and foe rolls for initiative
    :postcondition: returns True if character initiative roll > foe's initiative roll using INITIATIVE_DIE()
    :postcondition: returns False if character initiative roll < foe's initiative roll using INITIATIVE_DIE()
    :return: a Boolean of whether or not character has initiative

    No doctests, random module used
    """
    initiative_roll = {}
    draw = True
    while draw:
        initiative_roll["character"] = roll(INITIATIVE_DIE())
        initiative_roll["foe"] = roll(INITIATIVE_DIE())
        if initiative_roll["character"] != initiative_roll["foe"]:
            draw = False
    return initiative_roll["character"] > initiative_roll["foe"]


def combat_round(attacker: dict, opposition: dict) -> None:
    """Complete one round of combat between an attacker and opposition.

    :param attacker: a dictionary of either character or foe stats
    :param opposition: a dictionary of either character or foe stats
    :precondition: both attacker and opposition dictionaries include keys-- "name", "attacks", "HP", and "damage"
    :precondition: value of "name" is a string, the name of attacker or opposition
    :precondition: value of "attacks" is a list of string elements, attack types from attacker or opposition
    :precondition: value of "HP" is an integer, the current health points of attacker or opposition
    :precondition: value of "damage" is a tuple, the damage die for attacker or opposition
    :postcondition: amount of damage from attacker to foe is determined
    :postcondition: opposition takes damage from attacker["damage"] die, their HP will be modified to reflect the change
    :postcondition: a message is printed with attacker name and attack type
    :postcondition: a message is printed with opposition name, damage taken by opposition, and updated opposition HP
    :return: no value, but opposition's HP modified by damage from attacker
    :return: printed message of attacker and attack
    :return: printed message of opposition suffering damage

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
    """Battle character and foe in combat until character or foe dies (HP == 0).

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: both character and foe dictionaries include keys-- "name", "attacks", "HP", and "damage"
    :precondition: value of "name" is a string, the name of character or foe
    :precondition: value of "attacks" is a list of string elements, attack types from character or foe
    :precondition: value of "HP" is an integer, the current health points character or foe
    :precondition: value of "damage" is a tuple, the damage die for character or foe
    :postcondition: both character and foe's HP will be sent to combat based on rolled initiative order
    :postcondition: both character and foe may take damage to their "HP" key value
    :postcondition: combat will continue until either character or foe has "HP" == 0
    :return: no value, but modified effects of key value "HP" for both character and foe after end of combat

    No doctests, called functions, combat_round() and initiative() uses random module
    """
    while character["HP"] > 0 and foe["HP"] > 0 and not foe["flee"]:
        if engage():
            if initiative():
                attacker, opposition = character, foe
            else:
                attacker, opposition = foe, character
            combat_round(attacker, opposition)
            if opposition["HP"] > 0:
                combat_round(opposition, attacker)
            if opposition["HP"] > 0 and attacker["HP"] > 0:
                foe_flee(foe)
        else:
            return flee(character, foe)


def encounter(character: dict, foe: dict, board: dict) -> None:
    """Send character into an encounter with foe.

    Encounter ends by character's choice to flee or by character and foe's fight to death
    (either character or foe's "HP" key value is 0).

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :param board: a dictionary, representing the current game map
    :precondition: both character and foe dictionaries include keys-- "name", "attacks", "HP", and "damage"
    :precondition: value of "name" is a string, the name of character or foe
    :precondition: value of "attacks" is a list of string elements, attack types from character or foe
    :precondition: value of "HP" is an integer, the current health points character or foe
    :precondition: value of "damage" is a tuple, the damage die for character or foe
    :precondition: board contains the keys "max-x" and "max-y" with integer values >= 0
    :postcondition: character either engages in battle to the death or attempts to flee
    :postcondition: character's "HP" key value may be affected by damage from flee or by entering combat
    :postcondition: foe's "HP" key value may be affected by damage from combat
    :postcondition: if foe has been defeated, print message to indicate end of encounter
    :return: no value, but accurately modified "HP" of character depending on fight or flee decision and random rolls
    :return: print message if foe has been defeated

    No doctests, called enter_combat() and flee() uses random module
    """
    print(f"\nA {foe['name']} has showed up!")
    enter_combat(character, foe)
    if foe["HP"] <= 0:
        print(f"\nFantastic, you've successfully defeated the {foe['name']},\n"
              f"you triumph in glory as you watch their shoulders slump\n"
              f"and they walk away with their head down in shame.\n"
              f"Way to go, {character['name']}! (^◇^*)\n")
        gain_exp(character, foe["EXP"], board)

    if foe["flee"]:
        print(f"\n{foe['name']} ran away.")
    time.sleep(0.5)

# ===== CHECK LEVELING UP ==============================================================================================


def gain_exp(character: dict, experience_gain: int, board: dict) -> None:
    """Increase the EXP of the character then check if they have levelled up

    :param character: a dictionary of the character's stats
    :param board: a dictionary representing the current board
    :precondition: character contains the key "EXP"
    :precondition: board is a non-empty dictionary containing coordinate keys and max-x/max-y values
    :postcondition: character gains exp, leveling up if they meet a level-up threshold
    :return: nothing, character dictionary and board may be modified
    """
    character["EXP"] += experience_gain
    print(hero_colour(f"You've earned {experience_gain} experience points. Current EXP: {character['EXP']}"))
    if character["EXP"] >= 200 and character['level'] == 1:
        level_up(character, board)
    if character["EXP"] >= 1000 and character['level'] == 2:
        level_up(character, board)


def level_up(character: dict, board: dict) -> None:
    """Levels up the game!

    Game board and character will level up

    :param character: a dictionary of character stats
    :param board: a dictionary of map stats
    :precondition: character is a dictionary of character stats containing the keys "EXP" and "level"
    :precondition: EXP value is an integer >= 0, collection of experience points that character has
    :precondition: "level" value is an integer >= 1 indicating the current level character is at
    :precondition: board is a non-empty dictionary
    :postcondition: the game is leveled up (including the character and board map)
    :return: levels up the game, not return value
    """
    character["level"] += 1
    print(f"You've level up, bless up fam. You're now able to explore new horizons!")

    if character["class"] == "Illusionist":
        level_illusionist(character)
    elif character["class"] == "Rogue":
        level_rogue(character)
    elif character["class"] == "Ranger":
        level_ranger(character)
    elif character["class"] == "Paladin":
        level_paladin(character)
    board.update(make_board(character['level']))


def level_illusionist(character: dict) -> None:
    """Level up an Illusionist class.

    :param character: a dictionary of the character stats
    :precondition: the character dictionary is non-empty
    :precondition: the value of the character's "class" key is "Illusionist"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: nothing, character dictionary is updated
    """
    if character["level"] == 2:
        level_character = ILLUSIONIST_STATS_LVL2()
        character.update(level_character)
    elif character["level"] == 3:
        level_character = ILLUSIONIST_STATS_LVL3()
        character.update(level_character)
    print(f"You are now a {character['level_name']}.")


def level_rogue(character: dict) -> None:
    """Level up a Rogue class.

    :param character: a dictionary of the character stats
    :precondition: the character dictionary is non-empty
    :precondition: the value of the character's "class" key is "Rogue"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: nothing, character dictionary is updated
    """
    if character["level"] == 2:
        level_character = ROGUE_STATS_LVL2()
        character.update(level_character)
    elif character["level"] == 3:
        level_character = ROGUE_STATS_LVL3()
        character.update(level_character)
    print(f"You are now a {character['level_name']}.")


def level_ranger(character: dict) -> None:
    """Level up a Ranger class.

    :param character: a dictionary of the character stats
    :precondition: the character dictionary is non-empty
    :precondition: the value of the character's "class" key is "Ranger"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: nothing, character dictionary is updated
    """
    if character["level"] == 2:
        level_character = RANGER_STATS_LVL2()
        character.update(level_character)
    elif character["level"] == 3:
        level_character = RANGER_STATS_LVL3()
        character.update(level_character)
    print(f"You are now a {character['level_name']}.")


def level_paladin(character: dict) -> None:
    """Level up an Paladin class.

    :param character: a dictionary of the character stats
    :precondition: the character dictionary is non-empty
    :precondition: the value of the character's "class" key is "Paladin"
    :postcondition: the character stats are levelled up accurately in accordance to their current level
    :return: nothing, character dictionary is updated
    """
    if character["level"] == 2:
        level_character = PALADIN_STATS_LVL2()
        character.update(level_character)
    elif character["level"] == 3:
        level_character = PALADIN_STATS_LVL3()
        character.update(level_character)
    print(f"You are now a {character['level_name']}.")


# ===== END GAME =======================================================================================================

def boss_flee(character: dict, foe: dict) -> None:
    """Determine character takes damage when fleeing, print message to notify character if successful.

    If successful, print message will tell character they left the encounter successfully,
    if unsuccessful, print message will show damage that character has taken.

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: character contains the key "HP"
    :precondition: the value of character["HP"] is an integer > 0, representing the character's current health points
    :postcondition: accurately modify the current character's 'HP' if they are unsuccessful fleeing
    :postcondition: informative messages are printed to confirm if character can successfully flee or has taken damage
    :return: possible modified character["HP"]
    :return: informative printed messages of flee success

    No doctests, uses random module
    """
    if roll(ENCOUNTER_FOE_DIE()) in range(1, 3):
        damage = roll(FLEE_DAMAGE_DIE())
        character["HP"] -= damage
        print(f"As you attempt to flee from {foe['name']}, they catch up to you,\n"
              f"using {random.choice(foe['attacks'])} dealing \033[31m{damage}\033[0m damage.\n")
        time.sleep(0.5)
        print(f"You came out here to have a good time\n"
              f"but you're feeling pretty attacked right now.\n"
              f"Your health is now at \033[34m{character['HP']}\033[0m points.\n"
              f"\n{foe['name']}' blank eyes follow you as you cower away in fear.\n")
    else:
        print(f"\N{foe['name']}' blank eyes follow you as you cower away in fear.")
    time.sleep(0.5)


def enter_boss_combat(character: dict, foe: dict) -> None:
    """Battle character and foe in combat until character or foe dies (HP == 0).

    :param character: a dictionary containing character stats
    :param foe: a dictionary containing foe stats
    :precondition: both character and foe dictionaries include keys-- "name", "attacks", "HP", and "damage"
    :precondition: value of "name" is a string, the name of character or foe
    :precondition: value of "attacks" is a list of string elements, attack types from character or foe
    :precondition: value of "HP" is an integer, the current health points character or foe
    :precondition: value of "damage" is a tuple, the damage die for character or foe
    :postcondition: both character and foe's HP will be sent to combat based on rolled initiative order
    :postcondition: both character and foe may take damage to their "HP" key value
    :postcondition: combat will continue until either character or foe has "HP" == 0
    :return: no value, but modified effects of key value "HP" for both character and foe after end of combat

    No doctests, called functions, combat_round() and initiative() uses random module
    """
    while character["HP"] > 0 and foe["HP"] > 0 and not foe["flee"]:
        if engage():
            if initiative():
                attacker, opposition = character, foe
            else:
                attacker, opposition = foe, character
            combat_round(attacker, opposition)
            if opposition["HP"] > 0:
                combat_round(opposition, attacker)
        else:
            boss_flee(character, foe)
            return False

    return True


def final_boss_encounter(character: dict, foe: dict):
    print("You arrive at the source of the darkness. Standing before you is an incomprehensible being made \n"
          "entirely of unending nothingness. Are you ready to die?")

    if enter_boss_combat(character, foe) == False:
        return False
    else:
        return True


    time.sleep(0.5)


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

    >>> sample_character = {"name": "Bob", "HP": 0, "x-location": 1, "y-location": 2}
    >>> end_game(sample_character)
    =======================================================
    Today just isn't your day, eh? You've been defeated.
    You're tired and your optimism level has gone down to 0.
    That's alright, we'll get them another time, Bob.
     =======================================================
    <BLANKLINE>
    Thank you for playing, Bob! - Marti & Sally
    >>> x, y = GOAL_LOCATION()
    >>> sample_character = {"name": "Suzie", "HP": 1, "x-location": x, "y-location": y}
    >>> end_game(sample_character)
    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
    Can we get a HIP-HIP (hip-hip) HOORAY?
    Suzie, you slayed the day and managed to get to the grocery store!
    Now you can head home, bake some cinnamon buns, and relax.
    ｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆
    <BLANKLINE>
    Thank you for playing, Suzie! - Marti & Sally
    >>> sample_character = {"name": "Suzie", "HP": 2, "x-location": 0, "y-location": 1}
    >>> end_game(sample_character)
    =======================================================
    You have successfully quit the game.
    We hope to see you again soon!
    =======================================================
    <BLANKLINE>
    Thank you for playing, Suzie! - Marti & Sally
    """

    if character["HP"] <= 0:
        print("\n=======================================================\n"
              "Today just isn't your day, eh? You've been defeated.\n"
              "You're tired and your optimism level has gone down to 0.\n"
              f"That's alright, we'll get them another time, {character['name']}.\n "
              f"=======================================================\n")
    elif (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        print(f"｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆\n"
              f"As you look down at Erebus' lifeless body, you see an inkling of light appear through \n"
              f"the clouds, as the moonlight begins to pour in through the shadows. \n"
              f"｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆\n")
    else:   # quit ending
        print("=======================================================\n"
              "You have successfully quit the game.\n"
              "The adventure will be continued another day.!\n"
              "=======================================================\n")
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
    board, character = start_game()
    achieved_goal = False
    while not achieved_goal and character["HP"] > 0:
        print(f"\nYou're now at ({character['x-location']}, {character['y-location']}),"
              f"\033[35m Level {character['level']}: {character['level_name']}\033[0m, "
              f"\033[34m HP: {character['HP']}/{character['max-HP']}\033[0m, "
              f"\033[36m EXP: {character['EXP']}\033[0m \n"
              f"{board[(character['x-location'], character['y-location'])]} \n")
        print_map(character, board)
        next_move(character, board)
        if character["quit"]:
            achieved_goal = True
        else:
            achieved_goal = check_goal_attained(character)
            if (character["x-location"], character["y-location"]) != GOAL_LOCATION():
                check_for_foe(character, achieved_goal, board)
    end_game(character)


def main():
    """Execute doctest."""
    game()


if __name__ == '__main__':
    # Run main() if module is being run as a program
    main()
