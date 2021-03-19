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

# ======================================================================================================================
#                                                     CONSTANTS
# ======================================================================================================================

# ===== MAP CONSTANTS ==================================================================================================


def MAX_MAP_X_LVL1():
    """Return maximum map x-dimension = 5.

    :return: MAX_MAP_X dimensions as an integer
    """
    return 10


def MAX_MAP_Y_LVL1():
    """Return maximum map y-dimension = 5.

    :return: MAX_MAP_Y dimensions as an integer
    """
    return 10


def MAX_MAP_X_LVL2():
    return 25


def MAX_MAP_Y_LVL2():
    return 20


def MAX_MAP_X_LVL3():
    return 25


def MAX_MAP_Y_LVL3():
    return 25


def MAP_SCRIPTS():
    """Return a tuple of map scripts.

    :return: a tuple of map scripts
    """
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


def START_X():
    """Return character's starting x-location = 0.

    :return: START_X location as an integer
    """
    return 0


def START_Y():
    """Return character's starting y-location = 0.

    :return: START_Y location as an integer
    """
    return 0


def GOAL_LOCATION():
    """Return goal coordinates = (4, 4)

    :return: GOAL() coordinates as a tuple (x, y)
    """
    return 4, 4


def START_GAME_MSG():
    return "========================❋✿❀✿❋❋✿❀✿❋❋✿❀✿❋===========================\n"\
           "Welcome to Avocado Toast, a game about Gen Z and Millennial struggles\n"\
           "because we are a self-deprecating generation.\n" \
           "You've just completed a 7-hour hackathon and you've spent the last\n"\
           "few days pent up in your room studying for midterms. It could be nice to\n"\
           "get outside and enjoy the Spring weather. Maybe hit the grocery store\n"\
           "to grab some ingredients for a soothing baking session this evening.\n"\
           "========================❋✿❀✿❋❋✿❀✿❋❋✿❀✿❋===========================\n"


def CLASS_INFO():
    return "\033[1m<< Class Option 1 >>\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n" \
           "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud\n" \
           "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in.\n" \
           "\n" \
           "\033[1m<< Class Option 2 >>\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n" \
           "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud\n" \
           "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in.\n" \
           "\n" \
           "\033[1m<< Class Option 3 >>\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n" \
           "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud\n" \
           "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in.\n" \
           "\n" \
           "\033[1m<< Class Option 4 >>\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n" \
           "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud\n" \
           "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in.\n" \


# ===== MENU CONSTANTS =================================================================================================


def MOVE_OPTIONS():
    """Return tuple of move options as a list of string directions.

    :return: tuple of direction options
    """
    return "go North", "go South", "go West", "go East", "Quit Game"


def ENGAGE_OPTIONS():
    """Return engage options as a tuple of strings.

    :return: tuple of engagement options
    """
    return "Attack", "Flee"


def COMBAT_OPTIONS():
    """Return combat options as a tuple of strings.

    :return: tuple of combat options
    """
    return "Continue Combat", "Flee"


def CLASS_OPTIONS():
    """Return class options as a tuple of strings.

    :return: tuple of class options
    """
    return "Illusionist", "Rogue", "Ranger", "Paladin"


# ===== CHARACTER CONSTANTS ============================================================================================


def CHARACTER_MAX_HP():
    """Return the maximum character HP = 20.

    :return: MAX_CHARACTER_HP, an integer of character's max HP
    """
    return 20


def CHARACTER_DAMAGE_DIE():
    """Return the character damage die as a tuple, 1d10 = (1, 10).

    :return: a character's damage die as a tuple (rolls, number_of_sides)
    """
    return 1, 10


def CHARACTER_ATTACKS():
    """Return a tuple of a character's available attack types.

    :return: a tuple of character's attack types
    """
    return ("Perseverance", "Patience", "Setting Healthy Boundaries",
            "Empowerment", "Integrity", "Authenticity")


def CHARACTER_HEAL():
    """Return the maximum heal for HP if monster not encountered = 4.

    :return: an integer, the amount a character heals
    """
    return 4


def CHARACTER_START_LEVEL():
    """Return the character's starting level = 1.

    :return: an integer, representing the starting level of a character as defined above
    """
    return 1


