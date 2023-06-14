"""Test module for --collect-only option"""
from expression_function import expression


def test_number_is_zero():
    """    Check the operation of the second condition in the function.    """
    assert expression(0) == 0


def test_number_is_five():
    """    Check the right boundary of the second condition in the function.    """
    assert expression(5) == 10


def test_number_is_minus_five():
    """    Check the left boundary of the second condition in the function.    """
    assert expression(-5) == -10
