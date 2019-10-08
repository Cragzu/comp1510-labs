from unittest import TestCase
from lab05 import generate_name


class TestGenerateName(TestCase):

    def test_length(self):
        self.assertEqual(6, len(generate_name(3)))

    def test_vowels(self):
        for i in range(1, len(generate_name(4)), 2):  # every odd letter should be a vowel
            self.assertIn((generate_name(4))[i], 'aeiouy')

    def test_consonants(self):
        for i in range(0, len(generate_name(4)), 2):  # every even letter should be a consonant
            self.assertIn((generate_name(4))[i], 'bcdfghjklmnpqrstvwxyz')