def LEVEL_UP_THRESHOLD():
    """Return the threshold at which characters can level up = 500

    :return: an integer value of the threshold at which character can level up, as defined above
    """
    return 500


def LEVEL_DAMAGE_MODIFIER():
    """Return the bonus damage modifier for a character, 2

    :return: integer of bonus damage modifier as indicated in description above
    """
    return 2


# ===== FOE CONSTANTS ==================================================================================================


def FOE_NAMES():
    """Return a tuple of foe names.

    Recommend to use in conjunction with FOE_ATTACKS() which consists of Foe Attacks associated
    with each foe in this tuple.

    :return: a tuple containing names of foes
    """
    all_foe_names = ("Coffee Shop Barista",
                     "Dating App",
                     "Crappy Client",
                     "Existential Crisis",
                     "New-Age Teen",
                     "'Woke''Friend'",
                     "Job Posting")
    return all_foe_names


def FOE_ATTACKS():
    """Return a tuple of foe attacks.

    Recommend to use in conjunction with FOE_NAMES() which consists of Foe Names associated
    with each foe attack list in this tuple.

    :return: a tuple containing foes attacks
    """
    all_foe_attacks = (
        ["$12 Small Coffee", "Wrong Order", "Misspelled Name", "Out Of Cream And Sugar"],
        ["Corny Profile", "Sliding into Your DMs", "Lame Pickup Line", "Ghosted - POOF!"],
        ["Give Me A Discount Because I Know You", "Paid In Experience", "No Reply To Invoices",
         "'You're Not A Professional, You'll Get This On Your Portfolio!'"],
        ["Crippling Anxiety", "Pure Nihilism", "Angst", "Dread"],
        ["Tik-Tok Dance", "Viral Meme", "YEET", "Phone Scroll"],
        ["'I Just Think Mask Mandates Are Harsh'", "'Wake Up Sheeple!!1!'", "Do You Invest In Bitcoin?",
         "'Don't You Think The World Is *TOO* Progressive?'", "'Not To Be Racist But...'"],
        ["'Required: 32 years of experience'", "'Must possess a PhD'", "'Most Canadians are under-employed!'"])
    return all_foe_attacks


def FOE_MAX_HP():
    """Return a maximum foe HP = 10.

    A protective function for the foe's maximum HP constant.

    :return: MAX_CHARACTER_HP, an integer of foe's max HP
    """
    return 10


def FOE_DAMAGE_DIE():
    """Return the foe damage die as a tuple, 1d10 = (1, 10)

    :return: a foe's damage die as a tuple (rolls, number_of_sides)
    """
    return 1, 10


# ===== COMBAT CONSTANTS ===============================================================================================


def DAMAGE_RESPONSE():
    """Return a tuple of possible damage responses.

    :return: a tuple of possible damage responses
    """
    return ("Stumbles", "Curls Up in Fetal Position", "Screams in Binary",
            "Feels Sick", "Laughs Nervously")


def INITIATIVE_DIE():
    """Return the initiative die, 1d100 = (1, 100)

    :return: an initiative die as a tuple (rolls, number_of_sides)
    """
    return 1, 100


def ENCOUNTER_FOE_DIE():
    """Return the summon foe die, 1d10 = (1, 10)

    :return: an encounter foe die as a tuple (rolls, number_of_sides)
    """
    return 1, 10


def FLEE_DAMAGE_DIE():
    """Return the foe damage die when a character flees as a tuple, 1d4 = (1, 4)

    :return: a foe's damage die when a character flees unsuccessfully as a tuple (rolls, number_of_sides)
    """
    return 1, 4


def ATTACK_DIE():
    """Return the attack roll die, 1d20 = (1, 20)

    :return: the attack roll die as a tuple, (rolls, number_of_sides)
    """
    return 1, 20


# ======================================================================================================================
#                                              FUNCTIONS START HERE
# ======================================================================================================================


# ===== COMMON FUNCTIONS ===============================================================================================

def hero_colour(string):
    return f"\033[36m{string}\033[0m"


def foe_colour(string):
    return f"\033[33m{string}\033[0m"


def roll(die):
    """Roll a die with the specified number of sides the specified number of times.

    :param die: a tuple
    :precondition: the accepted die must be a tuple with two integers (rolls, sides)
    :precondition: rolls must be an int, represents the number of rolls for the die
    :precondition: sides must be an int, represents the number of sides on the die being rolled
    :postcondition: calculate the sum of the die rolled a specified number of times
    :return: the sum of rolled numbers

    No doctests, function uses random.int()
    """
    rolls, sides = die
    return random.randint(1, sides * rolls)


