# 1510-A4-Text-based-adventure-game

### Your names: Martin Gatchev & Sally Poon

### Your student numbers: A01257811 & A01232177

#### ** Add any comments for me below this line **

### ✨ Special Features: "Bóriya" from *Comrades Studio* 🤝🏻

* Our map is dynamic! The map overall is 25 x 25, but the player will start with a smaller map. As they level up, the
horizons they can explore will grow.

* ASCII art implementation for the map, in order to increase immersion for the player.
  
* Colour coded print statements that increase readability of the game. 

* We have added additional combat statistics to the game:
    * **Armor Class** stat that dictates how likely a character is able to block/dodge an attack from a foe.
    * **Initiative modifier** that will add bonuses to the initiative roll of a character.
    * **Attack modifier** that increases the chance a character will land a hit on a foe.
    * **Damage modifier** that acts as a source of consistent damage, in case a character/foe rolls poorly.
    * **Critical Hit** mechanic:
      * The critical hit mechanic works by checking a character's attack roll and comparing it to their critical 
        hit chance. Some classes such as the Rogue have higher chances to critical hit.
      * Once a critical hit has been established, a characters critical hit modifier is used to calculate the 
    total damage they inflicted.
    
* Healing takes into account a class' hit die rather than a constant value. This was implemented to increase variety 
in classes, as well as to help with game balance.
  
* EXP gain has also been altered to allow characters to gain at least some EXP if the foe's flee. This was 
implemented to be more in line with mainstream RPG games, as well as to speed up the game.
  
