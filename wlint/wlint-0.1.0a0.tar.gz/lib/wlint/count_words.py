#!/usr/bin/python3

import operator

import wlint.purify
import wlint.tool
import wlint.wordcounter


def _make_case_fn(parsed_args):
    def _case_sensitive(word):
        return word

    def _case_insensitive(word):
        return word.lower()

    if parsed_args.case_sensitive:
        return _case_sensitive
    return _case_insensitive


def _alpha_sort(items):
    return sorted(list(items))


def _count_sort(items):
    item_list = list(items)
    item_list.sort(key=operator.itemgetter(0))
    item_list.sort(key=operator.itemgetter(1), reverse=True)
    return item_list


_SORT_FNS = {
    "alpha": _alpha_sort,
    "count": _count_sort
}


def _make_ignored_words(parsed_args):
    ignored_words = {}
    if parsed_args.ignore:
        ignore_list = parsed_args.ignore.split(",")
        for word in ignore_list:
            ignored_words[word] = None
    return ignored_words


def _print_counts(counts, total_words):
    for word, count in counts:
        ratio = count / total_words
        print("{}\t{}\t{:.5f}".format(word, count, ratio))


_SORTS = [
    ("alpha", "Print words in alphabetical order."),
    ("count", "Print words based on number of occurances.")
]


class WordCounter(wlint.tool.Tool):

    def __init__(self):
        super().__init__(description="Count the occurrence of each word",
                         prog="wlint count-words")
        # Is there a way to have \w not match numbers?
        # We're going to a call a word anything with these properties:
        #  - surrounded by word boundaries (\b)
        #  - 1 or more:
        #    - word characters
        #    - hyphens
        #    - single quotes (for "plain text" apostrophes)
        #    - right single quotes (for "smart" apostrophes)
        self.add_argument(
            "--case-sensitive",
            help="Treat words differently if they use a different case.",
            action="store_true")
        self.add_argument(
            "--summarize",
            help="Only print summarized results.",
            action="store_true")
        self.add_argument(
            "--ignore",
            help="A comma-separated list of words to skip while processing "
                 "input.")

        self.add_sort(_SORTS)

    def execute(self, parsed_args):
        file_count = 0
        total_words = 0

        key_maker = _make_case_fn(parsed_args)
        sort_count = _SORT_FNS[parsed_args.sort]
        summarize_only = parsed_args.summarize
        ignored_words = _make_ignored_words(parsed_args)
        purifier = wlint.tool.get_purifier(parsed_args)

        total_files = 0
        total_counts = {}

        def _count_words(file_handle):
            nonlocal total_words
            nonlocal total_files

            file_words, word_count = wlint.wordcounter.count_lines(
                wlint.purify.PurifyingIterator(file_handle,
                                               lambda t: key_maker(
                                                   purifier(t))))

            for word, count in file_words.items():
                if word in ignored_words:
                    word_count -= count
                    del file_words[word]
                else:
                    current_count = total_counts.get(word, 0)
                    total_counts[word] = current_count + count

            if not summarize_only:
                print("{}: {}".format(file_handle.name, word_count))
                _print_counts(sort_count(file_words.items()),
                              word_count)
                print("")

            total_words += word_count
            total_files += 1

        missing_files = wlint.tool.iterate_files(parsed_args, _count_words)
        if file_count > 1 or summarize_only:
            print("Total: {}".format(total_words))
            _print_counts(sort_count(total_counts.keys()), total_counts)

        return missing_files


def main(args=None):
    # pylint: disable=missing-docstring
    word_counter = WordCounter()
    wlint.tool.execute_tool(word_counter, args)


_COUNT_WORDS_COMMAND = (
    main,
    "Count words")

if __name__ == '__main__':
    main()
