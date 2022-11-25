"""
Aron Zhang
A01280188
"""
import random


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character: object = make_character()
    achieved_goal = False
    describe_current_location(board, character)
    while not achieved_goal:
        # Tell the user where they are
        direction = get_user_choice(character)
        valid_move = validate_move(direction)
        if valid_move:
            # move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(character, board)
            if there_is_a_challenge:
                execute_challenge_protocol(character, board)
            if character_has_leveled(character):
                execute_glow_up_protocol(character)
                # achieved_goal = check_if_goal_attained(character)
        # else:
        # Tell the user they can’t go in that direction
        # Print end of game stuff like congratulations or sorry you died


def get_user_choice(character):
    directions = ['move north', 'move east', 'move south', 'move west']
    for choice, direction in enumerate(directions, 1):
        print(choice, direction)

    while True:
        move = input('What direction would you like to move?')
        if move == '1' and character['location X'] < 4:
            character['location X'] += 1
            break
        elif move == '2' and character['location Y'] < 4:
            character['location Y'] += 1
            break
        elif move == '3' and character['location X'] > 0:
            character['location X'] -= 1
            break
        elif move == '4' and character['location Y'] > 0:
            character['location Y'] -= 1
            break
        else:
            print('You cannot go that way')
            continue

    print(character)
    return character, True


def make_character():
    character_name = input('What is your name?: ')
    character = {'name': character_name, 'hp': 5, 'xp': 0, 'level': 1, 'location X': 0, 'location Y': 0,
                 'glow up': False, 'level cap': False, 'goal': False}
    return character


def describe_current_location(board, character):
    character_location = (character['location X'], character['location Y'])
    print(board[character_location])


def validate_move(move):
    if move:
        return True


def character_has_leveled(character):
    if character['level'] == 1:
        if character['xp'] == 5:
            character['level'] = 2
            character['glow up'] = True
    elif character['level'] == 2:
        if character['xp'] == 10:
            character['level'] = 3
            character['glow up'] = True
            character['level cap'] = True

    return character


def execute_glow_up_protocol(character):
    if character['glow up']:
        character['glow up'] = False
        print('glow up, level up')
    return character


def generate_encounters():
    dice_roll = random.randint(1, 100)

    if dice_roll < 45:
        return 'empty room'
    if dice_roll < 70:
        return 'light challenge'
    if dice_roll < 80:
        return 'medium challenge'
    if dice_roll < 101:
        return 'hard challenge'

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
    xp = character['xp']
    hp = character['hp']
    answer = str(input('what is 1 + 1?: '))

    answers = [1, 2, 3, 4]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    if answer != '2':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character


def medium_challenge(character):
    xp = character['xp']
    hp = character['hp']
    answer = str(input('what is 1 + 2?: '))

    answers = [1, 2, 3, 4]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    if answer != '3':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character

def hard_challenge(character):
    xp = character['xp']
    hp = character['hp']
    answer = str(input('what is 5 + 5?: '))

    answers = [5, 10, 15, 20]
    for choice, direction in enumerate(answers, 1):
        print(choice, direction)

    if answer != '10':
        print('wrong')
        character['hp'] -= 1
        return character
    else:
        print('correct')
        character['xp'] += 1
        return character


def make_board(rows, columns):
    board = {(row, column): generate_encounters() for row in range(rows + 1) for column in range(columns + 1)}
    return board


def main():
    game()


if __name__ == '__main__':
    main()
