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
    :postcondition: an int representing the total score of all dice rolls will be returned
    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :return: a random positive int within the calculated range
    """

    if number_of_rolls < 1 or number_of_sides < 1:  # make sure that ints are positive
        return 0

    return random.randint(number_of_rolls, number_of_sides * number_of_rolls)  # a random int within these parameters


def create_name(length):
    """
    Generate a capitalized string of random letters.

    Get a random sample from a string containing all 26 letters, concatenate it into a string, and capitalize it.

    :precondition: length should be a positive int, else None will be returned
    :postcondition: a capitalized name containing the given number of random letters will be returned
    :param length: a positive int
    :return: a string of the given length
    """
    if length < 1:  # length must be positive
        return None

    name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', length))  # select random letters and create a string
    return name.capitalize()  # capitalize first letter of the name


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """
    print(roll_die(3, 6))
    print(roll_die(3, 6))
    print(roll_die(5, 20))
    print(roll_die(-1, 6))

    print(create_name(5))
    print(create_name(5))
    print(create_name(3))
    print(create_name(-1))


if __name__ == "__main__":
    main()
