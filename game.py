"""
Aron Zhang
A01280188
"""
import battle_mechanics
import world_building
import movment


def game():  # called from main
    rows = 5
    columns = 5
    board = world_building.make_board(rows, columns)
    character: object = world_building.make_character()
    achieved_goal = False
    world_building.describe_current_location(board, character)
    while not achieved_goal:
        # Tell the user where they are
        direction = movment.get_user_choice(character)
        valid_move = movment.validate_move(direction)
        if valid_move:
            # move_character(character)
            world_building.describe_current_location(board, character)
            there_is_a_challenge = battle_mechanics.check_for_challenges(character, board)
            if there_is_a_challenge:
                battle_mechanics.execute_challenge_protocol(character, board)
            if battle_mechanics.character_has_leveled(character):
                battle_mechanics.execute_glow_up_protocol(character)
                # achieved_goal = check_if_goal_attained(character)
            if battle_mechanics.character_health(character):
                break
            else:
                continue
        else:
            # Tell the user they can’t go in that direction
            print('better luck next time! You died')
            # Print end of game stuff like congratulations or sorry you died


def main():
    game()


if __name__ == '__main__':
    main()
