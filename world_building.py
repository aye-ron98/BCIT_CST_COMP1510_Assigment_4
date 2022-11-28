"""
world_building.py

functions related to world building
- character
- map
- enemies
"""
import random


def make_character() -> dict:
    """
    Make a character dictionary

    :precondition: user must enter a character name
    :postcondition: will construct a dictionary representing game character
    :return: a dictionary of 11 items
    """
    character_name = input('What is your name?: ')
    character = {'name': character_name, 'hp': 30, 'xp': 0, 'level': 1, 'location': (4, 0), 'exit': False,
                 'glow up': False, 'level cap': False, 'goal': False, 'damage': 0, 'defence': 0}
    return character


def make_board(rows: int, columns: int) -> dict:
    """
    Create a board for size rows x columns.

    :param rows: an integer
    :param columns: an integer
    :precondition rows: must be a nonzero positive integer
    :precondition columns: must be a positive integer
    :postcondition: will generate a dictionary of tuple keys consisting of (row, column)
    :postcondiion: values are generated by a helper function
    :return: a dictionary of size row x column
    """
    board = {(row, column): generate_encounters() for row in range(rows + 1) for column in range(columns + 1)}
    return board


def generate_encounters() -> str:
    """
    Generate encounters randomly using random.randint

    :return: string empty room or light challenge
    """
    dice_roll = random.randint(1, 2)

    if dice_roll == 1:
        return 'light challenge'
    if dice_roll == 2:
        return 'light challenge'


def describe_current_location(character: dict) -> None:
    """
    Print the game board and character.

    :param character: a dictionary
    :precondition character: keys location X and location Y with values is required of character dictionary
    :precondition: values must be positive integers
    :postcondition: will print a board of len(board.keys()) x len(board.keys())
    """

    for x in range(0, 5):
        print('\n') if x != 0 else print(end='')
        for y in range(0, 5):
            if (x, y) == character['location']:
                print('(!)  ', end='')
            else:
                print(' +   ', end='')
    print('\n')


def main():
    """
    Drives the program
    """


if __name__ == '__main__':
    main()
