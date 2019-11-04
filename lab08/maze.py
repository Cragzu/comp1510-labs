"""
A module to simulate a small version of a Single User Dungeon.
"""


def input_loop(prompt, valid_choices):
    """
    Prompt the user repeatedly for a choice until a valid input is entered.

    :param prompt: a string describing what the user can choose from
    :param valid_choices: a list containing chars representing the available choices
    :precondition: the valid_choices list must contain only length-1 strings of capital letters
    :return: a char representing the user's choice
    """
    valid_input = False
    while not valid_input:
        user_choice = (input(prompt)).upper()

        if user_choice not in valid_choices:  # check if input is valid
            print('Sorry, that wasn\'t a valid input. Please try again.')

        else:
            valid_input = True

    return user_choice


def valid_movements(current_position):
    """
    Determine which movements can be taken based on the user's position in the game board.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: a list containing two lists with only the valid options

    >>> valid_movements([2, 2])
    [['(N)orth', '(S)outh', '(E)ast', '(W)est'], ['N', 'S', 'E', 'W']]

     >>> valid_movements([0, 0])
    [['(S)outh', '(E)ast'], ['S', 'E']]
    """
    instructions = ['(N)orth', '(S)outh', '(E)ast', '(W)est']  # for printing available options
    directions = ['N', 'S', 'E', 'W']

    if current_position[0] == 0:  # against north wall, cannot move north
        directions.remove('N')
        instructions.remove('(N)orth')

    if current_position[0] == 4:  # against south wall, cannot move south
        directions.remove('S')
        instructions.remove('(S)outh')

    if current_position[1] == 0:  # against west wall, cannot move west
        directions.remove('W')
        instructions.remove('(W)est')

    if current_position[1] == 4:  # against east wall, cannot move east
        directions.remove('E')
        instructions.remove('(E)ast')

    return [instructions, directions]


def move(current_position):
    """
    Update the character's position on the game board.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: an updated version of current_position with one of the ints incremented
    """

    prompt_list = valid_movements(current_position)[0]

    if len(prompt_list) < 4:  # user is against a boundary of the map
        print('You\'ve reached a dead end! Best not to continue past here or you will likely be eaten by a grue...')

    prompt = 'Which direction to move? You can go: '
    for i in prompt_list:
        prompt += (i + ' ')

    direction = input_loop(prompt, valid_movements(current_position)[1])

    if direction == 'N':
        current_position[0] -= 1

    elif direction == 'S':
        current_position[0] += 1

    elif direction == 'E':
        current_position[1] += 1

    elif direction == 'W':
        current_position[1] -= 1

    return current_position


def game():
    """
    Run the game.

    Continuously loop the gameplay until the user wins.

    :return: none
    """
    board = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
             [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
             [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
             [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
             [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]]  # 5x5 matrix
    character = [0, 0]  # starting coordinates

    victory_reached = False
    while not victory_reached:

        print('You are at coordinates:', board[character[0]][character[1]])
        move(character)

        if character == [4, 4]:  # quit
            victory_reached = True

        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    print('You found the exit! You win!\nThank you for playing.')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
