# 1510-A4-Text-based-adventure-game

### Your names: Martin Gatchev & Sally Poon

### Your student numbers: A01257811 & A01232177

#### ** Add any comments for me below this line **

### Special Features from Comrades

* Our map is dynamic! The map overall is 25 x 25, but the player will start with a smaller map. As they level up, the
horizons they can explore will grow.

* ASCII art implementation for the map, in order tto increase immersion for the player.
  
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
  

### Special Notes

* Although it may seem that the map is not 25x25 at first, this was a conscious decision in order give the player's
a reward for levelling up. Similar to how RPGs have areas on a map that you are not able to enter until you have 
  reached a certain level.
  
* If you'd like to beat the game the fastest way possible, we suggest following the class guidelines. The Illusionist
 for example has a very weak early game, so any time you take damage it is probably a good idea to flee and restore 
  your health in order to prepare for the next battle. Likewise, in the endgame, the Ranger class is weaker than the 
  other classes, so it is important to take note of your health as you travel through the map.
  
* The final boss is located at 24, 24: so if you would like to finish the game as fast as possible, we suggest moving 
in a south-easterly direction.
  
* The game has been balanced to be relatively easy to win with all classes, but if you find yourself struggling, we 
recommend opting for the Paladin class as it seems to perform the most consistently.



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
| Function annotations                               |   Y   |


### Game Specifications

| Modification Checklist                       | Done? |
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
| Elaborate storyline                          |   Y   |
| Change sleep timing to run the game faster   |   Y   |
| Implement color for foe and god.             |   Y   |
| Change chance of encountering foes           |   Y   |
| Change EXP gain and level up values          |   Y   |
| Make input loops to check validity           |   Y   |


### Unit Test Checklist

| In-game Function                             | Done? | Checked? |
|       -----                                  | ---   |    ---|
| hero_colour                                  |   Y   |   Y   |
| foe_colour                                   |   Y   |   Y   |
| roll                                         |   Y   |   Y   |
| get_menu                                     |   Y   |   Y   |
| get_user_choice                              |   Y   |   Y   |
| assign_hp                                    |   Y   |   Y   |
| is_not_digit                                 |   Y   |   Y   |
| get_valid_input                              |   Y   |   Y   |
| lvl_board_max                                |   Y   |   Y   |
| make_board*                                  |   Y   |   Y   |
| print_map                                    |   Y   |   Y   |
| choose_class                                 |   Y   |   Y   | <-- 1 test failed -M/ DEBUGGED -S
| get_name                                     |   Y   |   Y   |
| make_character                               |   Y   |   y   | <-- title with test_ + 2 test failed -M/ DEBUGGED -S
| start_game                                   |   Y   |   Y   |
| valid_move                                   |   Y   |   Y   |
| move_character                               |   Y   |   Y   |
| next_move                                    |   Y   |   Y   |
| heal                                         |   Y   |   Y   | <-- need to change messaging, tests run fine -M
| format_foe                                   |   Y   |   Y   |
| summon_foe                                   |   Y   |   Y   |
| select_foe                                   |   Y   |   Y   |
| check_for_foe                                |   Y   |   Y   |
| engage                                       |   Y   |   Y   |
| flee                                         |   Y   |   Y   |
| foe_flee                                     |   Y   |   Y   |
| initiative                                   |   Y   |   Y   |
| combat_round                                 |   Y   |   Y   |
| enter_combat                                 |   Y   |   Y   |
| encounter                                    |   Y   |   Y   |
| gain_exp                                     |   Y   |   Y   |
| level_up                                     |   Y   |   Y   |
| level_class                                  |   Y   |   Y   |
| goal_attained                                |   Y   |   Y   |
| summon_god                                   |   Y   |   Y   |
| final_boss_encounter                         |   Y   |   N   |
| flee_boss                                    |   Y   |   N   |
| end_game                                     |   Y   |   N   |


#### ** Add any comments for me above this line **
