from unittest import TestCase
from lab05 import choose_inventory


class TestChooseInventory(TestCase):

    def test_successful(self):

        for i in choose_inventory(['c', 'b', 'd', 'a', 'e'], 3):
            self.assertIn(i, ['a', 'b', 'c', 'd', 'e'])

    def test_empty_values(self):
        self.assertEqual([], choose_inventory([], 0))

    def test_negative_selection(self):
        self.assertEqual([], choose_inventory(['c', 'b', 'd', 'a', 'e'], 0))

    def test_equal_selection(self):
        self.assertEqual(['a', 'b', 'c'], choose_inventory(['c', 'a', 'b'], 3))

    def test_greater_selection(self):
        self.assertEqual(['a', 'b', 'c'], choose_inventory(['c', 'a', 'b'], 5))
