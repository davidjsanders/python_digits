import unittest
from python_digits import Digit


class TestDigits(unittest.TestCase):
    def test_digit_instantiate(self):
        d = Digit(1)
        self.assertEqual(d, 1)

    def test_digit_string_value(self):
        d = Digit("1")
        self.assertEqual(d, 1)

    def test_digit_too_high(self):
        with self.assertRaises(ValueError):
            d = Digit(23)

    def test_digit_too_low(self):
        with self.assertRaises(ValueError):
            d = Digit(-2)

    def test_digit_no_value(self):
        with self.assertRaises(TypeError):
            d = Digit()
