"""Module with function to test"""


def mult_numbers(numbers: list[int]) -> int:
    """
    The function multiplies numbers with each other
    :param numbers: list of numbers
    :return: product result
    """
    result = 1
    for number in numbers:
        result *= number
    return result
