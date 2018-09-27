#!/usr/bin/python3

"""Punctuation rules around dashes."""

import wlint.punctuation

_EMDASH = "—"
_ENDASH = "–"


def _get_dash_rules():
    rules = [("emdash.replace-double-hyphen",
              wlint.punctuation.make_regex_rule("\\-\\-")),
             ("emdash.preceeding-space",
              wlint.punctuation.make_pair_regex_rule("\\s", _EMDASH)),
             ("emdash.trailing-space",
              wlint.punctuation.make_pair_regex_rule(_EMDASH, "\\s"))]
    return rules


_DASH_RULES = _get_dash_rules()
