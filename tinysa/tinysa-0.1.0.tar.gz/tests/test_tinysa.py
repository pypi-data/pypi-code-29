import unittest
from tinysa.tinysa import TinySA


class TestTinySA(unittest.TestCase):

    def test_index(self):
        suffix_array = TinySA()
        suffix_array.index('banana')
        self.assertEqual(suffix_array.positions, [5, 3, 1, 0, 4, 2])

    def test__get_suffixes(self):
        suffix_array = TinySA()
        suffix_array._get_suffixes_of('banana')
        suffixes = ['banana', 'anana', 'nana', 'ana', 'na', 'a']
        self.assertEqual(suffix_array.suffixes, suffixes)

    def test__sort_suffixes_between(self):
        suffix_array = TinySA()
        suffix_array._get_suffixes_of('banana')
        suffix_array._sort_suffixes_between(0, len(suffix_array.suffixes) - 1)
        sorted_suffixes = ['a', 'ana', 'anana', 'banana', 'na', 'nana']
        sorted_positions = [5, 3, 1, 0, 4, 2]
        self.assertEqual(suffix_array.suffixes, sorted_suffixes)
        self.assertEqual(suffix_array.positions, sorted_positions)

    def test_search(self):
        suffix_array = TinySA()
        suffix_array.index('banana')
        self.assertEqual(suffix_array.search('ana'), 1)


if __name__ == "__main__":
    unittest.main()
