#!/usr/bin/python3

"""
A common module for punctuation rules.

Punctuation rules and checks are built around the idea of functions that
perform one check.  Each function should have the following properties:
  - take two arguments: text to check and a function to call if the rule is
    violated.  The callback function should take a single argument: the index
    into the text where the violation was detected.
  - If the violation is detected multiple times for a given piece of text, the
    callback function should be called for each violation.
  - Return either True or False, depending on whether the violation was
    detected or not.
"""

import re

import wlint.purify


def make_regex_rule(pattern_text):
    """
    Create a punctuation rule based on a simple regex check.

    Arguments:
    pattern_text - A string representing a valid regular expression.

    Return:
    A function that considers a match of pattern_text as a hit.
    """
    pattern = re.compile(pattern_text)

    def _execute(text, found_fn):
        hit = False
        match = pattern.search(text)
        while match:
            hit = True
            found_fn(match.start())
            match = pattern.search(text, match.end())
        return hit

    return _execute


def make_pair_regex_rule(first, second):
    """
    Create a punctuation rule based on consecutive patterns.

    Arguments:
    first -- the first part of a regex pattern
    second -- the second part of a regex pattern

    Return:
    A punctuation check function that fails if the concatinated regex pattern
    matches.
    """
    return make_regex_rule("{}{}".format(first, second))
