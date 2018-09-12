# -*- coding: utf-8 -*-

"""Main module."""

#JSON
import json
data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]);
json = json.loads(data);
