"""
enemy.py

function relating to enemy generation
"""
from random import randint


def make_final_boss():
    final_boss = {'name': enemy_name(), 'moves': [], 'hp': 50, 'damage': 15}

    return final_boss


def make_enemy(character):
    enemy = {'name': enemy_name(), 'moves': [],
             'hp': character['hp'] // 2.5 if character['level'] == 1 or character['xp'] < 3 else 35,
             'damage': 0 if character['level'] != 1 else randint(0, character['hp'] // 3)}
    enemy['defence'] = 0 if character['level'] != 1 and enemy['damage'] == 0 else randint(1, character['hp'] // 3)
    return enemy


def enemy_name():
    enemy_names = {1: 'bob', 2: 'joe', 3: 'rue paul', 4: 'tenseness', 5: 'lady luck', 6: 'mississippi', 7: 'uncle sam'}

    return enemy_names[randint(1, 7)]


def main():
    main()


if __name__ == '__main__':
    main()
