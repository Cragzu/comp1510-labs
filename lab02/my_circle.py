"""
Module to calculate the circumference and area of a circle given its radius.
"""


def main():
    """
    Calculate attributes of a circle given its radius.

    Sets const PI as 3.14159, initializes var radius as 0

    Prompts user input for a radius value, converts to a float for accurate calculations

    Calculates the circumference and area of the circle and displays the values.

    Creates a new float double_radius that is twice the original radius. Calculates the new area and circumference
    using the double radius.

    Uses division to determine how many times the area and circumference increase when radius doubles, displays
    these values.

    :precondition: given value must be a number
    :postcondition: returns values of different attributes of circles using the given radius value
    :return: floats representing the area and circumference of a circle given its base radius and doubled radius
    """
    PI = 3.14159
    radius = 0.0

    radius = float(input("Enter the radius of a circle: "))
    double_radius = radius*2.0

    circumference = 2.0 * PI * radius
    area = PI * (radius**2.0)

    print("The circumference of the circle is:", circumference)
    print("The area of the circle is:", area)

    increased_circumference = 2.0 * PI * double_radius
    increased_area = PI * (double_radius**2.0)

    print("The circumference of the circle when the radius is doubled is:", increased_circumference)
    print("The area of the circle when the radius is doubled is:", increased_area)

    print("The circumference increases by", increased_circumference/circumference, "times when the radius is doubled.")
    print("The area increases by", increased_area/area, "times when the radius is doubled.")


if __name__ == "__main__":
    main()
