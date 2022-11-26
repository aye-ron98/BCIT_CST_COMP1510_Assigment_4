"""
Battle_mechanics.py

functions related to fighting
- character movies
- enemy moves
- leveling
- damage
"""


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
