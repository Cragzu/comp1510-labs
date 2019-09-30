"""
Module containing a function to mix two primary colours into a secondary colour.
"""


def colour_check(first_colour, second_colour, third_colour, first_check, second_check, first_result, second_result):
    """
    Check whether the two colour inputs are primary and combine to create a secondary colour.

    :precondition: all inputs must be strings
    :precondition: first_colour, second_colour, and third_colour must be the three primary colours
    :postcondition: function will return a secondary colour or False if inputs are invalid
    :param first_colour: a string with the first primary colour to check against, the first input should always be this
    :param second_colour: a string with a possible second primary colour
    :param third_colour: a string with the other possible second primary colour
    :param first_check: a string, the first input to check whether it is the colour
    :param second_check: a string, the second input to check whether it is the colour
    :param first_result: a string, the expected result of the first and second colours (secondary colour)
    :param second_result: a string, the expected result of the first and third colours
    :return: a string containing one of the two results, or False if the colours are invalid
    """
    if first_check == first_colour:
        if second_check == second_colour:
            return first_result
        elif second_check == third_colour:
            return second_result

    return False


def colour_mixer():
    """
    Find the secondary colour created by mixing the two given primary colours.

    Gets the two strings as user input and passes them into the helper function in both possible positions.

    If the whole function has been executed with no return, the colours were invalid. Returns a helpful error message.

    :precondition: first_colour must be a string, and should be a primary colour
    :precondition: second_colour must be a string, and should be a primary colour different from first_colour
    :postcondition: find the secondary colour created by mixing the given primary colours
    :return: a string containing the created secondary colour, or an error message if the input was invalid
    """
    first_input = input("Enter a primary colour: ")
    second_input = input("Enter another primary colour: ")

    mixed_colour = colour_check("red", "yellow", "blue", first_input, second_input,
                                "orange", "purple")
    if mixed_colour:  # if the function returns a colour, not False
        return mixed_colour

    mixed_colour = colour_check("red", "yellow", "blue", second_input, first_input,
                                "orange", "purple")
    if mixed_colour:
        return mixed_colour

    # if red is not one of the colours, yellow must be one of the colours for it to be valid
    mixed_colour = colour_check("yellow", "blue", "red", first_input, second_input,
                                "green", "orange")
    if mixed_colour:
        return mixed_colour

    mixed_colour = colour_check("yellow", "blue", "red", second_input, first_input,
                                "green", "orange")
    if mixed_colour:
        return mixed_colour

    return "The entered colours were invalid. Please enter two different primary colours (red, yellow, or blue)."


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    print(colour_mixer())


if __name__ == "__main__":
    main()


'''
Get two strings representing primary colours, create functions that go through a sequence of if statements to find 
the secondary colour they will mix into and print it; or print an error message if the input is invalid.

    red + yellow = orange, red + blue = purple, blue + yellow = green

Computational thinking:
    Decomposition: First consider all cases when one colour exists, then move on to the other. Make helper functions
    that will allow this program to work as efficiently as possible using only the basics of Python.
    Pattern matching: Noticing that if red does not exist, the only possible options are yellow and blue. Don't bother
    repeating code by checking things twice.
'''
