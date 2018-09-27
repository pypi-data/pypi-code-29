#!/usr/bin/python3

import unittest

import wlint.purify
import wlint.wordcounter


def _verify_counts(word_count_result, expected, ut):
    ut.assertEqual(len(word_count_result[0]), len(expected[0]))
    ut.assertEqual(word_count_result[1], expected[1])

    total_count = 0
    for word, count in word_count_result[0].items():
        ut.assertEqual(count, expected[0][word])
        total_count += count

    ut.assertEqual(word_count_result[1], total_count)


class TestCountLine(unittest.TestCase):
    def test_count_empty(self):
        counts = wlint.wordcounter.count_line("")
        self.assertFalse(counts[0])
        expected = ({}, 0)
        _verify_counts(counts, expected, self)

    def test_single(self):
        counts = wlint.wordcounter.count_line("hello")
        expected = ({
            "hello": 1
        }, 1)
        _verify_counts(counts, expected, self)

    def test_multiple(self):
        counts = wlint.wordcounter.count_line("hello world")
        expected = ({
            "hello": 1,
            "world": 1
        }, 2)
        _verify_counts(counts, expected, self)

    def test_duplicate(self):
        counts = wlint.wordcounter.count_line("hello world hello")
        expected = ({
            "hello": 2,
            "world": 1
        }, 3)
        _verify_counts(counts, expected, self)

    def test_comma(self):
        counts = wlint.wordcounter.count_line("hello, world")
        expected = ({
            "hello": 1,
            "world": 1
        }, 2)
        _verify_counts(counts, expected, self)

    def test_single_quote(self):
        counts = wlint.wordcounter.count_line("that's cool")
        expected = ({
            "that's": 1,
            "cool": 1
        }, 2)
        _verify_counts(counts, expected, self)

    def test_single_apostrophe(self):
        counts = wlint.wordcounter.count_line(
            "that{}s cool".format(
                wlint.wordcounter._RIGHT_SINGLE_QUOTE))
        expected = ({
            "that{}s".format(wlint.wordcounter._RIGHT_SINGLE_QUOTE): 1,
            "cool": 1
        }, 2)
        _verify_counts(counts, expected, self)

    def test_single_hyphen(self):
        counts = wlint.wordcounter.count_line("e-mail is valid")
        expected = ({
            "e-mail": 1,
            "is": 1,
            "valid": 1
        }, 3)
        _verify_counts(counts, expected, self)


class TestCountSequence(unittest.TestCase):
    def test_empty(self):
        counts = wlint.wordcounter.count_lines([])
        expected = ({}, 0)
        _verify_counts(counts, expected, self)

    def test_simple(self):
        counts = wlint.wordcounter.count_lines(["hello world"])
        expected = ({
            "hello": 1,
            "world": 1
        }, 2)
        _verify_counts(counts, expected, self)

    def test_multiple(self):
        counts = wlint.wordcounter.count_lines(["hello world",
                                                "goodbye world"])
        expected = ({
            "hello": 1,
            "goodbye": 1,
            "world": 2
        }, 4)
        _verify_counts(counts, expected, self)


if __name__ == '__main__':
    unittest.main()
