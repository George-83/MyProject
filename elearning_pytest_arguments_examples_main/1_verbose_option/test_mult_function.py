"""Test module for verbose option"""
from cube_function import numbers_to_cube


def test_ten_numbers_to_cube():
    """    Check a function with positive values.    """
    result = ['1\n', '8\n', '27\n', '64\n', '125\n', '216\n', '343\n', '512\n', '729\n', '100\n']
    assert numbers_to_cube([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == result


def test_three_numbers_to_cube():
    """    Check a function with negative values.     """
    assert numbers_to_cube([-5, 2, 0]) == ['-125\n', '8\n', '0\n']
