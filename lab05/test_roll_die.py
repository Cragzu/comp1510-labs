from unittest import TestCase
import random
from lab05 import roll_die

random.seed(0)  # use seed so random results will always be the same


class TestRollDie(TestCase):

    def test_negative_roll(self):
        self.assertEqual(0, roll_die(0, 1))

    def test_negative_sides(self):
        self.assertEqual(0, roll_die(1, 0))

    def test_successful(self):
        self.assertEqual(9, roll_die(3, 6))
