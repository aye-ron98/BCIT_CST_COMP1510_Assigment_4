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
import enemy

def execute_final_boss(character: dict) -> dict:
    """
    Change character 'complete goal' flag to true of player defeats boss.

    :param character: a dictionary
    :precondition character: must have key 'achieved goal'
    :precondition character: value must be Boolean False
    :precondition character: must have keys 'hp', 'damage', and 'defence'
    :precondition character: values must be positive integers
    :postcondition: upon beating final boss will change 'achieved goal' value to True
    :return: an updated character dictionary
    """
    print('What out {}, its the final boss!'
          'To help you out you are getting a power buff, +20 health, +10 attack, +10 defense'.format(character['name']))
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
    :precondition character: must contain key 'location X' and 'location Y'
    :precondition board: keys must be tuples of length two comprised positive integers
    :postcondition: evaluate values of board
    """
    x_y_coordinate = (character['location X'], character['location Y'])
    if board[x_y_coordinate] == 'empty room':
        generate_scenario(character)
    if board[x_y_coordinate] == 'light challenge':
        battle(character, enemy.make_enemy(character), roll_initaitve())


def generate_scenario(player: dict) -> dict:
    """
    Update player values pending user input.

    :param player: a dictionary
    :precondition player: must contain key values 'hp', 'xp', 'damage', and 'defence'
    :precondition player: values must be integers
    :postcondition player: updates values pending user input
    :return: dictionary player
    """
    scenario_number = randint(1, 5)

    if scenario_number == 1:
        treasure_picker = randint(0, 4)
        treasures = ['stick', 'sword', 'battering ram', 'trumpet', 'flag pole']
        print("\nIt's your luck day!, You stumble across an armory, you leave with a {0}. ALl damage is now increased "
              "by +{1}."
              .format(treasures[treasure_picker], treasure_picker + 3))
        player['damage'] += treasure_picker + 3
        return player
    if scenario_number == 2:
        health_gain = randint(1, 10)
        print('\nYou come across a hospital, advertisers feed you a lot of multivitamins, you gain {} health'
              .format(health_gain))
        player['hp'] += health_gain
    if scenario_number == 3:
        defence_gain = randint(0, 4)
        shields = ['stick shield', 'aluminum shield', 'styrofoam shield', 'imaginary shield', 'kevelar vest']
        print('\nYou stubmle across an antique shop and leave with a {0}, all attacks are now reduced by {1}'
              .format(shields[defence_gain], defence_gain))
        player['defence'] += defence_gain
    if scenario_number == 4:
        print('\nA stander asks you:\n I’m tall when I’m young, and I’m short when I’m old. What am I?')
        answers = ['a candle', 'a human', 'a tree', 'an eraser']

        while True:
            for choice, answer in enumerate(answers, 1):
                print(choice, ': ', answer)
            user_input = input('\nYour answer?: ')
            if user_input == '1':
                print('Correct! You gain 1xp, you are now at {0}'.format(player['xp'] + 1))
                player['xp'] += 1
                break
            elif '2' <= user_input <= '4':
                print('The right answer was a candle! You lave with nothing')
                break
            else:
                print('that is not an option, try again')
                continue

    if scenario_number == 5:
        print('\nA stander asks you:\n What month of the year has 28 days?')
        answers = ['all of them', 'february', 'december', "what's a month?"]

        while True:
            for choice, answer in enumerate(answers, 1):
                print(choice, ': ', answer)
            user_input = input('\nYour answer?: ')
            if user_input == '1':
                print('Correct! You gain 1xp, you are now at {0}'.format(player['xp'] + 1))
                player['xp'] += 1
                break
            elif '2' <= user_input <= '4':
                print('The right answer was a all of them! You lave with nothing')
                break
            else:
                print('that is not an option, try again.')
                continue

    return player


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
    opponent['moves'] = battle_cards()
    player_guard = character['defence']
    enemy_guard = opponent['defence']

    if opponent['damage'] != 0 and character['level'] != 1:
        print('Watch out! {0} has been hitting the gym! All their attacks will have a +{1} effect!'
              .format(opponent['name'], opponent['damage']))
    elif opponent['defence'] != 0 and character['level'] != 1:
        print('{0} has been meditating lately, all your attacks will have a -{1} effect!'
              .format(opponent['name'], opponent['damage']))
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
    character['moves'] = []
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
    while True:
        for choice in range(0, len(cards_on_hand)):
            print(choice + 1, cards_on_hand[choice][0])

        move = int(input('what is your move?: ')) - 1

        if 0 <= move < len(cards_on_hand):
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
        else:
            print('{}, that is not a valid move!'.format(character['name']))
            continue


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


def main():
    """
    Drive the program
    """
    main()


if __name__ == '__main__':
    main()
