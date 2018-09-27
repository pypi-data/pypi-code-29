#!/usr/bin/python3

"""Functions to count words."""

import re

_RIGHT_SINGLE_QUOTE = "’"
_PATTERN = re.compile(r"\b([\w\-\'{}]+)\b".format(_RIGHT_SINGLE_QUOTE))


def count_line(text):
    """
    Count the number of words in a line.

    A word is defined as anything any combination of word characters (defined
    by \\w in Python's regex library), hyphens (-), straight single-quotes, and
    a right single typographer's quote (the latter two function as apostrophes
    depending on context), surrounded by word boundaries (defined by \\b in
    Python's regex library).

    Despite the function name, it can count words across multiple lines.

    Arguments:
    text -- ext to count words in

    Return:
    A tuple containing:
      - a dictionary of every word and its count
      - the total number of words
    """
    counts = {}

    local_count = 0
    match = _PATTERN.search(text)
    while match:
        word = match.group(1)
        new_count = counts.get(word, 0) + 1
        counts[word] = new_count
        local_count += 1
        match = _PATTERN.search(text, match.end())

    return (counts, local_count)


def _update_full_counts(full_counts, line_counts):
    for word, count in line_counts[0].items():
        new_count = full_counts.get(word, 0) + count
        full_counts[word] = new_count


def count_lines(handle):
    """
    Count the number of words in an iterable object.

    Arguments:
    handle -- Something to iterate over.

    Return:
    A tuple containing:
      - a dictionary of every word and its count
      - the total number of words
    """
    full_counts = {}
    total_word_count = 0

    for text in handle:
        counts = count_line(text)
        _update_full_counts(full_counts, counts)
        total_word_count += counts[1]

    return (full_counts, total_word_count)
