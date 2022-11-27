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
        battle(character, enemy.make_enemy(character), roll_initaitve())


def roll_initaitve():
    character = randint(1, 10)
    opponent = randint(1, 10)

    if character >= opponent:
        print('\nYou are lucky today, you will attack first!\n')
        return True
    else:
        print('\nnot so lucky, your enemy will attack first!\n')
        return False


def battle(character, opponent, player_goes_first):
    character['moves'] = battle_cards()
    opponent['moves'] = battle_cards()
    player_guard = 0
    enemy_guard = 0
    if player_goes_first:
        while True:
            player_choice = player_attack(character, enemy_guard)
            if player_choice < 0:
                player_guard += player_choice
            else:
                opponent['hp'] -= player_choice
                print('{1} is now at {0} health!'.format(opponent['hp'], opponent['name']))
                if opponent['hp'] <= 0:
                    print('{0} has been defeated! You gain 1 xp. You are at {1} health.'
                          .format(opponent['name'], character['hp']))
                    break
            enemy_guard = 0
            enemy_choice = enemy_attack(opponent, player_guard)
            if enemy_choice < 0:
                enemy_guard += enemy_choice
            else:
                character['hp'] -= enemy_choice
                print('You are now at {0} health!'.format(character['hp']))
                if character['hp'] <= 0:
                    print('You are defeated')
                    return character
            player_guard = 0
    else:
        while True:
            enemy_choice = enemy_attack(opponent, player_guard)
            if enemy_choice < 0:
                enemy_guard += enemy_choice
            else:
                character['hp'] -= enemy_choice
                print('You are now at {0} health!'.format(character['hp']))
                if character['hp'] <= 0:
                    print('You are defeated')
                    return character
            player_guard = 0
            player_choice = player_attack(character, enemy_guard)
            if player_choice < 0:
                player_guard += player_choice
            else:
                opponent['hp'] -= player_choice
                print('{1} is now at {0} health!'.format(opponent['hp'], opponent['name']))
                if opponent['hp'] <= 0:
                    print('{0} has been defeated! You gain 1 xp. You are at {1} health.'
                          .format(opponent['name'], character['hp']))
                    break
            enemy_guard = 0

    print('\nthe battle is over! You are now at {} health'.format(character['hp']))
    character['moves'] = []
    character['xp'] += 1
    return character


def player_attack(character, enemy_guard):
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
                player_damage = cards_on_hand[move][1] - abs(enemy_guard) \
                    if cards_on_hand[move][1] - abs(enemy_guard) > 0 else 0
                print('You chose {1} and dealt {0} damage.'.format(player_damage, cards_on_hand[move][0]), end='')
            return player_damage
        else:
            print('that is not a valid move!')
            continue


def enemy_attack(opponent, player_guard):
    cards_on_hand = opponent['moves']
    enemy_choice = cards_on_hand[randint(0, len(cards_on_hand) - 1)]
    print('{0} chose {1}!'.format(opponent['name'], enemy_choice[0]))

    if enemy_choice[1] < 0:
        enemy_guard = enemy_choice[1]
        print('Your next attack will now do {0} less damage to {1}!'
              .format(abs(enemy_guard), opponent['name']))
        return enemy_guard
    else:
        enemy_damage = enemy_choice[1] - player_guard if enemy_choice[1] - player_guard > 0 else 0
        print('{0} dealt {1} damage to you!'.format(opponent['name'], enemy_damage), end='')
        return enemy_damage


def battle_cards():
    attacks = {'strike': 5, 'stab': 8, 'scare': 3, 'drop kick': 10, 'bite': 2, 'arrow': 10, 'ultimate': 100}
    defense = {'defend': -5, 'parry': -3, 'dodge': -10, 'guard': -8, 'garrison': -6}

    attack_combos = list(combinations(attacks.items(), 3))
    defense_combos = list(combinations(defense.items(), 2))

    return attack_combos[randint(1, len(attack_combos) - 1)] + defense_combos[randint(1, len(defense_combos) - 1)]


def main():
    # main()
    battle_cards()


if __name__ == '__main__':
    main()
