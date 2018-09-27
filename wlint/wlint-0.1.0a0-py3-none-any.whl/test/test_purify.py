#!/usr/bin/python3

import unittest

import wlint.purify


def compare(ut, text, expected):
    ut.assertEqual(ut.fn(text), expected)


class TestPurifyText(unittest.TestCase):
    def setUp(self):
        self.fn = wlint.purify.text

    def test_text(self):
        text = "This is a test."
        compare(self, text, text)


class TestPurifyTex(unittest.TestCase):
    def setUp(self):
        self.fn = wlint.purify.tex

    def test_text(self):
        text = "This is a test."
        compare(self, text, text)

    def test_strip_comment(self):
        text = "% this is a comment"
        compare(self, text, "")

    def test_strip_command(self):
        text = R"\textbf{This is bold text.}"
        expected = "       {This is bold text.}"
        compare(self, text, expected)

    def test_strip_nested_command(self):
        text = R"\textbf{This is bold \textit{and slanted text.}}"
        expected = "       {This is bold        {and slanted text.}}"
        compare(self, text, expected)


if __name__ == '__main__':
    unittest.main()
