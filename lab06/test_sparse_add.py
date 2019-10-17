from unittest import TestCase
from sparsevector import sparse_add


class TestSparseAdd(TestCase):

    def test_empty_dicts(self):
        self.assertDictEqual(sparse_add({}, {}), {})

    def test_same_indices(self):
        self.assertDictEqual(sparse_add({0: 5, 1: 5, 2: 5}, {0: 1, 1: 2, 2: 3}), {0: 6, 1: 7, 2: 8})

    def test_first_empty(self):
        self.assertDictEqual(sparse_add({}, {0: 1, 1: 2, 2: 3}), {0: 1, 1: 2, 2: 3})

    def test_second_empty(self):
        self.assertDictEqual(sparse_add({0: 1, 1: 2, 2: 3}, {}), {0: 1, 1: 2, 2: 3})

    def test_no_index_matching(self):
        self.assertDictEqual(sparse_add({0: 1, 2: 1, 4: 1}, {1: 1, 3: 1, 5: 1}), {0: 1, 2: 1, 4: 1, 1: 1, 3: 1, 5: 1})

    def test_some_index_matching(self):
        self.assertDictEqual(sparse_add({0: 1, 2: 1, 5: 1}, {1: 1, 2: 1, 5: 1}), {0: 1, 2: 2, 1: 1, 5: 2})

    def test_add_to_zero(self):
        self.assertDictEqual(sparse_add({3: 1, 4: 2, 5: 4, 9: 5}, {3: 1, 5: 2, 9: -5}), {3: 2, 5: 6, 4: 2})
