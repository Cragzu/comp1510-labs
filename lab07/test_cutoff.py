from unittest import TestCase
from midterm import cutoff


class TestCutoff(TestCase):

    def test_empty_list_zero(self):
        self.assertEqual(cutoff([], 0), 0)

    def test_empty_list_non_zero(self):
        self.assertEqual(cutoff([], 5), 0)

    def test_one_item_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, cutoff, [0], 0)

    def test_one_item_non_divisible(self):
        self.assertEqual(cutoff([0], 5), 1)

    def test_one_item_equal(self):
        self.assertEqual(cutoff([2], 2), 1)

    def test_one_item_greater(self):
        self.assertEqual(cutoff([2], 4), 0)

    def test_many_items_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, cutoff, [1, 2, 3, 4, 5], 0)

    def test_many_items_some_divisible(self):
        self.assertEqual(cutoff([1, 2, 3, 4, 5], 2), 2)

    def test_many_items_identical_all_divisible(self):
        self.assertEqual(cutoff([2, 2, 2, 2, 2], 2), 5)

    def test_many_items_identical_none_divisible(self):
        self.assertEqual(cutoff([2, 2, 2, 2, 2], 10), 0)

    def test_many_items_all_divisible(self):
        self.assertEqual(cutoff([3, 6, 9, 12, 15], 3), 5)
