from unittest import TestCase

from subpaths.subpaths import find_all_subpath_occurrences, find_all_common_subpaths_between


class TestSubpathOccurrences(TestCase):

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


class TestCommonSubpath(TestCase):

    def test_find_all_common_subpaths_between__with_intersections(self):
        path1 = [1, 2, 3, 4, 5]
        path2 = [3, 4, 5, 6, 7]
        expected_paths = {(3, 4), (4, 5), (3, 4, 5)}
        self.assertEqual(expected_paths, find_all_common_subpaths_between(path1, path2))

    def test_find_all_common_subpaths_between__with_intersections__complex(self):
        path1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        path2 = [3, 4, 5, 6, 7]
        path3 = [4, 5]
        expected_paths = {(4, 5)}
        self.assertEqual(expected_paths, find_all_common_subpaths_between(path1, path2, path3))

    def test_find_all_common_subpaths_between__no_intersections(self):
        path1 = [1, 2, 3, 4, 5]
        path2 = [6, 7, 8, 9, 10]
        expected_paths = set()
        self.assertEqual(expected_paths, find_all_common_subpaths_between(path1, path2))

    def test_find_all_common_subpaths_between__single_path(self):
        path1 = [1, 2, 3, 4, 5]
        expected_paths = {(1, 2), (1, 2, 3, 4), (4, 5), (1, 2, 3, 4, 5), (1, 2, 3), (2, 3), (3, 4, 5), (2, 3, 4),
                          (2, 3, 4, 5), (3, 4)}
        self.assertEqual(expected_paths, find_all_common_subpaths_between(path1))

    def test_find_all_common_subpaths_between__no_paths(self):
        expected_paths = set()
        self.assertEqual(expected_paths, find_all_common_subpaths_between())
