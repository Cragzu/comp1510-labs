from unittest import TestCase
from lab05 import print_character
import random
import unittest.mock
import io

random.seed(0)

class TestPrintCharacter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('lab05.create_character', return_value=['Mykocico', ['Strength', 15], ['Dexterity', 12],
                                                     ['Constitution', 14], ['Intelligence', 6], ['Wisdom', 10],
                                                     ['Charisma', 10]])
    def test_print_character(self, mock_stdout, mock_create_character):
        expected_output = "Your character is named Mykocico\n Your Strength stat is 15\n" \
                          "Your Dexterity stat is 12\n Your Constitution stat is 14\n" \
                          "Your Intelligence stat is 6\n Your Wisdom stat is 10\n" \
                          "Your Charisma stat is 10"
        print_character(mock_create_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
