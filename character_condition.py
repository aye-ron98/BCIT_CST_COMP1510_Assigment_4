"""
character_condition.py

functions that check character status
- level
- health
-xp
"""


def character_has_leveled(character):
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


def character_health(character):
    if character['hp'] == 0:
        return True
    else:
        return False


def execute_glow_up_protocol(character):
    if character['glow up']:
        print('\nCongratulations! you have leveled up!'
              'choose an upgradable from the following!\n')
        character['glow up'] = False
        upgradeables = ['+10 health', '+10 base damage', '+10 base defence']
        for choice, item in enumerate(upgradeables, 1):
            print(item, choice)

        user_choice = str(input('what would you like?'))

        if user_choice == 1:
            character['hp'] += 10
        if user_choice == 2:
            character['damage'] += 10
        if user_choice == 3:
            character['defence'] += 10

    return character


def main():
    main()


if __name__ == '__main__':
    main()
