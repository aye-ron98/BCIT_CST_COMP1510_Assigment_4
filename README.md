# BCIT_CST_COMP1510_Assigment_4

Assignment 4 for comp 1510 Fall 2022

Name:
Aron Zhang

Student Number:
A01280188

## 1. Project Description
Final assigment a python game 
	
## 2. Technologies Used
Technologies used for this project:
* Python3

## 3. Complete setup/installion/usage
Here are the steps ...
* clone this repo
* open in VS code
* naviagte to game.py and run
* have fun!

## 5. Known Bugs
Here are some known bugs:
* N/A
	
## 6. Contents of Folder
Content of the project folder:

```
 Top level of project folder: 
├── battle_unit_test         
├── character_condition_unit_test 
├── enemy_unit_test
├── movment
├── scenarios_unit_test 
├── world_building_unit_test 
├── AronZhang_aardwolf_level10.pdf 
├── README.md
├── battle_mechanics.py
├── character_condition.py 
├── enemy.py
├── game.py			# run this to play the game!
├── movement.py
├── scenarios.py 
└── world_building.py

battle_unit_tests has the follwing subfolders and files:
├── test_battle.py      
├── test_battle_cards.py
├── test_enemy_attack.py
├── test_execute_final_boss.py
├── test_player_attack.py
├── test_remove_ulitmate.py
├── test_roll_initative.py

character_coniditons_unit_tests has the follwing subfolders and files:
├── test_character_has_leveled.py   
├── test_character_health.py
├── test_execute_glow_up_protocol.py

enemy_unit_tests has the follwing subfolders and files:
├── test_additonal_enemy_characterisitcs.py      
├── test_enemy_name.py
├── test_make_enemy.py
├── test_make_final_boss.py

movement has the follwing subfolders and files:
├── test_exit_game.py        
├── test_get_user_choice.py
├── test_validate_location.py
├── test_validate_move.py

scenarios_unit_tests has the follwing subfolders and files:
├── test_add_defense.py        
├── test_add_health.py
├── test_puzzle.py
├── test_riddle.py
├── test_treasure.py

world_building_tests has the follwing subfolders and files:
├── test_generate_encounters.py       
├── test_make_board.py 
├── test_make_character.py

```

| Required Element         | module (line)          |
|:-------------------------|:-----------------------|
| Tuple                    | world_building (45)    |
| List                     | scenarios (21)         |
| dictionary comprehension | world_building (46)    |
| selection (if)           | battle_mechanics (240) |
| repetition (while)       | movement (49)          |
| in operator              | battle_mechanics (275) |
| range                    | world_building (46)    |
| itertools                | battle_mechanics (253) | 
| enumerate                | movement (21)          |
| map                      | battle_mechanics (96)  |
| random                   | scenarios (20)         |
