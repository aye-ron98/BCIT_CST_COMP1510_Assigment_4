"""
Battle_mechanics.py

functions related to fighting
- character movies
- enemy moves
- leveling
- damage
"""
from itertools import combinations
from random import randint
from movment import validate_move
import scenarios
import enemy


def execute_final_boss(character: dict) -> dict:
    """
    Modify character dictionary.

    :param character: a dictionary
    :precondition character: must have key 'hp', 'damage', 'defence'
    :precondition character: values must be positive integers
    :postcondition: will modify character values for keys 'hp', 'damage', 'defence'
    :return: an updated character dictionary
    """
    print('\nWhat out {}, its the final boss!'
          'To help you out you are getting a power buff, +20 health, +10 attack, +10 defense\n'
          .format(character['name']))
    character['hp'] += 20
    character['damage'] += 10
    character['defence'] += 10

    battle(character, enemy.make_final_boss(), roll_initaitve())

    return character


def execute_challenge_protocol(character: dict, board: dict) -> None:
    """
    Compare board value against character values.

    Calls helper functions dependent on board and character values. Returns None
    :param character: a dictionary
    :param board: a dictionary
    :precondition character: must contain key 'location'
    :precondition board: keys must be tuples of length two comprised of positive integers
    :postcondition: evaluate values of board
    """
    x_y_coordinate = character['location']
    if board[x_y_coordinate] == 'health':
        scenarios.treasure(character)
    if board[x_y_coordinate] == 'damage':
        scenarios.add_health(character)
    if board[x_y_coordinate] == 'defense':
        scenarios.add_defense(character)
    if board[x_y_coordinate] == 'puzzle':
        scenarios.puzzle(character)
    if board[x_y_coordinate] == 'riddle':
        scenarios.riddle(character)
    if board[x_y_coordinate] == 'battle':
        battle(character, enemy.make_enemy(character), roll_initaitve())


def roll_initaitve() -> bool:
    """
    Randonly return True or False.

    :return: boolean True or False
    """
    coin_flip = randint(1, 2)

    if coin_flip == 1:
        print('\nYou are lucky today, you will attack first!\n')
        return True
    else:
        print('\nnot so lucky, your enemy will attack first!\n')
        return False


def battle(character: dict, opponent: dict, player_goes_first: bool) -> dict:
    """
    Updates character dictionary pending user input.

    :param character: a dictionary
    :param opponent: a dictionary
    :param player_goes_first: boolean True or False
    :precondition character: must contain keys 'level', 'hp', 'moves', 'damage', 'defence'
    :precondition opponent: must contain keys 'level', 'hp', 'moves', 'damage', 'defence'
    :precondition: values of 'level', 'hp', 'damage', 'defence' must be positive integers
    :precondition: calues of 'moves' must be list
    :postcondition: will update values of 'level', 'hp', 'moves', 'damage', 'defence' pending user input
    :return: the dictionary character
    """
    character['moves'] = battle_cards()
    opponent['moves'] = tuple(map(remove_ultimate, battle_cards()))
    player_guard = character['defence']
    enemy_guard = opponent['defence']

    enemy.additional_enemy_characteristics(opponent)
    if player_goes_first:
        while True:
            next_enemy_attack = opponent['moves'][randint(0, len(opponent['moves']) - 1)]
            print('\nYou should know, {} is planning to use {} on you!'
                  .format(opponent['name'], next_enemy_attack[0]))

            player_choice = player_attack(character, enemy_guard)
            if player_choice < 0:
                player_guard += player_choice
            else:
                opponent['hp'] -= player_choice
                if opponent['hp'] <= 0:
                    print('{0} has been defeated! You gain 1 xp. You are at {1} health.'
                          .format(opponent['name'], character['hp']))
                    break
                else:
                    print('{1} is now at {0} health!'.format(opponent['hp'], opponent['name']))

            enemy_guard = opponent['defence']
            enemy_choice = enemy_attack(opponent, player_guard, next_enemy_attack)
            if enemy_choice < 0:
                enemy_guard += enemy_choice
            else:
                character['hp'] -= enemy_choice
                print('You are now at {0} health!'.format(character['hp']))
                if character['hp'] <= 0:
                    print('You are defeated')
                    return character
            player_guard = character['defence']
    else:
        next_enemy_attack = opponent['moves'][randint(0, len(opponent['moves']) - 1)]
        enemy_choice = enemy_attack(opponent, player_guard, next_enemy_attack)
        if enemy_choice < 0:
            enemy_guard += enemy_choice
        else:
            character['hp'] -= enemy_choice
            print('You are now at {0} health!'.format(character['hp']))
            if character['hp'] <= 0:
                print('You are defeated')
                return character
        while True:
            next_enemy_attack = opponent['moves'][randint(0, len(opponent['moves']) - 1)]
            print('\nYou should know, {} is planning to use {} on you!***'
                  .format(opponent['name'], next_enemy_attack[0]))
            player_choice = player_attack(character, enemy_guard)
            if player_choice < 0:
                player_guard += player_choice
            else:
                opponent['hp'] -= player_choice
                if opponent['hp'] <= 0:
                    print('{0} has been defeated! You gain 1 xp. You are at {1} health.'
                          .format(opponent['name'], character['hp']))
                    break
                else:
                    print('{1} is now at {0} health!'.format(opponent['hp'], opponent['name']))
            enemy_guard = opponent['defence']
            enemy_choice = enemy_attack(opponent, player_guard, next_enemy_attack)
            if enemy_choice < 0:
                enemy_guard += enemy_choice
            else:
                character['hp'] -= enemy_choice
                print('You are now at {0} health!'.format(character['hp']))
                if character['hp'] <= 0:
                    print('You are defeated')
                    return character
            player_guard = character['defence']

    print('\nthe battle is over! You are now at {} health'.format(character['hp']))
    del character['moves']
    character['xp'] += 1
    return character


