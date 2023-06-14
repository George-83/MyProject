"""Test module for --collect-only option"""
from mult_numbers_function import mult_numbers


def test_with_negative_number():
    """    Check the function if there are negative input values.    """
    assert mult_numbers([1, 2, 3, 4, -5]) == -120


def test_with_valid_input():
    """    Check the operation of the function if there is to pass the correct values.    """
    numbers = list(range(1, 6))
    print(numbers)
    assert mult_numbers(numbers) == 120


def test_with_zero():
    """    Check the function if there is a pass 0.    """
    assert mult_numbers([1, 2, 3, 4, 0]) == 0
