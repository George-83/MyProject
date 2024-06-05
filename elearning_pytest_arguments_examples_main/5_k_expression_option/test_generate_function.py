"""Test module for -k option"""
from generate_function import generator


def test_generator_with_correct_values():
    """    Check the operation of the function with the correct values.    """
    assert generator(2, 9) == [2, 3, 4, 5, 6, 7, 8, 9]


def test_generator_start_more_than_finish():
    """    Check the operation of a function with inverted borders.    """
    assert generator(14, 7) == [7, 8, 9, 10, 11, 12, 13, 14]


def test_generator_negative_values():
    """    Check the operation of the function with negative values.    """
    assert generator(-3, -7) == [-7, -6, -5, -4, -3]


def test_generator_zero_value():
    """    Check the operation of the function with zero values.    """
    assert generator(5, 0) == [0, 1, 2, 3, 4, 5]
