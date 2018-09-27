#!/usr/bin/python3

import operator
import os
import re
import pkg_resources

import wlint.purify
import wlint.tool
import wlint.filter


def _get_default_lists(path):
    files_list = os.listdir(path)
    pattern = re.compile("^([a-z]+)-words.txt$")
    files = []
    for file in files_list:
        match = pattern.search(file)
        if match:
            files.append(match.group(1))
    return sorted(files)


_LIST_DIR = pkg_resources.resource_filename(__name__, "share/filter-lists/")
_DEFAULT_LISTS = _get_default_lists(_LIST_DIR)
_DEFAULT_LISTS_STR = ",".join(_DEFAULT_LISTS)

_SORTS = [
    ("alpha", "Sort output based on the actual words."),
    ("sequential", "Sort output based on the order words appear.")
]

_SORT_FNS = {
    "alpha": lambda hits: hits.sort(),
    "sequential": lambda hits: hits.sort(key=operator.itemgetter(1, 2))
}


class ListFilter(wlint.tool.Tool):

    def __init__(self):
        super().__init__(description="Detect troublesome words",
                         prog="wlint list-filter")
        self.add_argument(
            "--lists",
            help="Change the set of word lists.  This should be a "
                 "comma-separated list of built-in lists.",
            default=_DEFAULT_LISTS_STR)
        self.add_argument(
            "--list",
            help="Use a custom word list.  The list should be a plain text "
                 "file with one word per line.",
            action="append")

        self.add_sort(_SORTS)

    def execute(self, parsed_args):
        def _make_lists():
            if parsed_args.lists:
                lists = parsed_args.lists.split(",")
                # Read the built in lists
                return wlint.filter.build_word_list(_LIST_DIR, lists)
            return {}

        words = _make_lists()
        # Read any extra lists
        if parsed_args.list:
            def _add_words(word, pattern):
                nonlocal words
                words[word] = pattern

            for word_list in parsed_args.list:
                wlint.filter.add_word_file(word_list, _add_words)

        # word list is complete, so setup variables
        sorter = _SORT_FNS[parsed_args.sort]
        purifier = wlint.tool.get_purifier(parsed_args)

        def _print_hits(hits, found_fn):
            sorter(hits)
            for (word, line, col) in hits:
                found_fn(word, line, col)

        def _process(file_handle):
            hits = []
            wlint.filter.filter_sequence(
                words,
                wlint.purify.PurifyingIterator(file_handle, purifier),
                lambda word, line, col: hits.append((word, line, col)))
            _print_hits(
                hits, lambda word, line, col: print(
                    "{} {} ({}:{})".format(
                        file_handle.name, word, line, col)))

        return wlint.tool.iterate_files(parsed_args, _process)


def main(args=None):
    # pylint: disable=missing-docstring
    list_filter = ListFilter()
    wlint.tool.execute_tool(list_filter, args)


_LIST_FILTER_COMMAND = (
    main,
    "List filter words")

if __name__ == '__main__':
    main()