def get_menu(menu_type):
    """Print menu options for a given menu type of either "move" or "combat".

    :param menu_type: a string
    :precondition: menu_type is a string asking for the correct menu
    :precondition: menu_type is either "move" or "combat" only
    :postcondition: print enumerated MOVE_OPTIONS() if menu_type is "move"
    :postcondition: print enumerated COMBAT_OPTIONS() if menu_type is "combat"
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


def valid_menu_input(selected_option, menu_type):
    return int(selected_option) in range(1, len(menu_type) + 1)


# ===== START GAME =====================================================================================================


def lvl_board_max(level):
    if level == 1:
        return MAX_MAP_Y_LVL1(), MAX_MAP_Y_LVL1()
    elif level == 2:
        return MAX_MAP_X_LVL2(), MAX_MAP_Y_LVL2()
    else:
        return MAX_MAP_X_LVL3(), MAX_MAP_X_LVL3()


def make_board(character):
    """Create a dictionary to represent a board with given map_dimensions.

    For key:value pairs in the dictionary, coordinates will be keys and descriptions will be values.

    :postcondition: returns a dictionary data structure of the game's board
    :postcondition: the key values in the dictionary are coordinates represented in tuples (x, y)
    :return: a dictionary of the game board

    # >>> board = make_board()
    # >>> type(board)
    # <class 'dict'>
    # >>> pp = pprint.PrettyPrinter()
    # >>> pp.pprint(board)
    """
    map_script = itertools.cycle(MAP_SCRIPTS())
    lvl_max_x, lvl_max_y = lvl_board_max(character['level'])
    board = {(x_location, y_location): next(map_script)
             for x_location in range(lvl_max_x)
             for y_location in range(lvl_max_y)}
    board['max-x'], board['max-y'] = lvl_max_x, lvl_max_y
    return board


def print_map(character, board):
    """Print a map of where the character is located on a board.

    :param character: a dictionary of character stats
    :param board: a dictionary of the board
    :precondition
    :precondition: character is a dictionary of stats with keys, "x-location" and "y-location"
    :precondition: the values of "x-location" and "y-location" are both integers that are >= 0
                   and less than the MAX_MAP_X and MAX_MAP_Y values, respectively
    :postcondition: print out a visual map with the correct location as to where the character is on a board
    :return: printed map
    """
    for row in range(board['max-y']):
        for column in range(board['max-x']):
            print(f"[{hero_colour('웃')}]", end="") \
                if (column, row) == (character["x-location"], character["y-location"])\
                else print("[  ]", end="")
        print("")


def get_class():
    return input("\nEnter the number of your class choice: ")


def choose_class():
    print("\nWhat kind of adventurer are you?\n")
    print(CLASS_INFO())
    get_menu("class")
    chosen_class = get_class()
    if chosen_class == "1":
        return {"class": "Illusionist", "level_name": "Trickster",
                "AC": 12, "HP": 6, "max-HP": 6,
                "attacks": ["Colour Spray", "Phantasmal Force", "Shadow Blade"],
                "atk_modifier": 4, "damage": (1, 12), "dmg_modifier": 12,
                "crit_chance": [20], "crit_modifier": 2}
    elif chosen_class == "2":
        return {"class": "Rogue", "level_name": "Cutpurse",
                "AC": 14, "HP": 8, "max-HP": 8,
                "attacks": ["Sneak Attack", "their Longsword", "their Crossbow"],
                "atk_modifier": 12, "damage": (2, 4), "dmg_modifier": 4}
    elif chosen_class == "3":
        return {"class": "Ranger", "level_name": "Scout",
                "AC": 16, "HP": 8, "max-HP": 8,
                "attacks": ["Strike", "their Longbow", "Thorn Whip"],
                "atk_modifier": 10, "damage": (1, 6), "dmg_modifier": 6}
    elif chosen_class == "4":
        return {"class": "Paladin", "level_name": "Protector",
                "AC": 18, "HP": 12, "max-HP": 12,
                "attacks": ["their Hand-axe", "their Crossbow", "a Powerful Punch"],
                "atk_modifier": 6, "damage": (1, 12), "dmg_modifier": 10}


def get_name():
    """Ask user for their character name.

    :postcondition: return the user's input name as a string
    :return: string of character name
    """
    return input("What's your name? ")


def make_character():
    """Create a character dictionary with character details

    :precondition: make_character() is called
    :postcondition: returns a complete character dictionary
    :postcondition: character dictionary contains keys "name", "HP", "damage", "attacks", "x-location", "y-location"
    :postcondition: value of "name" is a string input by the user
    :postcondition: value of "HP" is an integer, determined by CHARACTER_MAX_HP()
    :postcondition: value of "damage" is a tuple, determined by CHARACTER_DAMAGE_DIE()
    :postcondition: value of "attacks" is a list, determined by CHARACTER_ATTACKS()
    :postcondition: value of "x-location" is an integer, determined by START_X()
    :postcondition: value of "y-location" is an integer, determined by START_Y()
    :return: a complete character dictionary

    No doctests, input is required
    """
    character = {"name": hero_colour(get_name()),
                 "x-location": START_X(),
                 "y-location": START_Y(),
                 "EXP": 0,
                 "level": CHARACTER_START_LEVEL(),
                 "quit": False}
    character.update(choose_class())
    character["attacks"] = list(map(hero_colour, character["attacks"]))
    return character


def start_game():
    """Start up the game by returning map and character information.

    :postcondition: collects result of the map as a dictionary
    :postcondition: collects result of the character as a dictionary
    :postcondition: produces a tuple of both map and character data structures in the order (map, character)
    :return: map and character data structures as a tuple (map, character)

    No doctests. Calls make_character(), which requires user input.
    """
    print(START_GAME_MSG())
    character = make_character()
    return make_board(character), character


# ===== NEXT MOVE (VALIDATE AND MOVE) ==================================================================================


def valid_move(direction, x_location, y_location, board):
    """Validate the character's movement is valid (in the board).

    Return Boolean True for valid move and False for invalid move.

    :param direction: integer between [1, 4]
    :param x_location: an integer representing character's current x-location
    :param y_location: an integer representing chraracter's current y-location
    :param board: a dictionary of the board
    :precondition: direction is an integer representative of moving
    :precondition: direction == 1 is moving north, or y - 1
    :precondition: direction == 2 is moving south, or y + 1
    :precondition: direction == 3 is moving west, or x - 1
    :precondition: direction == 4 is moving east, or x + 1
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


