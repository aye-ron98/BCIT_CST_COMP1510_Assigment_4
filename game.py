"""
Aron Zhang
A01280188
"""
import battle_mechanics
import world_building
import movment
import character_condition


def game():  # called from main
    rows = 5
    columns = 5
    board = world_building.make_board(rows, columns)
    character = world_building.make_character()
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        world_building.describe_current_location(character)
        movment.get_user_choice(character)
        world_building.describe_current_location(character)
        battle_mechanics.execute_challenge_protocol(character, board)
        if character_condition.character_has_leveled(character):
            character_condition.execute_glow_up_protocol(character)
            # achieved_goal = check_if_goal_attained(character)
        if character['level cap']:
            battle_mechanics.execute_final_boss(character)
            if character['hp'] > 0:
                achieved_goal = True
        if character_condition.character_health(character):
            break
        else:
            continue
    if achieved_goal:
        print('Congragulations {}, you beat the game!'.format(character['name']))
    else:
        print('Better luck next time {}! You died.'.format(character['name']))


def main():
    game()


if __name__ == '__main__':
    main()
