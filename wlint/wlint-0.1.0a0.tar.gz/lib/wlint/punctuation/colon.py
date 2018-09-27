#!/usr/bin/python3

"""Punctuation rules around colons and semi-colons."""

import wlint.punctuation


def _colon_rule(name, colon):
    rules = []
    # a colon might be followed by a digit if it's time
    if name == "colon":
        rules.append(("{}.missing-space".format(name),
                      wlint.punctuation.make_pair_regex_rule(colon,
                                                             "[^\\s\\d]")))
    elif name == "semicolon":
        rules.append(("{}.missing-space".format(name),
                      wlint.punctuation.make_pair_regex_rule(colon,
                                                             "\\S")))

    rules.append(("{}.preceeding-space".format(name),
                  wlint.punctuation.make_pair_regex_rule("\\s", colon)))

    return rules


def _get_colon_rules():
    rules = []
    rules += _colon_rule("colon", ":")
    rules += _colon_rule("semicolon", ";")

    return rules


_COLON_RULES = _get_colon_rules()