def move_character(direction, character):
    """Move the character in the direction indicated.

    :param direction: an integer representing where character will move
    :param character: a dictionary, the character's dictionary
    :precondition: the character dictionary contains an "x_location" and "y_location" key
    :precondition: the values of the "x_location" and "y_location" key in the character dictionary are
                   integers representing coordinates x and y of the character at the current moment
    :precondition: the direction being moved has been validated and is a valid move for the character
    :postcondition: accurately move the character by updating the character's x and y coordinates
    :precondition: direction == 1 is moving north, will change character's current y-coordinate to y - 1
    :precondition: direction == 2 is moving south, will change character's current y-coordinate to y + 1
    :precondition: direction == 3 is moving west, will change character's current x-coordinate to x - 1
    :precondition: direction == 4 is moving east, will change character's current x-coordinate to x + 1
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


def get_direction():
    """Ask user for the direction they want to go.

    :postcondition: return the user's input name as a string containing an integer [1, 5]
    :return: string of direction they'd like to go [1, 5]
    """
    return input("Enter the number of your decision: ")


def next_move(character, board):
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
    print("\nWhich direction would you like to go?")
    get_menu("move")
    while not move_valid:
        direction = get_direction()
        if direction == "5":
            move_valid, character["quit"] = True, True
        else:
            if valid_move(direction, character["x-location"], character["y-location"], board):
                move_valid = True
                move_character(direction, character)
            else:
                print("Move is invalid...")
    time.sleep(1)


# ===== CHECK IF GOAL ATTAINED =========================================================================================


def check_goal_attained(x_location, y_location):
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
    return (x_location, y_location) == GOAL_LOCATION()


# ===== CHECK FOR MONSTERS =============================================================================================


def heal(character):
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
    >>> sample_character["HP"]
    20
    >>> sample_character = {"name": "Bob", "HP": 1, "max-HP": 10}
    >>> heal(sample_character)
    >>> sample_character["HP"]
    5
    """
    threshold = character["max-HP"] - CHARACTER_HEAL()
    if character["HP"] == character["max-HP"]:
        print("\nNothing happens.")
    else:
        if character["HP"] < threshold:
            character["HP"] += CHARACTER_HEAL()
        else:
            character["HP"] = character["max-HP"]
        print("\n\033[32m.・。.・゜ As you take a step, you suddenly feel "
              "reinvigorated by the decent day you're having.・゜・。.\n"
              f".・。.・゜Your health has been healed to {character['HP']} points. (◡‿◡✿)・゜・。.\n\033[0m")
    time.sleep(1)


