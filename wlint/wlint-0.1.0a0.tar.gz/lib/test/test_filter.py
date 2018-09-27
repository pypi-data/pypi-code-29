#/usr/bin/python3

import unittest

import wlint.filter
import wlint.purify


class TestWordList(unittest.TestCase):
    def test_add_word(self):
        count = 0

        def _add_fn(word, pattern):
            del pattern
            nonlocal count
            count += 1
            self.assertEqual(word, "hello")

        wlint.filter.add_word("hello", _add_fn)
        self.assertEqual(count, 1)

    def test_add_sequence(self):
        words = {}
        count = 0

        def _add_fn(word, pattern):
            del pattern
            nonlocal count
            nonlocal words
            words[word] = None
            count += 1

        wlint.filter.add_words(["hello", "world"], _add_fn)
        self.assertEqual(count, 2)
        self.assertTrue("hello" in words)
        self.assertTrue("world" in words)


def _make_word_list(sequence):
    words = {}

    def _add_words(word, pattern):
        nonlocal words
        words[word] = pattern

    wlint.filter.add_words(sequence, _add_words)
    return words


class TestFilter(unittest.TestCase):
    def _run_filter(self, words, sequence, expected):
        hits = {}

        def build_hits(word, line, column):
            nonlocal hits
            hits[(line, column)] = word

        wlint.filter.filter_sequence(words, sequence, build_hits)
        self.assertEqual(len(hits), len(expected))
        for (key, value) in expected.items():
            del value

            self.assertTrue(key in expected)
            self.assertEqual(hits[key], expected[key])

    def test_single(self):
        words = _make_word_list(["hello"])
        text = [
            "hello world"
        ]
        expected = {
            (1, 0): "hello"
        }
        self._run_filter(words, text, expected)

    def test_multiple(self):
        words = _make_word_list([
            "hello",
            "world"
        ])
        text = [
            "hello world"
        ]
        expected = {
            (1, 0): "hello",
            (1, 6): "world"
        }
        self._run_filter(words, text, expected)


if __name__ == '__main__':
    unittest.main()
