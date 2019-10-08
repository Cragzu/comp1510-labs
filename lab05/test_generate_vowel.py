from unittest import TestCase
from lab05 import generate_vowel


class TestGenerateVowel(TestCase):

    def test_generate_vowel(self):
        self.assertIn(generate_vowel(), 'aeiouy')
