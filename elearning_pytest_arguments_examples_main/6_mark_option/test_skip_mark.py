"""Test module for mark option"""
import pytest
from count_functions import count_up_letters


def test_count_up_letters():
    """    Check the operation of the function with the correct values.    """
    assert count_up_letters("Hello, World!") == 2


@pytest.mark.skip(reason="function not developed yet")
def test_count_down_letters():
    """    Check the operation of the function with the correct values.    """
    assert count_lower_letters("Hello, World!") == 8
