"""Module with function to test"""


def generator(start: int, finish: int) -> list[int]:
    """
    The function creates a list of numbers
    :param start: start of sequence
    :param finish: end of sequence
    :return: list of numbers
    """
    return list(range(min(start, finish), max(start, finish)+1))
