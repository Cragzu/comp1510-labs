"""
Module to calculate the number of paint cans needed to paint a room.
"""
import math


def main():
    """
    Calculate the number of cans of paint needed given dimensions of a room and number of coats.

    Declares const COVERAGE, a 4 litre can of paint covers 400 square feet

    Prompts user for length, width, and height of the room. Prompts for number of coats of paint to apply.

    Calculates the total surface area to be painted in square feet, stores in surface_area (don't paint the floor).

    Multiplies surface_area by number of coats, stores in coverage_needed. Divides coverage_needed by COVERAGE const,
    stores in cans_of_paint_required.

    Prints out the exact float and an int containing the rounded up float (number needed to actually buy).

    :precondition: given inputs must be numbers
    :postcondition: returns the correct number of cans of paint needed based on the dimensions and number of coats
    :return: an int containing the number of required paint cans
    """
    COVERAGE = 400

    length = int(input("Enter the length of the room: "))
    width = int(input("Enter the width of the room: "))
    height = int(input("Enter the height of the room: "))
    coats = int(input("How many coats do you want to apply?: "))

    first_wall_area = length * height
    second_wall_area = width * height
    top_area = length * width

    surface_area = (first_wall_area * 2) + (second_wall_area * 2) + top_area  # calculate area, ignoring the floor
    coverage_needed = surface_area * coats
    cans_of_paint_required = coverage_needed / COVERAGE

    # should round up as one cannot buy only a portion of a can of paint
    print("The estimated amount of cans needed to paint this room is", cans_of_paint_required)
    print("So, you will need to buy", math.ceil(cans_of_paint_required), "cans.")


if __name__ == "__main__":
    main()
