#!/usr/bin/python3

import unittest

import wlint.punctuation_style
import wlint.punctuation.quote


def _run_rules(ut, text, expected_rule=None, expected_position=None):
    hit = False

    def hit_fn(rule_message, pos):
        nonlocal hit

        ut.assertEqual(rule_message, expected_rule)
        ut.assertEqual(pos, expected_position)
        hit = True

    wlint.punctuation_style._check_rules(ut.rules, text, hit_fn)
    if expected_position or expected_rule:
        ut.assertTrue(hit)


class TestQuotationRules(unittest.TestCase):
    def setUp(self):
        self.rules = wlint.punctuation.quote._get_quote_rules()

    def test_double_quotes(self):
        text = "{}{}Don't use duplicate quotes.{}".format(wlint.punctuation.quote._LEFT_SINGLE_QUOTE,
                                                          wlint.punctuation.quote._LEFT_SINGLE_QUOTE,
                                                          wlint.punctuation.quote._RIGHT_DOUBLE_QUOTE)
        _run_rules(self, text, "quotation.consecutive-opening-quotes", 0)

    def test_missing_space(self):
        text = "{}{}This is a nested quote{}{}{}".format(wlint.punctuation.quote._LEFT_DOUBLE_QUOTE,
                                                         wlint.punctuation.quote._LEFT_SINGLE_QUOTE,
                                                         wlint.punctuation.quote._RIGHT_SINGLE_QUOTE,
                                                         wlint.punctuation.quote._THIN_SPACE_NONBREAK,
                                                         wlint.punctuation.quote._RIGHT_DOUBLE_QUOTE)
        _run_rules(
            self,
            text,
            "quotation.missing-space-opening-double-single",
            0)

    def test_incorrect_space_plain(self):
        text = "{} {}This is a nested quote{}{}{}".format(wlint.punctuation.quote._LEFT_DOUBLE_QUOTE,
                                                          wlint.punctuation.quote._LEFT_SINGLE_QUOTE,
                                                          wlint.punctuation.quote._RIGHT_SINGLE_QUOTE,
                                                          wlint.punctuation.quote._THIN_SPACE_NONBREAK,
                                                          wlint.punctuation.quote._RIGHT_DOUBLE_QUOTE)
        _run_rules(
            self,
            text,
            "quotation.incorrect-space-opening-double-single",
            0)

    def test_incorrect_space_break(self):
        text = "{}{}{}This is a nested quote{}{}{}".format(wlint.punctuation.quote._LEFT_DOUBLE_QUOTE,
                                                           wlint.punctuation.quote._THIN_SAPCE_BREAK,
                                                           wlint.punctuation.quote._LEFT_SINGLE_QUOTE,
                                                           wlint.punctuation.quote._RIGHT_SINGLE_QUOTE,
                                                           wlint.punctuation.quote._THIN_SPACE_NONBREAK,
                                                           wlint.punctuation.quote._RIGHT_DOUBLE_QUOTE)
        _run_rules(
            self,
            text,
            "quotation.incorrect-space-opening-double-single",
            0)


if __name__ == '__main__':
    unittest.main()
