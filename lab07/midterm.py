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


def main():
    """
    Drive the program.

    Tests the function in this module.
    """


if __name__ == "__main__":
    main()
