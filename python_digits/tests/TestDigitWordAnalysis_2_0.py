import unittest
from python_digits import DigitWordAnalysis


class TestDigitWordAnalysis_2_0(unittest.TestCase):
    def test_dwa20_hex_digit(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit='f',
            in_word=True,
            match=True,
            multiple=True
        )
        self.assertEqual(dwa.digit, 'f')

    def test_dwa20_hex_bad_digit(self):
        with self.assertRaises(ValueError):
            dwa = DigitWordAnalysis(
                index=0,
                digit=0xff,
                in_word=True,
                match=True,
                multiple=True
            )

    def test_dwa20_hex_in_word(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=0xa,
            in_word=True,
            match=False,
            multiple=False
        )
        self.assertEqual(dwa.in_word, True)

    def test_dwa20_hex_match(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit='f',
            in_word=True,
            match=True,
            multiple=True
        )
        self.assertEqual(dwa.match, True)
