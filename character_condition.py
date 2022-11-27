"""
character_condition.py

functions that check character status
- level
- health
-xp
"""


def character_has_leveled(character: dict) -> dict:
    """
    Updates values of character dictionary.

    :param character: a dictionary.
    :precondition character: must contain keys 'level', 'xp', 'hp', glow up'
    :precondition character: values must be integer
    :return: an updated dictionary character
    """
    if character['level'] == 1:
        if character['xp'] == 3:
            character['level'] = 2
            character['xp'] = 0
            character['hp'] = 50
            character['glow up'] = True
    elif character['level'] == 2:
        if character['xp'] == 5:
            character['level'] = 3
            character['xp'] = 0
            character['hp'] = 100
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
    """
    if character['hp'] == 0:
        return True
    else:
        return False


def execute_glow_up_protocol(character: dict) -> dict:
    """
    Update character dictionary values

    :param character: a dictionary
    :precondition character: must contain keys 'glow up', 'damage', 'defence' 'hp'
    :postcondition: will update character values pending user input
    :return: the dictionary character
    """
    if character['glow up']:
        print('\nCongratulations! you have leveled up!'
              'choose an upgradable from the following!\n')
        character['glow up'] = False
        upgradeables = ['+10 health', '+10 base damage', '+10 base defence']
        for choice, item in enumerate(upgradeables, 1):
            print(item, ': ', choice)

        user_choice = str(input('\nwhat would you like?: '))

        if user_choice == '1':
            print('\nYour health is now permanently increased by 10, Your total health is now {}'
                  .format(character['hp'] + 10))
            character['hp'] += 10
        if user_choice == '2':
            print('\nAll attacks now have a +10 attack on top of their normal stats, beware enemy defences, they may '
                  'still defend against you!')
            character['damage'] += 10
        if user_choice == '3':
            print('\nAll incoming attacks are now reduced by 10!')
            character['defence'] += 10

    print(character)
    return character


def main():
    main()


if __name__ == '__main__':
    main()
