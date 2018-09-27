#!/usr/bin/python3

import unittest

import wlint.punctuation_style
import wlint.punctuation.colon


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


class TestColonRules(unittest.TestCase):
    def setUp(self):
        self.rules = wlint.punctuation.colon._get_colon_rules()

    def test_leading_space(self):
        text = "My favorite color : green."
        _run_rules(self, text, "colon.preceeding-space", 17)

    def test_missing_space_colon(self):
        text = "My favorite color:green."
        _run_rules(self, text, "colon.missing-space", 17)

    def test_missing_space_time(self):
        # this shouldn't fail the rules
        text = "It's 12:52"
        _run_rules(self, text)

    def test_missing_space_semicolon(self):
        text = "My favorite color is green;it's the best."
        _run_rules(self, text, "semicolon.missing-space", 26)


if __name__ == '__main__':
    unittest.main()
