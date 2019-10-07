"""
Module containing two functions to roll a die and create a name.
"""
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate the result of rolling a die with a given number of sides a given number of times.

    Check to make sure the given ints are positive, else return 0 and quit the function.

    We roll each die in succession. Generate a random number between 1 and number_of_sides for each roll.

    :precondition: number_of_rolls and number_of_sides should be positive ints, else 0 will be returned
    :postcondition: an int representing the total score of all dice rolls will be returned
    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :return: a random positive int within the calculated range
    """

    if number_of_rolls < 1 or number_of_sides < 1:  # make sure that ints are positive
        return 0

    total = 0

    for i in range(number_of_rolls):
        total += (random.randint(1, number_of_sides))

    return total


def choose_inventory(inventory, selection):
    """
    Select an assortment of items from a given list, create a sorted list containing the given number of selected items.

    :precondition: inventory should not be empty, else a warning will be returned
    :precondition: selection should be a positive int between 1 and inventory length, else a warning will be returned
    :postcondition: function will return a list of length selection containing a random sample from inventory
    :param inventory: a list representing all available items to choose from
    :param selection: a positive int less than or equal to the length of inventory representing the desired # of items
    :return: a sorted list containing a selection of items from the original inventory list
    """
    if inventory == [] and selection == 0:
        return []

    elif selection < 0:
        print("The selection cannot be a negative number!")
        return []

    elif selection >= len(inventory):  # selection is equal or longer than inventory
        if selection > len(inventory):  # warning message only when selection is longer
            print("The selection cannot be larger than the available inventory!")
        return sorted(inventory)

    else:
        return sorted(random.sample(inventory, selection))


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """
    print(choose_inventory(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3))


if __name__ == "__main__":
    main()
