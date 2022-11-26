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


def check_for_challenges(character, board):
    if board[(character['location X'], character['location Y'])] == 'empty room':
        return False
    else:
        return True


def execute_challenge_protocol(character, board):
    x_y_coordinate = (character['location X'], character['location Y'])
    if board[x_y_coordinate] == 'light challenge':
        return battle(character, enemy.make_enemy(character), roll_initaitve())


def roll_initaitve():
    character = randint(1, 10)
    opponent = randint(1, 10)

    if character >= opponent:
        return True
    else:
        return False


def battle(character, opponent, roll_initaitve):
    player_moves = character['moves'] = battle_cards()
    enemy_moves = opponent['moves'] = battle_cards()
    enemy_guard = 0
    player_guard = 0
    if roll_initaitve:
        while character['hp'] != 0 or opponent['hp'] != 0:
            print('\nQuickly! To battle!\n')  # start of player turn
            for choice, move in enumerate(player_moves[1], len(player_moves)):
                print(choice, move)

            move = int(input('\nwhat is your move?: '))

            if 0 < move < 5:
                if player_moves[move][1] < 0:
                    player_guard = player_moves[move][0]
                    print('\nYou chose {0}, the next attack will deal {1} less damage!'
                          .format(player_moves[move], abs(player_moves[move][0])))
                else:
                    player_damage = 0
                    player_damage = player_moves[move][1] - abs(enemy_guard) \
                        if player_damage > 0 else player_damage == 0
                    opponent['hp'] -= player_damage
                    print('\nYou dealt {0} damage to thr enemy!\n'
                          'They are now at {1} health!'.format(player_damage, opponent['hp']))
                if opponent['hp'] == 0:
                    print('Congratulations! You have defeated {}'.format(opponent['name']))
                    break

            enemy_guard = 0
            enemy_choice = enemy_moves[randint(1, len(enemy_moves))]  # start of enemy turn
            print('\nenemy chose {}!\n'.format(enemy_choice[0]))

            if enemy_choice < 0:
                enemy_guard = enemy_choice[1]
                print('Your next attack will now do {0} less damage to {1}!\n'
                      .format((abs(enemy_guard)), opponent['name']))
            else:
                enemy_damage = 0
                enemy_damage = enemy_choice[1] - abs(player_guard) if enemy_damage > 0 else enemy_damage == 0
                character['hp'] -= enemy_damage
                print('{0} dealt {1} damage to you! You are now at {2} health!'
                      .format(opponent['name'], enemy_damage, character['hp']))
            if character['hp'] == 0:
                print('you lost!')
                break
            player_guard = 0
    else:
        while character['hp'] != 0 or opponent['hp'] != 0:
            enemy_choice = enemy_moves[randint(1, len(enemy_moves))]  # start of enemy turn
            print('\nenemy chose {}!\n'.format(enemy_choice[0]))

            if enemy_choice < 0:
                enemy_guard = enemy_choice[1]
                print('Your next attack will now do {0} less damage to {1}!\n'
                      .format((abs(enemy_guard)), opponent['name']))
            else:
                enemy_damage = 0
                enemy_damage = enemy_choice[1] - abs(player_guard) if enemy_damage > 0 else enemy_damage == 0
                character['hp'] -= enemy_damage
                print('{0} dealt {1} damage to you! You are now at {2} health!'
                      .format(opponent['name'], enemy_damage, character['hp']))
            if character['hp'] == 0:
                print('you lost!')
                break
            player_guard = 0

            print("it's your turn now!\n")  # start of player turn
            for choice, move in enumerate(player_moves[1], len(player_moves)):
                print(choice, move)

            move = int(input('\nwhat is your move?: '))

            if 0 < move < 5:
                if player_moves[move][1] < 0:
                    player_guard = player_moves[move][0]
                    print('\nYou chose {0}, the next attack will deal {1} less damage!'
                          .format(player_moves[move], abs(player_moves[move][0])))
                else:
                    player_damage = 0
                    player_damage = player_moves[move][1] - abs(enemy_guard) \
                        if player_damage > 0 else player_damage == 0
                    opponent['hp'] -= player_damage
                    print('\nYou dealt {0} damage to thr enemy!\n'
                          'They are now at {1} health!'.format(player_damage, opponent['hp']))
                if opponent['hp'] == 0:
                    print('Congratulations! You have defeated {}'.format(opponent['name']))
                    break
            enemy_guard = 0

    print('the battle is over! You are now at {} health'.format(character['hp']))
    character['moves'] = []
    return character


def battle_cards():
    attacks = {'strike': 5, 'stab': 8, 'scare': 3, 'drop kick': 10, 'bite': 2, 'arrow': 10, 'ultimate': 100}
    defense = {'defend': -5, 'parry': -3, 'dodge': -10, 'guard': -8, 'garrison': -6}

    attack_combos = list(combinations(attacks.items(), 3))
    defense_combos = list(combinations(defense.items(), 2))

    return attack_combos[randint(1, len(attack_combos))] + defense_combos[randint(1, len(defense_combos))]


def main():
    # main()
    battle_cards()


if __name__ == '__main__':
    main()
