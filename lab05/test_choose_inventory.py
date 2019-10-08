from unittest import TestCase
import random
from lab05 import choose_inventory

random.seed(0)  # use seed so random results will always be the same


class TestChooseInventory(TestCase):

    def test_successful(self):
        self.assertEqual(['a', 'c', 'e'], choose_inventory(['c', 'b', 'd', 'a', 'e'], 3))
        # self.assertIn(choose_inventory(['c', 'b', 'd', 'a', 'e'], 3), ['c', 'b', 'd', 'a', 'e'])

    def test_empty_values(self):
        self.assertEqual([], choose_inventory([], 0))

    def test_negative_selection(self):
        self.assertEqual([], choose_inventory(['c', 'b', 'd', 'a', 'e'], 0))

    def test_equal_selection(self):
        self.assertEqual(['a', 'b', 'c'], choose_inventory(['c', 'a', 'b'], 3))

    def test_greater_selection(self):
        self.assertEqual(['a', 'b', 'c'], choose_inventory(['c', 'a', 'b'], 5))
