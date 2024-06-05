"""Test module for --collect-only option"""
from expression_function import expression


def test_if_number_less_than_minus_five():
    """    Check the operation of the first condition in the function    """
    assert expression(-10) == 95
