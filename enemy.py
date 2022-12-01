"""
enemy.py

function relating to enemy generation
"""
import random


def make_final_boss() -> dict:
    """
    Generate a final boss dictionary

    :return: a dictionary of length 4
    """
    final_boss = {'name': enemy_name(), 'moves': [], 'hp': 50, 'damage': 15, 'defence': 10}

    return final_boss


def make_enemy(character: dict) -> dict:
    """
    Generate enemy dictionary

    :param character: a dictionary
    :precondition character: must contain key 'level', 'hp', 'xp'
    :precondition character: values must be positive integers
    :precondition character: if key 'level' != 1 will generate additional key value pair
    :postcondition: will generate enemy dictionary of length 3 or 4
    :return: a dictionary of length 3 or 4
    """
    enemy = {'name': enemy_name(),
             'hp': character['hp'] // 2.5 if character['level'] == 1 else 35,
             'damage': 0 if character['level'] == 1 else random.randint(0, character['hp'] // 5)}
    enemy['defence'] = 0 if character['level'] == 1 or enemy['damage'] != 0 else random.randint(1, character['hp'] // 5)
    return enemy


def enemy_name() -> str:
    """
    Randomly select a value from the enemy_names dictionary.

    :return: a string value corresponding to the randomly selected key
    """
    enemy_names = {1: 'bob', 2: 'joe', 3: 'rue paul', 4: 'tenseness', 5: 'lady luck', 6: 'mississippi', 7: 'uncle sam'}

    return enemy_names[random.randint(1, 7)]


def additional_enemy_characteristics(opponent: dict) -> None:
    """
    Validate if key 'damage' or defence' in opponent dictionary.

    :param opponent: a dictionary
    :precondition opponent: must be a dictionary
    :postcondition: if key 'damage' in opponent > 0 will print a statement indicating so
    :postcondition: if key 'defence' in opponent > 0 will print a statement indicating so
    >>> additional_enemy_characteristics({'damage': 1, 'defence': 0, 'name': 'bob'})
    Watch out! bob has been hitting the gym! All their attacks will have a +1 effect!
    >>> additional_enemy_characteristics({'damage': 0, 'defence': 1, 'name': 'bob'})
    bob has been meditating lately, all your attacks will have a -1 effect!
    >>> additional_enemy_characteristics({'damage': 0, 'defence': 0, 'name': 'bob'})

    """
    if opponent['damage'] > 0:
        print('Watch out! {0} has been hitting the gym! All their attacks will have a +{1} effect!'
              .format(opponent['name'], opponent['damage']))
    elif opponent['defence'] > 0:
        print('{0} has been meditating lately, all your attacks will have a -{1} effect!'
              .format(opponent['name'], opponent['defence']))


def main():
    """
    Drives the program
    """
    main()


if __name__ == '__main__':
    main()
