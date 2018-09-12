# -*- coding: utf-8 -*-

import codecs
import os
import re
from collections import OrderedDict

__escape_decoder = codecs.getdecoder('unicode_escape')
__posix_variable = re.compile(r'\$\{[^\}]*\}')


def decode_escaped(escaped):
    return __escape_decoder(escaped)[0]


def dotenv_values(dotenv_path):
    values = OrderedDict(parse_dotenv(dotenv_path))
    values = resolve_nested_variables(values)
    return values


def parse_dotenv(dotenv_path):
    with open(dotenv_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)

            # Remove any leading and trailing spaces in key, value
            k, v = k.strip(), v.strip().encode('unicode-escape').decode('ascii')

            if len(v) > 0:
                quoted = v[0] == v[len(v) - 1] in ['"', "'"]

                if quoted:
                    v = decode_escaped(v[1:-1])

            yield k, v


def resolve_nested_variables(values):
    def _replacement(name):
        """
        get appropriate value for a variable name.
        first search in environ, if not found,
        then look into the dotenv variables
        """
        ret = os.getenv(name, values.get(name, ""))
        return ret

    def _re_sub_callback(match_object):
        """
        From a match object gets the variable name and returns
        the correct replacement
        """
        return _replacement(match_object.group()[2:-1])

    for k, v in values.items():
        values[k] = __posix_variable.sub(_re_sub_callback, v)

    return values
