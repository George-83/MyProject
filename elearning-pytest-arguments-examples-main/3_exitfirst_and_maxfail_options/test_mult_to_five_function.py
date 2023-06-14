"""Test module for -k option"""
from mult_function import mult_to_five


def test_with_integer():
    """    Check the result of the function with the integer data type.    """
    assert mult_to_five(5) == 25


def test_with_string():
    """    Check the result of the function with the string data type.    """
    assert mult_to_five("3") == 15


def test_with_list():
    """    Check the result of the function with the list data type.    """
    assert mult_to_five([1, 2, 3]) == [5, 10, 15]


def test_with_set():
    """    Check the result of the function with the set data type.    """
    assert mult_to_five({1, 1, 1}) == {5, 5, 5}
