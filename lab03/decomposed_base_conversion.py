"""
Module containing functions to convert a number between bases.
"""


def remainder_calc(a, b):
    """
    Get the remainder left over when a is divided by b, as a string.

    :precondition: a and b must be ints, a >= b for correct output.
    :postcondition: will return a number representing the amount left over after a is divided by b.
    :param a: an int
    :param b: an int
    :return: a string representing the remainder of a over b.
    """
    return str(int(a % b))


def base_conversion():
    """
    Convert a base 10 number into a four-digit number of another base.

    Get the destination base from the user and calculates the maximum possible four-digit number.

    Get the desired number to convert from the user, with an error case if the input is over the maximum
    acceptable value.

    Perform the conversion calculations by getting the remainder of the given number divided by the destination base,
    adding it to a string, then updating the number to the quotient. Repeats four times in a for loop.

    Convert the finished string into an int and prints the result.

    :precondition: destination base must be an int between 2 and 9, num_to_convert must be less than maximum_number
    :postcondition: a correctly converted int in the given base
    :return: a four-digit int equivalent to the given base-10 int in the given base.
    """
    destination_base = int(input("What base would you like to convert to? (between 2 and 9): "))
    maximum_number = (destination_base ** 4) - 1

    print("The maximum number that will fit into four base", destination_base, "digits is", maximum_number)
    num_to_convert = int(input("Please enter a number to convert, less than or equal to the above number: "))

    if num_to_convert > maximum_number:  # make sure input is acceptable
        print("That number is too large!")
        return

    first_digit = remainder_calc(num_to_convert, destination_base)
    num_to_convert //= destination_base # set new_num to quotient of itself over the base
    print(first_digit)

    second_digit = remainder_calc(num_to_convert, destination_base)
    num_to_convert //= destination_base
    print(second_digit)

    third_digit = remainder_calc(num_to_convert, destination_base)
    num_to_convert //= destination_base
    print(third_digit)

    fourth_digit = remainder_calc(num_to_convert, destination_base)
    num_to_convert //= destination_base
    print(fourth_digit)

    new_num = int(fourth_digit + third_digit + second_digit + first_digit)  # add digits and convert back to int

    print("The result in base", destination_base, "is", new_num)


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """
    base_conversion()


if __name__ == "__main__":
    main()
