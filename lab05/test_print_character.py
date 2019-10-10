from unittest import TestCase
from lab05 import print_character
import unittest.mock
import io


class TestPrintCharacter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):  # a list with these attributes should print expected_output
        expected_output = "Your character is named Test\nYour Strength is 15\n" \
                          "Your Dexterity is 12\nYour Constitution is 14\n" \
                          "Your Intelligence is 6\nYour Wisdom is 10\n" \
                          "Your Charisma is 10\nYou don\'t have any items right now.\n"
        print_character(['Test', ['Strength', 15], ['Dexterity', 12],
                        ['Constitution', 14], ['Intelligence', 6], ['Wisdom', 10],
                        ['Charisma', 10]])
        self.assertEqual(mock_stdout.getvalue(), expected_output)
