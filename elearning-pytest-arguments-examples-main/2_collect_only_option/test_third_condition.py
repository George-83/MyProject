"""Test module for --collect-only option"""
from expression_function import expression


def test_whether_number_more_than_five():
    """    Check the operation of the third condition in the function.    """
    assert expression(10) == 105
