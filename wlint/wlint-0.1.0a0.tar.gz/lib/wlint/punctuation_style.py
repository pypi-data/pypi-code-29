#!/usr/bin/python3

import re

import wlint.plugin
import wlint.purify
import wlint.tool


def _add_enabled_rules(pattern, enabled_rules):
    for (message, check_fn) in _AVAILABLE_RULES:
        if pattern.match(message):
            enabled_rules[message] = check_fn


def _get_enabled_rules(enabled_rules):
    ret = {}
    rules = enabled_rules.split(",")
    for rule in rules:
        pattern = re.compile(rule.replace(".", R"\.").replace("*", ".*"))
        _add_enabled_rules(pattern, ret)
    return ret


def _build_rms(pattern, checks):
    rms = []
    for message in checks:
        if pattern.match(message):
            rms.append(message)
    return rms


def _delete_rules(rms, checks):
    for message in rms:
        del checks[message]


def _remove_disabled_rules(disabled_rules, checks):
    for rule in disabled_rules:
        if rule:  # don't deal with empty strings
            pattern = re.compile(rule.replace(
                ".", R"\.").replace("*", ".*"))
            rms = _build_rms(pattern, checks)
            _delete_rules(rms, checks)
    return checks


def _build_available_rules():
    found_rules = wlint.plugin.query_plugins("wlint.punctuation_rules")
    rule_lists = []
    for name, rules in found_rules.items():
        del name
        rule_lists += rules
    return rule_lists


_AVAILABLE_RULES = _build_available_rules()


def _check_rules(rules, text, hit_fn):
    for (message, check_fn) in rules:
        check_fn(text, lambda pos, backup_message=message: hit_fn(
            backup_message, pos))


def _check_sequence(rules, iterable, hit_fn):
    line_number = 0
    for text in iterable:
        line_number += 1
        _check_rules(
            rules, text,
            lambda message, pos: hit_fn(line_number, message, pos))


class PunctuationStyle(wlint.tool.Tool):

    def __init__(self):
        super().__init__(description="Check for common punctuation issues",
                         prog="wlint punctuation-style")
        self.add_argument(
            "--enable",
            help="Rules to use when processing text.  An asterisk (*) can be "
                 "used for wildcard matching.",
            default="*")
        self.add_argument(
            "--disable",
            help="Rules to disable when processing text.  If a rule is both "
                 "enabled and disabled, disable takes precedence.")

    def execute(self, parsed_args):
        rules = _get_enabled_rules(parsed_args.enable)
        if parsed_args.disable:
            disable = parsed_args.disable.split(",")
            rules = _remove_disabled_rules(disable, rules)

        checks = []
        for (message, check_fn) in rules.items():
            checks.append((message, check_fn))

        purifier = wlint.tool.get_purifier(parsed_args)

        def _process(file_handle):
            hits = []
            _check_sequence(checks, wlint.purify.PurifyingIterator(file_handle,
                                                                   purifier),
                            lambda line_number, message, pos: hits.append(
                                (line_number, pos, message)))
            hits.sort()
            for (line, col, message) in hits:
                print("{}-{}:{} {}".format(file_handle.name, line,
                                           col, message))

        return wlint.tool.iterate_files(parsed_args, _process)


def main(args=None):
    # pylint: disable=missing-docstring
    punctuation_style = PunctuationStyle()
    wlint.tool.execute_tool(punctuation_style, args)


_PUNCTUATION_STYLE_COMMAND = (
    main,
    "Check for punctuation errors")

if __name__ == '__main__':
    main()
