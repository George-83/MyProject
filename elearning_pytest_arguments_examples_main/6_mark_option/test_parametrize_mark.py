"""Test module for verbose option"""
import pytest
from count_functions import count_up_letters


@pytest.mark.parametrize(
    ("words", "result"),
    [
        ("Hello, World!", 2),
        ("Hop-Hey, Lalaley!", 3),
        ("SuNsHiNe", 4)
    ]
)
def test_count_up_letters(words: str, result: int):
    """
    Check the function with different input data.
    :param words: the words
    :param result: result of function
    """
    assert count_up_letters(words) == result
