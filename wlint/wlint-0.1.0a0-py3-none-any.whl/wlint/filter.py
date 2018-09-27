#!/usr/bin/python3

"""Types and functions to work with filter words."""

import re


def add_word(word, handle_fn):
    """
    Add a word to the list.

    Arguments:
    word -- the word to add
    """
    pattern = re.compile(r"\b{}\b".format(word), re.IGNORECASE)
    handle_fn(word, pattern)


def add_words(sequence, handle_fn):
    """
    Add a series of words to the word list.

    Arguments:
    sequence -- some object that can be iterated over.
    """
    for word in sequence:
        add_word(word, handle_fn)


def add_word_file(path, handle_fn):
    class _NewlineStrippingIterator:
        # pylint: disable=too-few-public-methods
        def __init__(self, file_handle):
            self._iter = iter(file_handle)

        def __iter__(self):
            return self

        def __next__(self):
            next_word = next(self._iter)
            return next_word[:-1]

    with open(path, "r") as input_list:
        add_words(_NewlineStrippingIterator(input_list), handle_fn)


def build_word_list(path, word_lists):
    """
    Parse built-in word lists for filtering.

    Arguments:
    path -- the filesystem path to find word lists
    word_lists -- the subset of built-in lists to use
    """
    words = {}

    def _add_word(word, pattern):
        nonlocal words

        words[word] = pattern

    for word_list in word_lists:
        file_path = "{}/{}-words.txt".format(path, word_list)
        try:
            add_word_file(file_path, _add_word)
        except FileNotFoundError:
            raise \
                ValueError("'{}' is not a word list".format(file_path))
    return words


def filter_text(words, text, found_fn):
    """
    Search text for any filter words.

    Arguments:
    words -- a dictionary of words and regex patterns to detect those words
    text -- the text to parse
    found_fn -- The function to call when a filter word is found.
                Arguments are word, line_number.
    """
    for word, pattern in words.items():
        match = pattern.search(text)
        while match:
            found_fn(word, match.start())
            match = pattern.search(text, match.end())


def filter_sequence(words, sequence, found_fn):
    """Parse a sequence.

    Arguments:
    words -- a dictionary of words and regex patterns to detect those words
    sequence -- an iterable object to filter over
    found_fn -- A function to invoke on each match.  Arguments are: word,
                lineNumber, column.
    """
    line = 0
    for text in sequence:
        line += 1
        filter_text(words, text, lambda word, col: found_fn(word, line, col))
