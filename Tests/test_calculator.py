"""Docstring."""

import unittest
from calculator import Calculator
# import module mock from unittest
from unittest import mock


class TestCalculator(unittest.TestCase):
    """Docstring."""

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        result = self.calculator.sum(3, 7)
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = self.calculator.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_subtract(self):
        result = self.calculator.subtract(22, 2)
        self.assertEqual(result, 20)

    def test_divide(self):
        result = self.calculator.divide(100, 25)
        self.assertEqual(result, 4)

    def test_sqrt(self):
        result = self.calculator.sqrt(25)
        self.assertEqual(result, 5)

    def test_pi(self):
        result = self.calculator.pi(180)
        expected_result = 3.14159
        self.assertAlmostEqual(result, expected_result, places=2)


# create a new Mock object and assign it to the variable
m = mock.Mock()

# End of EPAM education


if __name__ == "__main__":
    unittest.main()

    # """Docstring."""
    #
    # import unittest
    # from tasks.calculator import Calculator
    #
    #
    # class TestCalculator(unittest.TestCase):
    #     """Docstring."""
    #
    #     def setUp(self):
    #         self.calculator = Calculator()
    #
    #     def test_sum(self):
    #         result = self.calculator.sum(3, 7)
    #         self.assertEqual(result, 10)
    #
    #     def test_multiply(self):
    #         result = self.calculator.multiply(3, 4)
    #         self.assertEqual(result, 12)
    #
    #     def test_subtract(self):
    #         result = self.calculator.subtract(22, 2)
    #         self.assertEqual(result, 20)
    #
    #     def test_divide(self):
    #         result = self.calculator.divide(100, 25)
    #         self.assertEqual(result, 4)
    #
    #     def test_sqrt(self):
    #         result = self.calculator.sqrt(25)
    #         self.assertEqual(result, 5)
    #
    #     def test_pi(self):
    #         result = self.calculator.pi(180)
    #         expected_result = 3.14159
    #         self.assertAlmostEqual(result, expected_result, places=2)
    #
    #
    # if __name__ == "__main__":
    #     unittest.main()