def player_attack(character: dict, enemy_guard: int) -> int:
    """
    Calculate an integer to return pending values of character and enemy_guard

    :param character: a dictionary
    :param enemy_guard: a positive integer
    :precondition character: must contain key 'damage'
    :precondition character: value must be a positive integer
    :postcondition: an integer value for attack or defense
    :return: an integer
    """
    cards_on_hand = character['moves']
    print('Quickly! To battle!\n')  # start of player turn

    for choice in range(0, len(cards_on_hand)):
        print(choice + 1, cards_on_hand[choice][0])

    move = int(validate_move(1, len(cards_on_hand))) - 1

    if cards_on_hand[move][1] < 0:
        player_guard = cards_on_hand[move][1]
        print('You chose {0}, the next attack will deal {1} less damage!'
              .format(cards_on_hand[move][0], abs(player_guard)))
        return player_guard
    else:
        player_damage = cards_on_hand[move][1] + character['damage'] - abs(enemy_guard) \
            if cards_on_hand[move][1] + character['damage'] - abs(enemy_guard) > 0 else 0
        print('You chose {1} and dealt {0} damage.'.format(player_damage, cards_on_hand[move][0]), end='')
    return player_damage


def enemy_attack(opponent: dict, player_guard: int, next_attack: tuple) -> int:
    """
    Calculate an integer to return pending values of character and enemy_guard

    :param opponent: a dictionary
    :param player_guard: a positive integer
    :param next_attack: a tupple of length 2
    :precondition opponent: must contain key 'damage' and 'name'
    :precondition opponent: damage value must be a positive integer
    :precondition opponent: name value must be string
    :precondition next_attack: first item must be string second must be a positive integer
    :postcondition: an integer value for attack or defense
    :return: an integer
    >>> monster = {'name': 'keanu', 'damage': 5}
    >>> guard = 3
    >>> attack = ('example', 2)
    >>> enemy_attack(monster, guard, attack)
    keanu chose example!
    keanu dealt 4 damage to you!4
    >>> monster = {'name': 'keanu', 'damage': 5}
    >>> guard = 10
    >>> attack = ('example', 2)
    >>> enemy_attack(monster, guard, attack)
    keanu chose example!
    keanu dealt 0 damage to you!0
    """
    print('{0} chose {1}!'.format(opponent['name'], next_attack[0]))

    if next_attack[1] < 0:
        enemy_guard = next_attack[1]
        print('Your next attack will now do {0} less damage to {1}!'
              .format(abs(enemy_guard), opponent['name']))
        return enemy_guard
    else:
        enemy_damage = next_attack[1] + opponent['damage'] - abs(player_guard) \
            if next_attack[1] + opponent['damage'] - abs(player_guard) > 0 else 0
        print('{0} dealt {1} damage to you!'.format(opponent['name'], enemy_damage), end='')
        return enemy_damage


def battle_cards() -> tuple:
    """
    Generate a random tuple of tuples of length 5 and 2 respectively
    :return: a tuple of tuples
    """
    attacks = {'strike': 5, 'stab': 8, 'scare': 3, 'drop kick': 10, 'bite': 2, 'arrow': 10, 'ultimate': 20}
    defense = {'defend': -5, 'parry': -3, 'dodge': -10, 'guard': -8, 'garrison': -6}

    attack_combos = list(combinations(attacks.items(), 3))
    defense_combos = list(combinations(defense.items(), 2))

    return attack_combos[randint(1, len(attack_combos) - 1)] + defense_combos[randint(1, len(defense_combos) - 1)]


def remove_ultimate(enemy_cards: tuple) -> tuple:
    """
    Check for 'ultimate' keyword and removes it from list.

    :param enemy_cards: a tuple of tuples length 2
    :preconditon enemy_cards: nested tuples must be of (string, int) format
    :postcondition: will modify enemy_cards, removing tuples containing 'ultimate'
    and replace with tuple ('penultimate, 12)
    :postcondition: if 'ultimate' does not exist will return enemy_cards unmodified
    :return: the tuple enemy_cards
    >>> remove_ultimate((('stab', 3), ('ultimate', 10)))
    (('stab', 3), ('penultimate', 12))
    >>> remove_ultimate((('kick', 5), ('slap', 2), ('dodge', -5)))
    (('kick', 5), ('slap', 2), ('dodge', -5))
    """

    if 'ultimate' in enemy_cards[0]:
        return 'penultimate', 10
    else:
        return enemy_cards


def main():
    """
    Drive the program
    """
    main()


if __name__ == '__main__':
    main()
