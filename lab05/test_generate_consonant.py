from unittest import TestCase
from lab05 import generate_consonant


class TestGenerateConsonant(TestCase):

    def test_generate_consonant(self):
        self.assertIn(generate_consonant(), 'bcdfghjklmnpqrstvwxyz')
