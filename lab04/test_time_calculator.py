import io
from unittest import TestCase
import unittest.mock
from time_calculator import time_calculator


class TestTimeCalculator(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_30_seconds(self, mock_stdout):
        expected_output = "0 0 0 30\n"  # account for auto inserted newline
        time_calculator(30)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_one_minute(self, mock_stdout):
        expected_output = "0 0 1 0\n"
        time_calculator(60)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_one_hour(self, mock_stdout):
        expected_output = "0 1 0 0\n"
        time_calculator(3600)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_one_day(self, mock_stdout):
        expected_output = "1 0 0 0\n"
        time_calculator(84600)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
