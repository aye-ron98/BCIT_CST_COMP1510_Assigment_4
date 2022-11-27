"""
movement.py

functions related to moving around the map
"""


def get_user_choice(character: dict) -> dict:
    """
    Take user input and verify input is in range [0, 4]. Updates relevant character values upon verification.

    :param character: a dictionary
    :preconditon character: must contain key 'location X' and 'location Y'
    :preconditon character: values must be positive integers
    :postcondition: updates relevant character keys
    :return: the character dictionary
    """
    directions = ['move south', 'move east', 'move north', 'move west']
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

    return character


def main():
    main()


if __name__ == '__main__':
    main()
