"""Module with function to test"""


def numbers_to_cube(numbers: list[int]) -> list[str]:
    """
    The function raises each number to a power and adds a line break to it
    :param numbers: list of numbers
    :return: list of strings
    """
    return [str(number ** 3) + "\n" for number in numbers]
