"""Module with function to test"""


def expression(number: int) -> int:
    """
    The function evaluates the result of the expression
    :param number: number
    :return: result of expression
    """
    if number < -5:
        return number ** 2 - 5
    elif -5 <= number <= 5:
        return number * 2
    elif number > 5:
        return number ** 2 + 5
