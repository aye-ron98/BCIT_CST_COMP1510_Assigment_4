"""
scenarios.py

functions that relate to non battle scenarios the players can experience.
"""
import random
import movment


def treasure(player: dict) -> dict:
    """
    Modify player dictionary positively with a randomly selected number.

    :param player: a dictionary
    :precondition player: must have key 'damage'
    :precondition player: damage must be a positive integer
    :postcondition: increments 'damage' key equivalent to randomly picked number in range [3, 7]
    :return: the player dictionary
    """
    treasure_picker = random.randint(0, 4)
    treasures = ['stick', 'sword', 'battering ram', 'trumpet', 'flag pole']
    print("\nIt's your luck day!, You stumble across an armory, you leave with a {0}. ALl damage is now increased "
          "by +{1}."
          .format(treasures[treasure_picker], (treasure_picker + 3)))
    player['damage'] += treasure_picker + 3

    return player


def add_health(player: dict) -> dict:
    """
    Modify player dictionary with a randomly selected number.

    :param player: a dictionary
    :precondition player: must have key 'hp'
    :precondition player: hp must be a positive integer
    :postcondition: increments 'hp' key equivalent to randomly picked number in range [1, 10]
    :return: the player dictionary
    """
    health_gain = random.randint(1, 10)
    print('\nYou come across a hospital, advertisers feed you a lot of multivitamins, you gain {} health'
          .format(health_gain))
    player['hp'] += health_gain

    return player


def add_defense(player: dict) -> dict:
    """
    Modify player dictionary with a randomly selected number.

    :param player: a dictionary
    :precondition player: must have key 'defence'
    :precondition player: defence must be a positive integer
    :postcondition: increments 'defence' key equivalent to randomly picked number in range [0, 4]
    :return: the player dictionary
    """
    defence_gain = random.randint(0, 4)
    shields = ['stick shield', 'aluminum shield', 'styrofoam shield', 'imaginary shield', 'kevelar vest']
    print('\nYou stubmle across an antique shop and leave with a {0}, all attacks are now reduced by {1}'
          .format(shields[defence_gain], defence_gain))
    player['defence'] += defence_gain
    return player


def puzzle(player: dict) -> dict:
    """
    Modify player dictionary depending on user input.

    :param player: a dictionary
    :precondition player: must have key 'xp'
    :precondition player: xp must be a positive integer
    :postcondition: increments 'xp' key by one if user input == 1
    :postcondition: returns unmodified player dictionary if user input != 1
    :return: the player dictionary
    """
    print('\nA stander asks you:\n I’m tall when I’m young, and I’m short when I’m old. What am I?')
    answers = ['a candle', 'a human', 'a tree', 'an eraser']

    for choice, answer in enumerate(answers, 1):
        print(choice, ': ', answer)
    user_input = movment.validate_move(1, 4)
    if user_input == '1':
        player['xp'] += 1
        print('Correct! You gain 1xp, you are now at {0}'.format(player['xp']))
        return player
    elif '2' <= user_input <= '4':
        print('The right answer was a candle! You lave with nothing')


def riddle(player: dict) -> dict:
    """
    Modify player dictionary depending on user input.

    :param player: a dictionary
    :precondition player: must have key 'xp'
    :precondition player: xp must be a positive integer
    :postcondition: increments 'xp' key by one if user input == 1
    :postcondition: returns unmodified player dictionary if user input != 1
    :return: the player dictionary
    """
    print('\nA stander asks you:\n What month of the year has 28 days?')
    answers = ['all of them', 'february', 'december', "what's a month?"]

    for choice, answer in enumerate(answers, 1):
        print(choice, ': ', answer)
    user_input = movment.validate_move(1, 4)
    if user_input == '1':
        print('Correct! You gain 1xp, you are now at {0}'.format(player['xp'] + 1))
        player['xp'] += 1
        return player
    elif '2' <= user_input <= '4':
        print('The right answer was a all of them! You lave with nothing')