def summon_foe():
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
    all_foes = list(zip(FOE_NAMES(), FOE_ATTACKS()))
    foe_name, foe_attacks = random.choice(all_foes)
    return {"name": foe_colour(foe_name),
            "attacks": list(map(foe_colour, foe_attacks)),
            "atk_modifier": 0,
            "HP": FOE_MAX_HP(),
            "max-HP": FOE_MAX_HP(),
            "damage": FOE_DAMAGE_DIE(),
            "dmg_modifier": 0,
            "AC": 10,
            "flee": False}


def check_for_foe(character, achieved_goal, board):
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
            encounter(character, summon_foe(), board)
        else:
            heal(character)
    else:
        heal(character)


# ===== FOE ENCOUNTER ==================================================================================================


def get_engage_decision():
    """Ask user for the combat decision.

    :postcondition: return the user's input as a string containing an integer [1, 2]
    :return: string of combat decision [1, 2]
    """
    return input("Enter the number of your decision: ")


def engage():
    """Ask character if they would like to engage with or flee from foe.

    :postcondition: determine, based on character's decision, if they will engage in combat or flee
    :postcondition: if user's input is 1, result of engage is True (engage)
    :postcondition: if user's input is 2, result of engage is False (flee)
    :return: Boolean value of whether or not character will engage

    No doctests, user input required
    """
    print("\nWhat will you do next, adventurer?")
    get_menu("engage")
    engage_choice = get_engage_decision()
    time.sleep(1)
    return engage_choice == "1"


def flee(character, foe):
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
              f"using {random.choice(foe['attacks'])} and dealing \033[31m{damage}\033[0m damage.\n")
        time.sleep(1)
        print(f"You came out here to have a good time\n"
              f"but you're feeling pretty attacked right now.\n"
              f"Your health is now at \033[34m{character['HP']}\033[0m points.\n")
    else:
        print(f"\nYou said 'bye, Felicia!' and got out of {foe['name']}'s view range.\n"
              f"Phew! That was a close one.\n")
    time.sleep(2)


def foe_flee(foe):
    """Determine if foe will flee.

    :param foe:
    :return:
    """
    foe["flee"] = True if roll((1, 10)) <= 2 else False


def initiative():
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


def combat_round(attacker, opposition):
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
    attack_roll = roll(ATTACK_DIE()) + attacker["atk_modifier"]
    print(f"\n{attacker['name']} attacks using {random.choice(attacker['attacks'])}!")
    time.sleep(1)
    if attack_roll >= opposition["AC"]:
        attack_damage = roll(attacker["damage"]) + attacker["dmg_modifier"]
        opposition["HP"] -= attack_damage
        print(f"{opposition['name']} {random.choice(DAMAGE_RESPONSE())} and takes "
              f"\033[31m{attack_damage}\033[0m damage.\n"
              f"{opposition['name']}'s health level is now "
              f"\033[34m{opposition['HP']}/{opposition['max-HP']}\033[0m...\n")
    else:
        print(f"{opposition['name']} dodges the attack successfully.")
    time.sleep(2)


def enter_combat(character, foe):
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
            return flee(character, foe)


def encounter(character, foe, board):
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
    print(f"\n A {foe['name']} has showed up!\n")
    enter_combat(character, foe)
    if foe["HP"] <= 0:
        print(f"Fantastic, you've successfully defeated this {foe['name']},\n"
              f"you triumph in glory as you watch their shoulders slump\n"
              f"and they walk away with their head down in shame.\n"
              f"Way to go, {character['name']}! (^◇^*)\n")
        gain_exp(character, board)

    if foe["flee"]:
        print(f"{foe['name']} ran away.")
    time.sleep(1)

