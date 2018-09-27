#!/usr/bin/python3

import unittest

import wlint.punctuation_style
import wlint.punctuation.range


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


class TestRangeRules(unittest.TestCase):
    def setUp(self):
        self.rules = wlint.punctuation.range._get_range_rules(R"\d+")

    def test_preceeding_space(self):
        text = "10 {}11".format(wlint.punctuation.range._ENDASH)
        _run_rules(self, text, "endash.preceeding-space", 0)

    def test_trailinging_space(self):
        text = "10{} 11".format(wlint.punctuation.range._ENDASH)
        _run_rules(self, text, "endash.trailing-space", 0)

    def test_replace_hyphen(self):
        text = "10-11"
        _run_rules(self, text, "endash.replace-hyphen", 0)

    def test_replace_emdash(self):
        text = "10{}11".format(wlint.punctuation.range._EMDASH)
        _run_rules(self, text, "endash.replace-emdash", 0)


if __name__ == '__main__':
    unittest.main()
