"""
enemy.py

function relating to enemy generation
"""
from random import randint


def make_enemy(character):
    enemy = {'name': enemy_name(), 'moves': [], 'hp': character['hp'] // 10 if character['level'] == 1 or character['xp'] < 3 else 20}
    return enemy


def enemy_name():
    enemy_names = {1: 'bob', 2: 'joe', 3: 'rue paul', 4: 'tenseness', 5: 'lady luck', 6: 'mississippi', 7: 'uncle sam'}

    return enemy_names[randint(1, 7)]


def main():
    # make_enemy(character={'hp': 100, 'level': 1, 'xp': 3})
    main()


if __name__ == '__main__':
    main()
