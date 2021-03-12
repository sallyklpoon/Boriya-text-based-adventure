# CLASS SYSTEM

def make_character():
    """Generate a playable character.

    A function that generates a playable character in the form of a dictionary.

    :return: A dictionary that contains a playable character's information.
    """
    hero_name = input("What is your name Prisoner?\n")
    hero_character = {"name": hero_name, "level": 1, "EXP": 0, "location": (0, 0)}
    hero_class = choose_class()
    hero_character.update(hero_class)

    return hero_character

def choose_class():
    """
    Add number of attacks, crit chance, crit modifier ??
    :return:
    """

    chosen_class = class_input()
    class_list = ["Sorcerer", "Rogue", "Ranger", "Fighter"]
    class_name = class_list[int(chosen_class) - 1]

    if chosen_class == "1":
        class_dictionary = {"class": "Sorcerer", "AC": 12, "HP": 6, "atk_modifier": 4, "damage": (1, 12), "dmg_modifier": 12}
    elif chosen_class == "2":
        class_dictionary = {"class": "Rogue", "AC": 14, "HP": 8, "atk_modifier": 12, "damage": (2, 4), "dmg_modifier": 4}
    elif chosen_class == "3":
        class_dictionary = {"class": "Ranger", "AC": 16, "HP": 8, "atk_modifier": 10, "damage": (1, 6), "dmg_modifier": 6}
    elif chosen_class == "4":
        class_dictionary = {"class": "Fighter", "AC": 18, "HP": 12, "atk_modifier": 6, "damage": (1, 12), "dmg_modifier": 10}

    return class_dictionary

def class_input():
    class_name = input("What kind of an adventurer are you? [1] Sorcerer, [2] Rogue, [3] Ranger, [4] Fighter.\n")

    correct_input = False

    if class_name in ["1", "2", "3", "4"]:
        correct_input = True

    while not correct_input:
        print("That was an invalid option adventurer. Please choose a correct number.")
        class_name = input("What kind of an adventurer are you? "
                               "[1] Sorcerer, [2] Rogue, [3] Ranger, [4] Fighter.\n")
        if class_name in ["1", "2", "3", "4"]:
            correct_input = True

    return class_name

# SIMPLE LEVELING SYSTEM

def level_up():
    """
    Level names: Adventurer, Hero, God
    :return:
    """

    hero["EXP"] += 100

    if hero["EXP"] % 500 == 0:
        hero["level"] += 1
        hero["damage"] += 2
        print(f"\nYou have gained 100 EXP. You now have {hero['EXP']} EXP.\n"
              f"You feel your skill in battle increase, you have made your friend proud."
              f" You are now level {hero['level']}, and deal 1d{hero['damage']} damage.")
    else:
        print(f"\nYou have gained 100 EXP. You now have {hero['EXP']} EXP.")

# COHERENT RICH ECOSYSTEM FOR FOES

def generate_foe():

    guard = {"HP": 10}

    return guard

def generate_boss():

# PROGRAM CALLS
heromans = make_character()
print(heromans)
