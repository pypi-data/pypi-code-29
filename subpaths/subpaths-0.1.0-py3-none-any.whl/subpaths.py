from collections import defaultdict
from itertools import chain


def __find_all_subpaths_in_path(path):
    for j in range(len(path) - 1):
        all_partials = (path[i:] for i in range(len(path) - j))
        for pair in zip(*all_partials):
            yield pair


def find_all_subpath_occurrences(*paths) -> dict:
    """
    Turns a dictionary of all paths and the number of times they were seen from any of the given paths
    :param paths: Any number of paths given as a list
    :return: Dictionary mapping a path to it count
    """
    # Generating all subpaths for each path
    all_paths_generator = (__find_all_subpaths_in_path(path) for path in paths if len(path) > 1)

    # Combining all subpaths into one dictionary
    sub_paths = defaultdict(int)
    for sub_path in chain(*all_paths_generator):
        sub_paths[sub_path] += 1

    return sub_paths
