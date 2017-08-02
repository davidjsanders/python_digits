import unittest
from python_digits import DigitWord
from python_digits import DigitWordAnalysis


class TestDigitWord_2_0(unittest.TestCase):
    def test_dw20_instantiate_dec(self):
        dw = DigitWord(1, 2, 3, 4, wordtype=DigitWord.DIGIT)
        self.assertEqual(dw.word, [1, 2, 3, 4])

    def test_dw20_instantiate_hex(self):
        dw = DigitWord(1, 0xc, 0xf, 4, wordtype=DigitWord.HEXDIGIT)
        self.assertEqual(dw.word, ['1', 'c', 'f', '4'])

    def test_dw20_instantiate_hexstr(self):
        dw = DigitWord('1', '0xc', '0xf', '4', wordtype=DigitWord.HEXDIGIT)
        self.assertEqual(dw.word, ['1', 'c', 'f', '4'])

    def test_dw20_instantiate_badtype(self):
        with self.assertRaises(ValueError):
            DigitWord('A', 'Z', 'X', 'E', wordtype=3)

    def test_dw20_empty_dec(self):
        dw = DigitWord(wordtype=DigitWord.DIGIT)
        self.assertEqual(dw.word, [])

    def test_dw20_empty_hex(self):
        dw = DigitWord(wordtype=DigitWord.HEXDIGIT)
        self.assertEqual(dw.word, [])

    def test_dw20_str_hex(self):
        dw = DigitWord(1, 2, 0xc, 0xa, 5, wordtype=DigitWord.HEXDIGIT)
        self.assertEqual(str(dw), "12ca5")

    def test_dw20_equality_hex(self):
        dw1 = DigitWord(0xa, 0xb, 0xc, wordtype=DigitWord.HEXDIGIT)
        dw2 = DigitWord(0xa, 0xb, 0xc, wordtype=DigitWord.HEXDIGIT)
        self.assertEqual(dw1, dw2)

    def test_dw20_inequality_hex(self):
        dw1 = DigitWord(0xa, 0xb, 0xc, wordtype=DigitWord.HEXDIGIT)
        dw2 = DigitWord(0xc, 0xb, 0xa, wordtype=DigitWord.HEXDIGIT)
        self.assertNotEqual(dw1, dw2)

    def test_dw20_iteration_hex(self):
        dw = DigitWord(0x1, 2, 0xc, 0xa, wordtype=DigitWord.HEXDIGIT)
        iterstring = ""
        for d in dw:
            iterstring += str(d)[2:]  # Slice string to remove 0x from each element
        self.assertEqual(iterstring, str(dw))

    def test_dw20_json_hex(self):
        dw = DigitWord(1, 0xf, 3, wordtype=DigitWord.HEXDIGIT)
        dwjson = dw.dump()
        dw2 = DigitWord(wordtype=DigitWord.HEXDIGIT)
        dw2.load(dwjson)
        self.assertEqual(dw, dw2)

    def test_dw20_json_badtypes(self):
        with self.assertRaises(ValueError):
            dw = DigitWord(1, 2, 0xc, wordtype=DigitWord.HEXDIGIT)
            dwjson = dw.dump()
            dw2 = DigitWord()
            dw2.load(dwjson)

    def test_dw20_random_hex(self):
        dw = DigitWord(1, 2, 3, 4, wordtype=DigitWord.HEXDIGIT)
        # Use a while loop just in case the computer randomly
        # generates [1, 2, 3, 4]
        while dw.word == [1, 2, 3, 4]:
            dw.random(4)
        self.assertNotEqual(dw.word, [1, 2, 3, 4])

    def test_dw20_comphex(self):
        dw1 = DigitWord(1, 2, 3, wordtype=DigitWord.HEXDIGIT)
        dw2 = DigitWord(2, 3, 1, wordtype=DigitWord.HEXDIGIT)
        for i in dw1.compare(dw2):
            self.assertIsInstance(i, DigitWordAnalysis)

    def test_dw20_comp_bad_types(self):
        dw1 = DigitWord(1, 2, 3, wordtype=DigitWord.HEXDIGIT)
        dw2 = DigitWord(1, 2, 3, wordtype=DigitWord.DIGIT)
        with self.assertRaises(ValueError):
            dw1.compare(dw2)

    def test_dw20_set_hexword(self):
        dw = DigitWord(1, 2, 3, wordtype=DigitWord.HEXDIGIT)
        dw.word = [0xa, 0xc, 1]
        self.assertEqual(dw.word, ['a', 'c', '1'])
