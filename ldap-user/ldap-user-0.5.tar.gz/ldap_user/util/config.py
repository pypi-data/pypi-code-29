#! /usr/bin/env python
# coding: utf-8
import re
__author__ = '鹛桑够'


invalid_line_compile = re.compile("^([a-z]\S*)\s+(\S*)", re.I)


def load_config(config_path):
    with open(config_path) as r:
        c = r.read()
        all_lines = c.split("\n")
        c_values = dict()
        for line in all_lines:
            match_r = invalid_line_compile.match(line)
            if match_r is not None:
                c_values[match_r.groups()[0]] = match_r.groups()[1]
        return c_values
