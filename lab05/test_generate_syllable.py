from unittest import TestCase
from lab05 import generate_syllable


class TestGenerateSyllable(TestCase):

    def test_first_consonant(self):
        self.assertIn((generate_syllable())[0], 'bcdfghjklmnpqrstvwxyz')

    def test_second_vowel(self):
            self.assertIn((generate_syllable())[1], 'aeiouy')

    def test_length(self):
        self.assertEqual(2, len(generate_syllable()))