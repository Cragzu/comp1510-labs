"""
Module containing functions that calculate factorials two different ways,
and determines which one is faster.
"""
import time


def timer(func):
    """
    Write the time it takes to execute a given function to a file.

    :param func: a function
    :return: None
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        # Write file output to results.txt
        with open('results.txt', 'a+') as file_object:
            file_object.write("Run time for " + func.__name__ + "(" + str(args[0]) + ") is " + str(run_time) + "\n")

    return wrapper


@timer
def factorial_iterative(num: int) -> int:
    """
    Calculate factorial using a loop.

    :param num: int
    :precondition: num must be a positive int
    :postcondition: calculates the correct factorial
    :return: the factorial of num as an int

    >>>factorial_iterative(0)
    1
    >>>factorial_iterative(1)
    1
    >>>factorial_iterative(5)
    120
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    return factorial


def factorial_recursive_helper(num: int, factorial: int) -> int:
    """
    Calculate factorial using recursion.

    :param num: int
    :param factorial: int
    :postcondition: calculates the correct factorial
    :return: the factorial of num as an int

    >>>factorial_recursive_helper(0)
    1
    >>>factorial_recursive_helper(1)
    1
    >>>factorial_recursive_helper(5)
    120
    """
    if num == 0:
        return factorial

    factorial *= num
    return factorial_recursive_helper(num - 1, factorial)


@timer
def factorial_recursive(num: int, factorial: int = 1) -> int:
    """
    Call the factorial_recursive_helper function to allow the decorator to work properly.

    :param num: int
    :param factorial: int
    :precondition: num must be a positive int
    :precondition: factorial has a default value and should not be passed a different argument
    :return: the factorial of num as an int
    """
    return factorial_recursive_helper(num, factorial)


def main():
    for i in range(1, 101):
        factorial_iterative(i)

    for i in range(1, 101):
        factorial_recursive(i)


if __name__ == "__main__":
    main()
