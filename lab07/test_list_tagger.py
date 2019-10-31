from unittest import TestCase
from midterm import list_tagger


class TestListTagger(TestCase):

    def test_empty_list(self):
        self.assertEqual(list_tagger([]),[0])

    def test_list_one_item(self):
        self.assertEqual(list_tagger(['a']), [1, 'a'])

    def test_list_multiple_items(self):
        self.assertEqual(list_tagger(['a', 'b', 'c', 'd']), [4, 'a', 'b', 'c', 'd'])
