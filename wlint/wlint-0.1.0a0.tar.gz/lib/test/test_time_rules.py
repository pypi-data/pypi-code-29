#!/usr/bin/python3

import unittest

import wlint.punctuation_style
import wlint.punctuation.time


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


class TestTimeRules(unittest.TestCase):
    def setUp(self):
        self.rules = wlint.punctuation.time._get_time_rules()

    def test_missing_space(self):
        text = "12:00a.m."
        _run_rules(self, text, "time.missing-space", 0)

    def test_missing_periods(self):
        text = "12:00 am"
        _run_rules(self, text, "time.missing-periods", 0)

    def test_missing_uppercase_AP_M(self):
        text = "12:00 A.M."
        _run_rules(self, text, "time.uppercase-APM", 0)

    def test_missing_uppercase_AP_m(self):
        text = "12:00 A.m."
        _run_rules(self, text, "time.uppercase-APm", 0)

    def test_missing_uppercase_ap_M(self):
        text = "12:00 a.M."
        _run_rules(self, text, "time.uppercase-apM", 0)


if __name__ == '__main__':
    unittest.main()
