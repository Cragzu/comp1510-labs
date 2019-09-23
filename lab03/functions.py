"""
Module containing two functions to roll a die and create a name.
"""
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate the result of rolling a die with a given number of sides a given number of times.

    Check to make sure the given ints are positive, else return 0 and quit the function.

    The range the result can be in is the number of rolls (rolling a 1 each time) up to the number of sides
    multiplied by the number of rolls (rolling the maximum value each time). Generate a random int within that range.

    :precondition: number_of_rolls and number_of_sides should be positive ints, else 0 will be returned
    :postcondition: a random int within the calculated range will be returned
    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :return: an int representing the total score of all dice rolls
    """

    if number_of_rolls < 1 or number_of_sides < 1:  # make sure that ints are positive
        return 0

    return random.randint(number_of_rolls, number_of_sides * number_of_rolls)


print(roll_die(3, 6))