# ===== CHECK LEVELING UP ==============================================================================================


def gain_exp(character, board):
    """

    :param character:
    :param board:
    :return:
    """
    character["EXP"] += 100
    print(f"You've earned +100 experience points. Current EXP: {hero_colour(str(character['EXP']))}\n")
    if character["EXP"] == 500:
        level_up(character, board)
    if character["EXP"] == 1250:
        level_up(character, board)
    if character["EXP"] == 2500:
        level_up(character, board)


def level_up(character, board):
    """Levels up the game if character meets level_up threshold!

    :param character: a dictionary of character stats
    :param board: a dictionary of map stats
    :precondition: character is a dictionary of character stats containing the keys "EXP" and "level"
    :precondition: EXP value is an integer >= 0, collection of experience points that character has
    :precondition: "level" value is an integer >= 0 indicating the current level character is at
    :precondition: board is a non-empty dictionary
    :postcondition: the game is leveled up (including the character and map)
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
    board.update(make_board(character))


def level_illusionist(character):
    """

    :param character:
    :return:
    """
    if character["level"] == 2:
        level_character = {"level_name": "Mesmer", "AC": 15,
                           "attacks": ["Hypnotic Pattern", "Shatter", "Mind Spike"],
                           "atk_modifier": 8, "damage": (1, 20), "dmg_modifier": 16, "crit_chance": [20],
                           "crit_modifier": 3}
        character.update(level_character)
    elif character["level"] == 3:
        level_character = {"class": "Creator", "level_name": "Trickster", "AC": 20,
                           "attacks": ["Psychic Scream", "Mental Prison", "Ravenous Void"],
                           "atk_modifier": 10, "damage": (1, 32), "dmg_modifier": 20,
                           "crit_chance": [20], "crit_modifier": 5}
        character.update(level_character)
    print(f"You are now a {character['level_name']}.")


def level_rogue(character):
    """

    :param character:
    :return:
    """
    if character["level"] == 2:
        character["level_name"] = "Assassin"
    elif character["level"] == 3:
        character["level_name"] = "Shadow Master"
    print(f"You are now a {character['level_name']}.")


def level_ranger(character):
    """

    :param character:
    :return:
    """
    if character["level"] == 2:
        character["level_name"] = "Pathfinder"
    elif character["level"] == 3:
        character["level_name"] = "Far Wanderer"
    print(f"You are now a {character['level_name']}.")


def level_paladin(character):
    """

    :param character:
    :return:
    """
    if character["level"] == 2:
        character["level_name"] = "Guardian"
    elif character["level"] == 3:
        character["level_name"] = "Justiciar"
    print(f"You are now a {character['level_name']}.")


# ===== END GAME =======================================================================================================


def end_game(character):
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
        print("=======================================================\n"
              "Today just isn't your day, eh? You've been defeated.\n"
              "You're tired and your optimism level has gone down to 0.\n"
              f"That's alright, we'll get them another time, {character['name']}.\n "
              f"=======================================================\n")
    elif (character["x-location"], character["y-location"]) == GOAL_LOCATION():
        print(f"｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆\n"
              f"Can we get a HIP-HIP (hip-hip) HOORAY?\n"
              f"{character['name']}, you slayed the day and managed to get to the grocery store!\n"
              f"Now you can head home, bake some cinnamon buns, and relax.\n"
              f"｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆｡･:*:･ﾟ★,｡･:*:･ﾟ☆\n")
    else:   # quit ending
        print("=======================================================\n"
              "You have successfully quit the game.\n"
              "We hope to see you again soon!\n"
              "=======================================================\n")
    print(f"Thank you for playing, {character['name']}! - Marti & Sally")


# ======================================================================================================================
#                                              MAIN GAME FUNCTION
# ======================================================================================================================


def game():
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
        time.sleep(1.5)
        print_map(character, board)
        next_move(character, board)
        if character["quit"]:
            achieved_goal = True
        else:
            achieved_goal = check_goal_attained(character["x-location"], character["y-location"])
            check_for_foe(character, achieved_goal, board)
    end_game(character)


def main():
    """Execute doctest."""
    game()


if __name__ == '__main__':
    # Run main() if module is being run as a program
    main()
