import unittest
from python_digits import DigitWord
from python_digits import Digit


class TestDigits(unittest.TestCase):
    def test_digitword_instantiate(self):
        dw = DigitWord(1, 2, 3, 4)
        self.assertEqual(dw.word, [1, 2, 3, 4])
