import unittest
from python_digits import HexDigit


class TestHexDigits(unittest.TestCase):
    def test_hd_instantiate(self):
        d = HexDigit(0x1)
        self.assertEqual(d, 0x1)

    def test_hd_instantiate_f(self):
        d = HexDigit(0xf)
        self.assertEqual(d, 0xf)

    def test_hd_instantiate_int(self):
        d = HexDigit(5)
        self.assertEqual(d, 0x5)

    def test_hd_instantiate_str(self):
        d = HexDigit("0x5")
        self.assertEqual(d, 0x5)

    def test_hd_string_value(self):
        d = HexDigit("f")
        self.assertEqual(d, 0xf)

    def test_hd_bad_hexstr(self):
        with self.assertRaises(ValueError):
            d = HexDigit('0xh')

    def test_hd_too_high(self):
        with self.assertRaises(ValueError):
            d = HexDigit(0xf2)

    def test_hd_too_low(self):
        with self.assertRaises(ValueError):
            d = HexDigit(-2)

    def test_hd_no_value(self):
        with self.assertRaises(TypeError):
            d = HexDigit()

    def test_hd_acts_as_int(self):
        d1 = HexDigit(0xf)
        d2 = HexDigit(4)
        self.assertEqual(d1 * d2, 60)
