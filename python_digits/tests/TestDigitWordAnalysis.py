import unittest
from python_digits import DigitWordAnalysis


class TestDigitWordAnalysis(unittest.TestCase):
    def test_dwa_instantiation(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=1,
            in_word=False,
            match=False,
            multiple=False
        )
        self.assertIsInstance(dwa, DigitWordAnalysis)

    def test_dwa_index(self):
        dwa = DigitWordAnalysis(
            index=7,
            digit=1,
            in_word=False,
            match=False,
            multiple=False
        )
        self.assertEqual(dwa.index, 7)

    def test_dwa_index_minus_1(self):
        with self.assertRaises(ValueError):
            dwa = DigitWordAnalysis(
                index=-1,
                digit=1,
                in_word=False,
                match=False,
                multiple=False
            )

    def test_dwa_index_bad(self):
        with self.assertRaises(TypeError):
            dwa = DigitWordAnalysis(
                index="S",
                digit=2,
                in_word=False,
                match=False,
                multiple=False
            )

    def test_dwa_digit(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=8,
            in_word=False,
            match=False,
            multiple=False
        )
        self.assertEqual(dwa.digit, 8)

    def test_dwa_digit_minus_1(self):
        with self.assertRaises(ValueError):
            dwa = DigitWordAnalysis(
                index=0,
                digit=-1,   # Should be integer between 0 and 9
                in_word=False,
                match=False,
                multiple=False
            )

    def test_dwa_digit_bad(self):
        with self.assertRaises(ValueError):
            dwa = DigitWordAnalysis(
                index=-1,
                digit="S",  # Should be integer between 0 and 9
                in_word=False,
                match=False,
                multiple=False
            )

    def test_dwa_in_word(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=8,
            in_word=True,
            match=False,
            multiple=False
        )
        self.assertEqual(dwa.in_word, True)

    def test_dwa_in_word_bad(self):
        with self.assertRaises(TypeError):
            dwa = DigitWordAnalysis(
                index=1,
                digit=1,  # Should be integer between 0 and 9
                in_word="False",
                match=False,
                multiple=False
            )

    def test_dwa_match(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=8,
            in_word=True,
            match=True,
            multiple=False
        )
        self.assertEqual(dwa.match, True)

    def test_dwa_match_bad(self):
        with self.assertRaises(TypeError):
            dwa = DigitWordAnalysis(
                index=1,
                digit=1,  # Should be integer between 0 and 9
                in_word=False,
                match="False",
                multiple=False
            )

    def test_dwa_multiple(self):
        dwa = DigitWordAnalysis(
            index=0,
            digit=8,
            in_word=True,
            match=False,
            multiple=True
        )
        self.assertEqual(dwa.multiple, True)

    def test_dwa_multiple_bad(self):
        with self.assertRaises(TypeError):
            dwa = DigitWordAnalysis(
                index=1,
                digit=1,  # Should be integer between 0 and 9
                in_word=False,
                match=False,
                multiple="False"
            )
