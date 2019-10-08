from unittest import TestCase
from lab05 import create_character


class TestCreateCharacter(TestCase):

    def test_starting_name(self):  # check if first item in list is string
        self.assertIsInstance((create_character(3))[0], str)

    def test_following_lists(self):
        for i in range(1, len(create_character(4))):  # every list item after first should be a list
            self.assertIsInstance((create_character(4))[i], list)

    def test_length(self):
        self.assertEqual(len(create_character(2)), 7)