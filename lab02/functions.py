"""
Module containing four basic functions.
"""


def format_name(first_name, last_name):
    """
    Format a given first and last name to proper English grammar.

    Removes excess whitespace, capitalizes only the first letter of each word, and combines the two names separated
    by one space.

    :param first_name: a string
    :param last_name: a string
    :precondition: first_name and last_name must be strings
    :postcondition: returns a string that is the properly formatted name
    :return: a concatenated string
    """
    first_name = first_name.strip()
    first_name = first_name.capitalize()

    last_name = last_name.strip()
    last_name = last_name.capitalize()
    return first_name + " " + last_name


def tripler(parameter):
    """
    Print the given parameter thrice sequentially.

    Converts the data to a string and returns it three times in a row.

    :param parameter: some data of any type
    :precondition: input must be given
    :postcondition: returns a tripled string
    :return: a concatenated string which is the param repeated three times
    """
    return str(parameter) * 3


def this_year():
    """
    Perform some interesting mathematical calculations that resolve to 2019, the current year.

    :precondition: none
    :postcondition: returns the number 2019
    :return: the int 2019
    """
    return ((250 * 4) * 2) + (30 / 3) + (11 - 2)  # resolves to 2019


def base_conversion():
    """
    Convert a base 10 number into a four-digit number of another base.

    Gets the destination base from the user and calculates the maximum possible four-digit number.

    Gets the desired number to convert from the user, with an error case if the input is over the maximum
    acceptable value.

    Performs the conversion calculations by getting the remainder of the given number divided by the destination base,
    adding it to a string, then updating the number to the quotient. Repeats four times in a for loop.

    Converts the finished string into an int and prints the result.

    :precondition: destination base must be an int between 2 and 9, num_to_convert must be less than maximum_number
    :postcondition: a correctly converted int in the given base
    :return: a four-digit int equivalent to the given base-10 int in the given base.
    """
    destination_base = int(input("What base would you like to convert to? (between 2 and 9): "))
    maximum_number = (destination_base**4) - 1

    print("The maximum number that will fit into four base", destination_base, "digits is", maximum_number)
    num_to_convert = int(input("Please enter a number to convert, less than or equal to the above number: "))

    if num_to_convert > maximum_number:  # make sure input is acceptable
        print("That number is too large!")
        return

    new_num = ""

    for i in range(4):  # repeat for all four digits (could be changed here to be dynamic in size)
        new_num = str(int(num_to_convert % destination_base)) + new_num  # get the remainder, append to front of string
        num_to_convert //= destination_base  # set new_num to quotient of itself over the base

    new_num = int(new_num)  # convert back to int once finished

    print("The result in base", destination_base, "is", new_num)


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """
    print(format_name("john", "smith"))  # designed to accept a string, so only works when parameters are strings
    print(format_name("JOHN", "SMITH"))
    print(format_name(" johN ", " smitH "))

    print(tripler(3))  # works in all cases as there is a str conversion
    print(tripler("test"))
    print(tripler(""))

    print(this_year())  # works in all cases as there is no need for user input

    base_conversion()


if __name__ == "__main__":
    main()
