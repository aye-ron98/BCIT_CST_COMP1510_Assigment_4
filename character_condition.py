"""
character_condition.py

functions that check character status
- level
- health
-xp
"""
import movment


def character_has_leveled(character: dict) -> dict:
    """
    Updates values of character dictionary.

    :param character: a dictionary.
    :precondition character: must contain keys 'level', 'xp', 'hp', glow up'
    :precondition character: values must be integer
    :return: an updated dictionary character
    >>> my_character = {'level': 1, 'xp': 3, 'hp': 30, 'defence': 0, 'damage': 0, 'glow up': False}
    >>> character_has_leveled(my_character)
    {'level': 2, 'xp': 0, 'hp': 50, 'defence': 10, 'damage': 10, 'glow up': True}
    >>> character_level_2 = {'level': 2, 'xp': 3, 'hp': 10, 'defence': 0, 'damage': 0, 'glow up': False}
    >>> character_has_leveled(character_level_2)
    {'level': 2, 'xp': 3, 'hp': 10, 'defence': 0, 'damage': 0, 'glow up': False}
    """
    if character['level'] == 1:
        if character['xp'] == 3:
            character['level'] = 2
            character['xp'] = 0
            character['hp'] = 50
            character['defence'] += 10
            character['damage'] += 10
            character['glow up'] = True
    elif character['level'] == 2:
        if character['xp'] == 5:
            character['level'] = 3
            character['xp'] = 0
            character['hp'] = 100
            character['defence'] += 25
            character['damage'] += 25
            character['glow up'] = True
            character['level cap'] = True

    return character


def character_health(character: dict) -> bool:
    """
    Check value of character dictionary key 'hp'. Returns True if value is != 0 else False.

    Does not modify dictionary values.
    :param character: a dictionary
    :precondition character: must contain key 'hp'
    :postcondition: will return True or False
    :return: a boolean True or False
    >>> my_character = {'hp': 0}
    >>> character_health(my_character)
    True
    >>> healthy_character = {'hp': 10}
    >>> character_health(healthy_character)
    False
    """
    if character['hp'] <= 0:
        return True
    else:
        return False


def execute_glow_up_protocol(character: dict) -> dict:
    """
    Update character dictionary values

    :param character: a dictionary
    :precondition character: must contain keys 'glow up', 'damage', 'defence' 'hp', 'name'
    :postcondition: will update character values pending user input
    :return: the dictionary character
    """
    if character['glow up']:
        print('\nCongratulations! {} have leveled up!'
              'choose an upgradable from the following!\n'.format(character['name']))
        character['glow up'] = False
        upgradeables = ['+10 health', '+10 base damage', '+10 base defence']
        for choice, item in enumerate(upgradeables, 1):
            print(item, ': ', choice)

        user_choice = movment.validate_move(1, 3)

        if user_choice == '1':
            character['hp'] += 10
            print('\nYour health is now permanently increased by 10, Your total health is now {0}'
                  .format(character['hp']))
        if user_choice == '2':
            character['damage'] += 10
            print('\nAll attacks now have a +10 attack on top of their normal stats, beware enemy defences, they may'
                  ' still defend against you, your total attack is now {0}'.format(character['damage']))
        if user_choice == '3':
            character['defence'] += 10
            print('\nAll incoming attacks are now reduced by 10!, your total defence is now {0}'
                  .format(character['defence']))

    return character


def main():
    main()


if __name__ == '__main__':
    main()
