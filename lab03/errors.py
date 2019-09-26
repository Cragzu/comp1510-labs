"""
Module containing code meant to intentionally throw some Python errors for demonstration purposes.
"""


def main():
    """
    Drive the program.

    Create errors in Python.
    """

    print(1/0)  # zero division error: can't divide by 0

    print("four"[4])  # index error: string index out of range
    print("hi"[-6])

    print(4 + "4") # type error: variables are not the same type
    print(5.0 ** 'a')


if __name__ == "__main__":
    main()
