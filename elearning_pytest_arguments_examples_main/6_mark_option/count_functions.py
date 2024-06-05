"""Module with function to test"""


def count_up_letters(words: str) -> int:
    """
    The function counts how many uppercase letters are in words
    :param words: the words
    :return: number of letters
    """
    count_upper_letters = 0
    for letter in words:
        if letter.isalpha() and letter.isupper():
            count_upper_letters += 1
    return count_upper_letters
