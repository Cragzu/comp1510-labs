"""
Module containing a function that adds two sparse vectors.
"""


def sparse_add(first_vec, second_vec):
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


def main():
    print(sparse_add({3: 1, 4: 2, 5: 4, 9: 5}, {3: 1, 5: 2, 9: -5}))


if __name__ == '__main__':
    main()
