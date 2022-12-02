"""
movement.py

functions related to moving around the map
"""


def get_user_choice(player: dict) -> dict:
    """
    Take user input modifies character dictionary.

    Prints an enumerated list of options for user to choose from.
    :param player: a dictionary
    :preconditon character: must contain key 'location' and 'exit'
    :precondition character: location value must tuple length 2 comprised of integer data type
    :precondition character: 'exit' key must be boolean value False
    :postcondition: modifies and returns player dictionary
    :return: the character dictionary
    """
    directions = [('move north', (-1, 0)), ('move east', (0, +1)), ('move south', (+1, 0)), ('move west', (0, -1)),
                  ('Quit', '_')]
    for choice, direction in enumerate(directions, 1):
        print(choice, direction[0])

    while True:
        move = validate_move(1, 5)
        exit_game(move, player)
        if player['exit']:
            return player
        potential_move = validate_location(int(move), directions, player)
        if 0 <= potential_move[0] <= 4 and 0 <= potential_move[1] <= 4:
            player['location'] = potential_move
            return player
        else:
            print('{} you cannot go that way'.format(player['name']))


def validate_move(lower_bound: int, upperbound: int) -> str:
    """
    Takes user input and validates it is within the range of upper and lower bound before retuning it.
    Asks user to try again if input is not in a valid range. Will convert upper and lower bound to string.

    :param lower_bound: an integer
    :param upper upperbound: an integer
    :precondition upperbound: must be greater than lower bound
    :postcondition: if user input is in [lower_bound, upper_bound] will return user input
    :return: user input as a string
    """

    while True:
        try:
            user_input = int(input('\nWhat is your choice?: \n'))
        except ValueError:
            print('That is not an option, try again!')
            continue
        else:
            if lower_bound <= user_input <= upperbound:
                return str(user_input)
            else:
                print('That is not an option, try again!')
                continue


def validate_location(choice: int, options: list, player: dict) -> tuple:
    """
    Sum individual values two tuples together. Tuple values must be integer

    :param choice: a nonzero positive integer
    :param options: a list of length 2
    :param player: a dictionary
    :preconditon choice: must be within range [0 , len(options)]
    :precondition options: second item must be tuple of length 2, contents must be integers
    :precondition player: must contain key 'location' value must be tuple of length 2, contents must be integers
    :postcondition: will sum individual values two tuples together
    :return: a tuple length 2
    >>> validate_location(1, [('move south', (0, -1)), ('move north', (1, 0))], {'location': (3, 4)})
    (3, 3)
    >>> validate_location(2, [('move south', (0, -1)), ('move north', (1, 0))], {'location': (3, 4)})
    (4, 4)
    """
    new_coordinates = options[choice - 1][1]
    player_coordinates = player['location']
    updated_coordinates = [new_coordinates + player_coordinates for
                           new_coordinates, player_coordinates in zip(new_coordinates, player_coordinates)]
    return tuple(updated_coordinates)


def exit_game(choice: str, player: dict) -> dict:
    """
    Evaluate choice and modify player dictionary if choice is '5'. Returns modified dictionary.

    :param choice: a string
    :param player: a dictionary
    :precondition player: must contain key 'exit'
    :precondition player: key 'exit' must be boolean False
    :postcondition: if choice == '5' will modify player['exit'] to True
    :postcondition: if choice != '5' will return player without modifications
    :return: the player dictionary
    >>> yes_exit = {'exit': False}
    >>> exit_game('5', yes_exit)
    {'exit': True}
    >>> no_exit = {'exit': False}
    >>> exit_game('3', no_exit)
    {'exit': False}

    """
    if choice == '5':
        player['exit'] = True
        return player
    else:
        return player


def main():
    main()


if __name__ == '__main__':
    main()
