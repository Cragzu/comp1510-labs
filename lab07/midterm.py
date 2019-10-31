"""
Module containing functions from the 1510 midterm exam.
"""


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
        temp_string = new_str + str_list[i]
        str_list[i] = temp_string  # todo: does this need a temp variable to work? could I reassign it in one line?
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


def main():
    """
    Drive the program.

    Tests the function in this module.
    """


if __name__ == "__main__":
    main()