* Improved input validation not only verifies if you have input a valid direction to travel, but also it
  checks if you may have inputted something other than a valid menu choice 
  (i.e. if you didn't enter a valid number choice by accident, we got you!).
  
* We have a complex set of foes in the level of weak, strong, and epic. Each foe has unique statistics and only certain
foes may appear during a player's level.
  

### 📝 Special Notes

* Although it may seem that the map is not 25x25 at first, this was a conscious decision in order give the player's
a reward for levelling up. Similar to how RPGs have areas on a map that you are not able to enter until you have 
  reached a certain level.
  
* If you'd like to beat the game the fastest way possible, we suggest following the class guidelines. The Illusionist
 for example has a very weak early game, so any time you take damage it is probably a good idea to flee and restore 
  your health in order to prepare for the next battle. Likewise, in the endgame, the Ranger class is weaker than the 
  other classes, so it is important to take note of your health as you travel through the map.
  
* In addition, HP is only gained when moving through the map. If you were to gain a level, your MAX HP increases, 
however that still means you will have to move around to heal your current health to your MAX HP levels.
  
* The final boss is located at 24, 24: so if you would like to finish the game as fast as possible, we suggest moving 
in a south-easterly direction.
  
* The game has been balanced to be relatively easy to win with all classes, but if you find yourself struggling, we 
recommend opting for the Paladin class as it seems to perform the most consistently.

### Code Stats
| Stat                | Total |
| ---                 | :---: |
| Defined Constants   | 57  |
| Unit Tests          | 158 |
| Functions           | 38  |
| Coded Lines (*excl. white spaces, encapsulating func, docstrings, and doctests*) | 291 |
| Total Lines         | 2056 |

*for lines of code per function, go to Unit Test Checklist table*

### Code Requirements

| Required Element                                   | Location (line #) |
|       -----                                        | ---   |
| Tuple                                              |   751 / 270 , 1265  |
| List                                               |   269 |
| An example of dictionary or list comprehension     |   1147 |
| Selection using if-statement                       |   1803, 915, 1332, 2044 |
| Clever use of repetition with the for/while loop   |   2036, 1604  |
| The membership operator (in) where it makes sense  |   1340, 804 |
| The range function                                 |   1340, 886, 1285 |
| One or more functions from itertools module        |   1145   |
| The enumerate function                             |   804   |
| The filter or map function                         |   748 (map), 885 (filter)   |
| The random module                                  |   1473, 764, 1632 |
| Function annotations                               |   Y   |
| Unit Tests for all necessary functions             |   Y (game() excluded)  |
| Doc Tests for all necessary functions              |   Y   |
| All output must be formatted strings               |   Y   |
| Functions no longer than 15 lines                  |   Y   |


### Game Specifications

| Modification Checklist                       | Implemented? |
|       -----                                  | :---:   |
| game.pdf Flowchart                           |   Y   |
| 25 x 25 grid environment                     |   Y   |
| character has **name**                       |   Y   |
| character has **HP**                         |   Y   |
| character has **class**                      |   Y   |
| character has **level**; start Lvl.1         |   Y   |
| character has **class-based attacks**        |   Y   |
| Create 4 classes with special attributes     |   Y   |
| game end when boss killed at fixed position  |   Y   |
| character moves N, E, S, W                   |   Y   |
| choice to run away/fight foe upon encounter  |   Y   |
| 20% foe encounter each time character moves  |   Y   |
| choice to flee before or during encounter    |   Y   |
| 20% foe will flee after each combat round    |   Y   |
| 20% foe will damage you if you flee          |   Y   |
| ASCII Map                                    |   Y   |
| End when user choose quit instead of move    |   Y   |
| Simple leveling scheme                       |   Y   |
| Max HP increases at lvl-up                   |   Y   |
| Elaborate class attacks                      |   Y   |
| Elaborate foe/god summoning                  |   Y   |
| Elaborate class healing                      |   Y   |
| Damage character does increases at lvl-up    |   Y   |
| Print critical hit messaging                 |   Y   |
| Fix attack messaging                         |   Y   |
| Foes become more challenging to defeat       |   Y   |
| Game ends if character dies                  |   Y   |
| Elaborate storyline                          |   Y   |
| Change sleep timing to run the game faster   |   Y   |
| Implement color for foe and god.             |   Y   |
| Change chance of encountering foes           |   Y   |
| Change EXP gain and level up values          |   Y   |
| Make input loops to check validity           |   Y   |


### Unit Test Checklist

| In-game Function                             | Done? | Checked? | # of lines |
|       -----                                  | :---:   |  :---: |  :---: |
| ALL DOCTESTS RUNNING?                        |YES!   |   YES!   |    -   |
| hero_colour                                  |   Y   |   Y   | 1 |
| foe_colour                                   |   Y   |   Y   | 1 |
| format_foe                                   |   Y   |   Y   | 2 |
| roll                                         |   Y   |   Y   | 2 |
| get_menu                                     |   Y   |   Y   | 9 |
| get_user_choice                              |   Y   |   Y   | 1 |
| assign_hp                                    |   Y   |   Y   | 1 |
| is_not_digit                                 |   Y   |   Y   | 4 |
| get_valid_input                              |   Y   |   Y   | 5 |
| lvl_board_max                                |   Y   |   Y   | 6 |
| make_board                                   |   Y   |   Y   | 5 |
| choose_class                                 |   Y   |   Y   | 11 |
| get_name                                     |   Y   |   Y   | 1 |
| make_character                               |   Y   |   y   | 5 |
| start_game                                   |   Y   |   Y   | 5 |
| print_map                                    |   Y   |   Y   | 10 |
| valid_move                                   |   Y   |   Y   | 9 |
| move_character                               |   Y   |   Y   | 8 |
| next_move                                    |   Y   |   Y   | 13 |
| heal                                         |   Y   |   Y   | 8 |
| summon_foe                                   |   Y   |   Y   | 10 |
| check_for_foe                                |   Y   |   Y   | 5 |
| engage                                       |   Y   |   Y   | 4 |
| flee                                         |   Y   |   Y   | 12 |
| foe_flee                                     |   Y   |   Y   | 1 |
| initiative                                   |   Y   |   Y   | 8 |
| combat_round                                 |   Y   |   Y   | 15 |
| enter_combat                                 |   Y   |   Y   | 13 |
| encounter                                    |   Y   |   Y   | 9 |
| gain_exp                                     |   Y   |   Y   | 5 |
| level_up                                     |   Y   |   Y   | 9 |
| level_class                                  |   Y   |   Y   | 8 |
| goal_attained                                |   Y   |   Y   | 9 |
| summon_god                                   |   Y   |   Y   | 4 |
| final_boss_encounter                         |   Y   |   Y   | 6 |
| flee_boss                                    |   Y   |   Y   | 8 |
| end_game                                     |   Y   |   Y   | 7 |
| game                                         |   -   |  -    | 9 |


#### ** Add any comments for me above this line **
