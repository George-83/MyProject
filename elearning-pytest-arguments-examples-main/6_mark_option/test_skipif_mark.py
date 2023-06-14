"""Test module for mark option"""
import pytest


@pytest.mark.skipif(TypeError, reason="function not developed yet")
def test_count_down_letters():
    """    Check the operation of the function with the correct values.    """
    assert count_lower_letters("Hello, World!") == 8
