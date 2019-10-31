from unittest import TestCase
from midterm import prepender


class TestPrepender(TestCase):

    def test_all_empty(self):
        test_list = []
        prepender(test_list, '')
        self.assertEqual(test_list, [])

    def test_only_string(self):
        test_list = []
        prepender(test_list, 'Python')
        self.assertEqual(test_list, [])

    def test_only_list(self):
        test_list = ['Python']
        prepender(test_list, '')
        self.assertEqual(test_list, ['Python'])

    def test_one_string(self):
        test_list = ['Python']
        prepender(test_list, 'I love ')
        self.assertEqual(test_list, ['I love Python'])

    def test_many_strings_no_prepend(self):
        test_list = ['Python', 'is', 'better', 'than', 'JavaScript']
        prepender(test_list, '')
        self.assertEqual(test_list, ['Python', 'is', 'better', 'than', 'JavaScript'])

    def test_many_strings_prepend(self):
        test_list = ['Python', 'is', 'better', 'than', 'JavaScript']
        prepender(test_list, 'Umm... ')
        self.assertEqual(test_list, ['Umm... Python', 'Umm... is', 'Umm... better', 'Umm... than', 'Umm... JavaScript'])

