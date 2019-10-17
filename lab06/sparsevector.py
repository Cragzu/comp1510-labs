"""
Module containing a function that adds two sparse vectors.

If we were to create a function that returns the length of a sparse vector, it would not work with the current way we
are storing vectors. This is because we only store indices that have a non-0 value at them, and we don't know how
many 0s are in the vector. To do this, we would need to ask the team lead how many 0s are in the sparse vector.
We could then add that number to the length of the dict representing the sparse vector to find its length (the number
of dimensions it has).
"""


def sparse_add(first_vec, second_vec):
    """
    Add together two dictionaries representing sparse vectors by combining the element-wise sum of their elements into
    a new dictionary.

    Iterate through the keys of the first dict, and if the key is present in the second dict, add the values and insert
    the pair into the new dict.

    Iterate through the keys of the first and second dict, and for each key that is not present in the new dict, insert
    that pair into the new dict. (these are pairs that are only present in one of the two dicts)

    If any of the additions resolved to 0, remove that pair from the dict.

    :precondition: the two sparse vectors must have the same number of dimensions
    :param first_vec: a dictionary representing a sparse vector
    :param second_vec: a dictionary representing a sparse vector
    :return: a dictionary containing the sum of the two param dictionaries
    """
    sum_vec = {}
    for key, value in first_vec.items():  # add values with the same key
        if key in second_vec.keys():
            sum_vec[key] = (first_vec[key] + second_vec[key])

    for key, value in first_vec.items():  # include keys only present in the first vector
        if key not in sum_vec.keys():
            sum_vec[key] = first_vec[key]

    for key, value in second_vec.items():  # include keys only present in the second vector
        if key not in sum_vec.keys():
            sum_vec[key] = second_vec[key]

    zeros = []
    for key, value in sum_vec.items():  # remove any kv pairs with value of 0
        if value == 0:
            zeros.append(key)

    for i in zeros:
        del sum_vec[i]
             
    return sum_vec
