# 1510-A4-Text-based-adventure-game

### Your names: Martin Gatchev & Sally Poon

### Your student numbers: A01257811 & A01232177

#### ** Add any comments for me below this line **

### Special Features from Comrades
* healing takes place by each class' hit die rather than a constant value
* our map is dynamic! The map overall is 25 x 25, but the player will start with a smaller map. As they level up, the
horizons they can explore will grow.

* 

### Code Requirements

| Required Element                             | Location (line #) |
|       -----                                        | ---   |
| Tuple                                              |   N   |
| List                                               |   N   |
| An example of dictionary or list comprehension     |   N   |
| Selection using if-statement                       |   N   |
| Clever use of repetition with the for/while loop   |   N   |
| The membership operator (in) where it makes sense  |   N   |
| The range function                                 |   N   |
| One or more functions from itertools module        |   N   |
| The enumerate function                             |   N   |
| The filter or map function                         |   N   |
| The random module                                  |   N   |
| Function annotations                               |       |


### Game Specifications

| Modification Requirement                     | Done? |
|       -----                                  | ---   |
| game.pdf Flowchart                           |   N   |
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
| Elaborate storyline                          |   IP  |
| Change sleep timing to run the game faster   |   Y   |
| Implement color for foe and god. Use make_character    |   Y   |
| Change chance of encountering foes           |   Y   |
| Change EXP gain and level up values          |   Y   |
| Make input loops to check validity           |   Y   |


### Unit Test Checklist

| In-game Function                             | Done? | Checked? |
|       -----                                  | ---   |    ---|
| hero_colour                                  |   Y   |   N   |
| foe_colour                                   |   Y   |   N   |
| roll                                         |   Y   |   N   |
| get_menu                                     |   Y   |   N   |
| get_user_choice                              |   Y   |   N   |
| assign_hp                                    |   N   |   N   |
| is_not_digit                                 |   Y   |   N   |
| get_valid_input                              |   Y   |   N   |
| lvl_board_max                                |   Y   |   N   |
| make_board*                                  |   Y   |   N   |
| print_map                                    |   Y   |   N   |
| choose_class                                 |   Y   |   N   |
| get_name                                     |   Y   |   N   |
| make_character                               |   Y   |   N   |
| start_game                                   |   Y   |   N   |
| valid_move                                   |   Y   |   N   |
| move_character                               |   Y   |   N   |
| next_move                                    |   Y   |   N   |
| heal                                         |   Y   |   N   |
| format_foe                                   |   Y   |   N   |
| summon_foe                                   |   Y   |   N   |
| select_foe                                   |   N   |   N   |
| check_for_foe                                |   N   |   N   |
| engage                                       |   N   |   N   |
| flee                                         |   N   |   N   |
| foe_flee                                     |   N   |   N   |
| initiative                                   |   N   |   N   |
| combat_round                                 |   N   |   N   |
| enter_combat                                 |   N   |   N   |
| encounter                                    |   N   |   N   |
| gain_exp                                     |   N   |   N   |
| level_up                                     |   N   |   N   |
| level_class                                  |   N   |   N   |
| goal_attained                                |   N   |   N   |
| summon_god                                   |   N   |   N   |
| final_boss_encounter                         |   N   |   N   |
| boss_flee                                    |   N   |   N   |
| end_game                                     |   N   |   N   |


### Doc String Checklist

| In-game Function                             | MARTI |  |
|       -----                                  | ---   |    ---|
| hero_colour                                  |   Y   |   N   |
| foe_colour                                   |   Y   |   N   |
| roll                                         |   Y   |   N   |
| get_menu                                     |   Y   |   N   |
| get_user_choice                              |   Y   |   N   |
| assign_hp                                    |   N   |   N   |
| is_not_digit                                 |   Y   |   N   |
| get_valid_input                              |   Y   |   N   |
| lvl_board_max                                |   Y   |   N   |
| make_board*                                  |   Y   |   N   |
| print_map                                    |   Y   |   N   |
| choose_class                                 |   Y   |   N   |
| get_name                                     |   Y   |   N   |
| make_character                               |   Y   |   N   |
| start_game                                   |   Y   |   N   |
| valid_move                                   |   Y   |   N   |
| move_character                               |   Y   |   N   |
| next_move                                    |   Y   |   N   |
| heal                                         |   Y   |   N   |
| format_foe                                   |   Y   |   N   |
| summon_foe                                   |   N   |   N   |
| select_foe                                   |   N   |   N   |
| check_for_foe                                |   N   |   N   |
| engage                                       |   N   |   N   |
| flee                                         |   N   |   N   |
| foe_flee                                     |   N   |   N   |
| initiative                                   |   N   |   N   |
| combat_round                                 |   N   |   N   |
| enter_combat                                 |   N   |   N   |
| encounter                                    |   N   |   N   |
| gain_exp                                     |   YEP   |   N   |
| level_up                                     |   YEP   |   N   |
| level_class                                  |   YEP   |   N   |
| goal_attained                                |   YEP   |   N   |
| summon_god                                   |   YEP   |   N   |
| final_boss_encounter                         |   YEP   |   N   |
| boss_flee                                    |   YEP   |   N   |
| end_game                                     |   YEP   |   N   |



#### ** Add any comments for me above this line **
