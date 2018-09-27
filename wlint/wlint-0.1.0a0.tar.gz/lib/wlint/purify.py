#!/usr/bin/python3

"""Built-in purification functions"""

import re


class PurifyingIterator:
    """A class to perform purification as it iterates."""
    # pylint: disable=too-few-public-methods

    def __init__(self, iterable, purifier):
        self._iter = iter(iterable)
        self._purifier = purifier

    def __iter__(self):
        return self

    def __next__(self):
        return self._purifier(next(self._iter))


def text(s_data):
    """Purify plain text input."""
    return s_data


_TEXT_PURIFIER = (text, "Plain text")


def tex(s_data):
    """Purify (La)TeX input."""
    def _strip_comment(text_data):
        index = text_data.find("%")
        if index == -1:
            return text_data
        return text_data[:index]

    pattern = re.compile(r"(\\\w+)")

    def _strip_commands(text_data):
        def _replace_fn(match):
            return " " * len(match.group(0))

        return re.sub(pattern, _replace_fn, text_data)

    return _strip_commands(_strip_comment(s_data))


_TEX_PURIFIER = (tex, "(La)TeX input")
