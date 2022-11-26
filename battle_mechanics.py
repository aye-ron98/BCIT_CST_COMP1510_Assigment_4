"""
Battle_mechanics.py

functions related to fighting
- character movies
- enemy moves
- leveling
- damage
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


def check_for_challenges(character, board):
    if board[(character['location X'], character['location Y'])] == 'empty room':
        return False
    else:
        return True


def execute_challenge_protocol(character, board):
    x_y_coordinate = (character['location X'], character['location Y'])
    if board[x_y_coordinate] == 'light challenge':
        return easy_challenge(character)
    elif board[x_y_coordinate] == 'medium challenge':
        return medium_challenge(character)
    elif board[x_y_coordinate] == 'hard challenge':
        return hard_challenge(character)


def easy_challenge(character):
    answers = [1, 2, 3, 4]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    answer = str(input('what is 1 + 1?: '))

    if answer != '2':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character


def medium_challenge(character):
    answers = [1, 2, 3, 4]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    answer = str(input('what is 1 + 2?: '))

    if answer != '3':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character


def hard_challenge(character):
    answers = [5, 10, 15, 20]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    answer = str(input('what is 5 + 5?: '))

    if answer != '10':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character


def main():
    main()


if __name__ == '__main__':
    main()
