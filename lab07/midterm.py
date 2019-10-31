"""
Module containing functions from the 1510 midterm exam.
"""
import random


def list_tagger(batch):
    """
    Tag the given list batch with its length.

    Calculate the length of the list batch and return the same list with the length (int) inserted at the front.
    :param batch: a list
    :return: a list equal to batch with the length at index 0

    >>> list_tagger(['a', 'b', 'c', 'd'])
    [4, 'a', 'b', 'c', 'd']
    >>> list_tagger([])
    [0]
    """
    batch.insert(0, len(batch))
    return batch


def cutoff(num_list, divisor):
    """
    Determine the number of integers in a given list that are a multiple of the given number.

    :precondition: num_list must only contain integers
    :param num_list: a list of ints
    :param divisor: an int
    :return: an int representing the count of numbers in num_list that are a multiple of divisor

    >>> cutoff([2, 3, 4, 8], 2)
    3
    """
    count = 0
    for i in num_list:
        if i % divisor == 0:
            count += 1
    return count


def prepender(str_list, new_str):
    """
    Prepend each string in a given list with the given string.

    Add new_str to the beginning of every string in str_list, modifying the existing list.

    :precondition: str_list must only contain strings
    :param str_list: a list of strings
    :param new_str: a string
    :return: none
    """
    for i in range(len(str_list)):
        str_list[i] = new_str + str_list[i]  # add new_str to the front of every string in str_list
    return


def name_list():
    """
    Create a dictionary containing a series of user-entered names, grouped by their length.

    Repeatedly prompt the user to enter a name, exiting the loop when they enter 'quit'. For each name, check if the
    dictionary already contains a key for that name's length. If it does, add the name to its value (a list). If it
    doesn't, create a new key-value pair with the length as the key and a list containing the name as the value.

    :return: a dictionary containing key-value pairs of ints and lists of strings representing the name list.
    """
    names = {}
    user_exit = False

    while not user_exit:
        name = input('Please enter a name, or enter quit to finish: ')
        if name.lower() == 'quit':
            user_exit = True

        else:
            if len(name) in names.keys():
                names[len(name)].append(name)  # add name to existing dict length entry
            else:
                names[len(name)] = [name]  # start new dict length entry

    return names


def multiples_of_3(upper_bound):
    """
    Calculate the sum of all positive multiples of 3 below the given upper_bound.

    :precondition: upper_bound must be a positive int
    :param upper_bound: an int
    :return: an int representing the sum of every multiple of 3 below upper_bound

    >>>multiples_of_3(10)
    18
    """
    multiple_sum = 0
    for i in range(upper_bound):
        if i % 3 == 0:
            multiple_sum += i

    return multiple_sum


def die_tallies():
    """
    Tabulate the number of times each side of a die was rolled in a given number of rolls.

    Get user input for number of sides of the die and number of rolls to perform. Create a dict with int keys
    representing each side of the die. Roll the die the specified number of times, and keep track of how many times
    each side was rolled using the dict.

    :return: none, uses print to display the result
    """
    sides = int(input('How many sides should the die have?: '))
    rolls = int(input('Roll how many dice?: '))

    tally = {i: 0 for i in range(1, (sides + 1))}  # initialize dict with keys for every side of the die

    progress = 0
    while progress < rolls:  # roll dice and tick up tallies for each instance of a side
        roll = random.randint(1, sides)
        tally[roll] += 1
        progress += 1

    for k, v in tally.items():
        print(k, ': ', v)


def main():
    """
    Drive the program.

    Tests the function in this module.
    """


if __name__ == "__main__":
    main()
