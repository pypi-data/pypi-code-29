from unittest import TestCase

from subpaths.subpaths import find_all_subpath_occurrences


class TestSubpaths(TestCase):

    def test_finds_paths_for_single_path(self):
        path = [1, 2, 3, 4, 5]
        expected_paths = {
            (1, 2): 1,
            (2, 3): 1,
            (3, 4): 1,
            (4, 5): 1,
            (1, 2, 3): 1,
            (2, 3, 4): 1,
            (3, 4, 5): 1,
            (1, 2, 3, 4): 1,
            (2, 3, 4, 5): 1,
            (1, 2, 3, 4, 5): 1,
        }
        self.assertEqual(expected_paths, find_all_subpath_occurrences(path))

    def test_finds_paths_for_multiple_paths(self):
        path_a = [1, 2, 3, 4, 5]
        path_b = [3, 4, 5, 7]
        path_c = [2, 3, 4, 8, 9, 7]
        expected_paths = {
            (1, 2): 1,
            (1, 2, 3): 1,
            (1, 2, 3, 4): 1,
            (1, 2, 3, 4, 5): 1,
            (2, 3): 2,
            (2, 3, 4): 2,
            (2, 3, 4, 5): 1,
            (2, 3, 4, 8): 1,
            (2, 3, 4, 8, 9): 1,
            (2, 3, 4, 8, 9, 7): 1,
            (3, 4): 3,
            (3, 4, 5): 2,
            (3, 4, 5, 7): 1,
            (3, 4, 8): 1,
            (3, 4, 8, 9): 1,
            (3, 4, 8, 9, 7): 1,
            (4, 5): 2,
            (4, 5, 7): 1,
            (4, 8): 1,
            (4, 8, 9): 1,
            (4, 8, 9, 7): 1,
            (5, 7): 1,
            (8, 9): 1,
            (8, 9, 7): 1,
            (9, 7): 1
        }
        self.assertEqual(expected_paths, find_all_subpath_occurrences(path_a, path_b, path_c))

    def test_finds_no_paths_for_single_node_path(self):
        path = [1]
        expected_paths = {}
        self.assertEqual(expected_paths, find_all_subpath_occurrences(path))

    def test_finds_no_paths_for_no_node_path(self):
        path = []
        expected_paths = {}
        self.assertEqual(expected_paths, find_all_subpath_occurrences(path))

    def test_finds_no_paths_when_given_nothing(self):
        expected_paths = {}
        self.assertEqual(expected_paths, find_all_subpath_occurrences())
