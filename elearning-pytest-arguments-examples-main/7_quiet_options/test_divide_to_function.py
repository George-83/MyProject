"""Test module for --collect-only option"""
from divide_function import divide_to


def test_divide_by_default():
    """    Check a function with a single parameter passed.    """
    assert divide_to(6) == 3.0


def test_divide_to_another_divider():
    """    Check a function with the second parameter changed.    """
    assert divide_to(10, 5) == 2.0


def test_divide_to_zero():
    """    Check a function with a null value.    """
    assert divide_to(4, 0) == 4
    