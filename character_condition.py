"""
character_condition.py

functions that check character status
- level
- health
-xp
"""


def character_has_leveled(character):
    if character['level'] == 1:
        if character['xp'] == 5:
            character['level'] = 2
            character['xp'] = 0
            character['hp'] = 10
            character['glow up'] = True
    elif character['level'] == 2:
        if character['xp'] == 10:
            character['level'] = 3
            character['xp'] = 0
            character['hp'] = 15
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
        character['glow up'] = False
        print('glow up, level up')
    return character


def main():
    main()


if __name__ == '__main__':
    main()
