#!/usr/bin/python
"""Standardize the order of elements in the schema.sql file generated from virtuoso"""
from __future__ import print_function
from builtins import zip
import re
import sys
from itertools import islice

create_re = re.compile(r'^create\s+(\w+)', re.I+ re.MULTILINE)
order = ['type', 'table', 'index', 'view', 'procedure', 'method', 'trigger']

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        schema = f.read()
        parts = create_re.split(schema)
        if len(parts) % 2:
            start = parts.pop(0)
        parts = list(zip([x.lower() for x in islice(parts,0,None,2)], islice(parts,1,None,2)))
        parts.sort(key=lambda t_n: (order.index(t_n[0]), t_n[1]))
        for t, n in parts:
            print('create', t, n)
