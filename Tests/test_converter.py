"""Docstring."""

import unittest
from unittest.mock import patch
from converter import Converter


def mock_converter(_, celsius):
    return celsius * 9/5 + 32


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    @patch('converter.Converter.convert_celsius_to_fahrenheit', side_effect=mock_converter)
    def test_converter(self, _):
        expected_result = 86
        actual_result = Converter.convert_celsius_to_fahrenheit(self, 30)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
