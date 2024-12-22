import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_negative(self):
        self.assertRaises(ValueError, factorial, -10)

    def test_float(self):
        self.assertRaises(TypeError, factorial, 3.14)

    def test_0(self):
        self.assertEqual(factorial(0), 1)

    def test_10(self):
        self.assertEqual(factorial(10), 3628800)
