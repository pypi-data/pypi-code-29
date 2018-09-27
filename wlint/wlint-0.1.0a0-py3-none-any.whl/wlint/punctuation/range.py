#!/usr/bin/python3

"""Punctuation rules around range operations (e.g., "5-17")."""

import wlint.punctuation

_EMDASH = "—"
_ENDASH = "–"


def _get_range_rules(pattern):
    rules = []
    rules.append(("endash.preceeding-space",
                  wlint.punctuation.make_regex_rule("{}\\s+{}\\s*{}".format(
                      pattern, _ENDASH,
                      pattern))))
    rules.append(("endash.trailing-space",
                  wlint.punctuation.make_regex_rule("{}\\s*{}\\s+{}".format(
                      pattern, _ENDASH,
                      pattern))))

    rules.append(("endash.replace-hyphen",
                  wlint.punctuation.make_regex_rule("{}\\s*-\\s*{}".format(
                      pattern, pattern))))
    rules.append(("endash.replace-emdash",
                  wlint.punctuation.make_regex_rule("{}\\s*{}\\s*{}".format(
                      pattern, _EMDASH,
                      pattern))))

    return rules


_RANGE_RULES = _get_range_rules(R"\d+")
