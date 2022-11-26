"""
movement.py

functions related to moving around the map
"""


def get_user_choice(character):
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

    print(character)
    return character, True


def validate_move(move):
    if move:
        return True


def main():
    main()


if __name__ == '__main__':
    main()
