"""Test module for verbose option"""
import pytest
from count_functions import count_up_letters


def test_count_up_letters():
    """    Check the operation of the function with the correct values.    """
    assert count_up_letters("Hello, World!") == 2


@pytest.mark.extend
def test_count_empty_string():
    """    Check the operation of a function with an empty string.    """
    assert count_up_letters("") == 0


@pytest.mark.extend
def test_count_numbers_signs():
    """    Check a function with non-letter characters.    """
    assert count_up_letters("21+") == 0
