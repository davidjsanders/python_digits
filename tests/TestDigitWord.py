import unittest
import json
from python_digits import DigitWord
from python_digits import Digit
from python_digits import DigitWordAnalysis


class TestDigits(unittest.TestCase):
    def test_dw_instantiate(self):
        dw = DigitWord(1, 2, 3, 4)
        self.assertEqual(dw.word, [1, 2, 3, 4])

    def test_dw_empty(self):
        dw = DigitWord()
        self.assertEqual(dw.word, [])

    def test_dw_str(self):
        dw = DigitWord(1, 2, 3, 4, 5)
        self.assertEqual(str(dw), "12345")

    def test_dw_equality(self):
        dw1 = DigitWord(1, 2, 3)
        dw2 = DigitWord(1, 2, 3)
        self.assertEqual(dw1, dw2)

    def test_dw_inequality(self):
        dw1 = DigitWord(1, 2, 3)
        dw2 = DigitWord(0, 2, 3)
        self.assertNotEqual(dw1, dw2)

    def test_dw_equality_bad(self):
        dw = DigitWord(1, 2, 3)
        self.assertNotEqual(dw, [1, 2, 3])

    def test_dw_iteration(self):
        dw = DigitWord(1, 2, 3, 4)
        iterstring = ""
        for d in dw:
            iterstring += str(d)
        self.assertEqual(iterstring, str(dw))

    def test_dw_length(self):
        dw = DigitWord(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(len(dw), 7)

    def test_dw_length_bad(self):
        dw = DigitWord(1, 2, 3)
        self.assertNotEqual(len(dw), 4)

    def test_dw_json(self):
        dw = DigitWord(1, 2, 3)
        dwjson = dw.dump()
        dw2 = DigitWord()
        dw2.load(dwjson)
        self.assertEqual(dw, dw2)

    def test_dw_json_bad_type(self):
        dw = DigitWord()
        with self.assertRaises(TypeError):
            dw.load([1, 2, 3, 4])

    def test_dw_json_bad_json(self):
        dw = DigitWord()
        with self.assertRaises(json.decoder.JSONDecodeError):
            dw.load("1, 2, 3")

    def test_dw_random(self):
        dw = DigitWord(1, 2, 3, 4)
        # Use a while loop just in case the computer randomly
        # generates [1, 2, 3, 4]
        while dw.word == [1, 2, 3, 4]:
            dw.random(4)
        self.assertNotEqual(dw.word, [1, 2, 3, 4])

    def test_dw_random_bad(self):
        dw = DigitWord()
        with self.assertRaises(TypeError):
            dw.random("S")

    def test_dw_comp(self):
        dw1 = DigitWord(1, 2, 3)
        dw2 = DigitWord(2, 3, 1)
        for i in dw1.compare(dw2):
            self.assertIsInstance(i, DigitWordAnalysis)

    def test_dw_comp_bad_length(self):
        dw1 = DigitWord(1, 2, 3)
        dw2 = DigitWord(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            dw1.compare(dw2)

    def test_dw_comp_bad_empty(self):
        dw1 = DigitWord(1, 2, 3)
        with self.assertRaises(TypeError):
            dw1.compare(None)

    def test_dw_set_word(self):
        dw = DigitWord(1, 2, 3)
        dw.word = [3, 2, 1]
        self.assertEqual(dw.word, [3, 2, 1])
