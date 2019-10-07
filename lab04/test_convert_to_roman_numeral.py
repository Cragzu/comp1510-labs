from unittest import TestCase
from lab04.roman_numbers import convert_to_roman_numeral


class TestConvertToRomanNumeral(TestCase):
    def test_1(self):
        self.assertEqual('I', convert_to_roman_numeral(1))

    def test_10000(self):
        self.assertEqual('MMMMMMMMMM', convert_to_roman_numeral(10000))

    def test_4(self):
        self.assertEqual('IV', convert_to_roman_numeral(4))

    def test_5(self):
        self.assertEqual('V', convert_to_roman_numeral(5))

    def test_6(self):
        self.assertEqual('VI', convert_to_roman_numeral(6))

    def test_9(self):
        self.assertEqual('IX', convert_to_roman_numeral(9))

    def test_10(self):
        self.assertEqual('X', convert_to_roman_numeral(10))

    def test_20(self):
        self.assertEqual('XX', convert_to_roman_numeral(20))

    def test_40(self):
        self.assertEqual('XL', convert_to_roman_numeral(40))

    def test_50(self):
        self.assertEqual('L', convert_to_roman_numeral(50))

    def test_90(self):
        self.assertEqual('XC', convert_to_roman_numeral(90))

    def test_100(self):
        self.assertEqual('C', convert_to_roman_numeral(100))

    def test_400(self):
        self.assertEqual('CD', convert_to_roman_numeral(400))

    def test_500(self):
        self.assertEqual('D', convert_to_roman_numeral(500))

    def test_900(self):
        self.assertEqual('CM', convert_to_roman_numeral(900))

    def test_1000(self):
        self.assertEqual('M', convert_to_roman_numeral(1000))

