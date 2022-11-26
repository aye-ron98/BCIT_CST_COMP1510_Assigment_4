"""
world_building.py

functions related to world building
- character
- map
- enemies
"""
import random


def make_character():
    character_name = input('What is your name?: ')
    character = {'name': character_name, 'hp': 5, 'xp': 0, 'level': 1, 'location X': 0, 'location Y': 0,
                 'glow up': False, 'level cap': False, 'goal': False}
    return character


def make_board(rows, columns):
    board = {(row, column): generate_encounters() for row in range(rows + 1) for column in range(columns + 1)}
    return board


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


def describe_current_location(board, character):
    character_location = (character['location X'], character['location Y'])
    print(board[character_location])


def validate_move(move):
    if move:
        return True


def main():
    main()


if __name__ == '__main__':
    main()
