import unittest
from python_digits import Digit


class TestDigits(unittest.TestCase):
    def test_d_instantiate(self):
        d = Digit(1)
        self.assertEqual(d, 1)

    def test_d_string_value(self):
        d = Digit("1")
        self.assertEqual(d, 1)

    def test_d_too_high(self):
        with self.assertRaises(ValueError):
            d = Digit(23)

    def test_d_too_low(self):
        with self.assertRaises(ValueError):
            d = Digit(-2)

    def test_d_no_value(self):
        with self.assertRaises(TypeError):
            d = Digit()

    def test_d_as_int(self):
        d1 = Digit(2)
        d2 = Digit(2)
        self.assertEqual(d1 * d2, 4)
