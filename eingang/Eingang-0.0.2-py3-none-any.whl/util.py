"""
Some secondary utility functions.
"""

import binascii
import os
import random
import string
import sys


def get_random_alphanum_string(count):
    return ''.join(
        random.choice(
            string.ascii_lowercase + string.digits) for _ in range(count))


def get_quoted_random_string(length, chunk_size):
    value = get_random_alphanum_string(length)
    indices = list(range(0, length, chunk_size))
    substrings = [value[x:x + chunk_size] for x in indices]
    first = True
    s = '"""\n'
    s += '\n'.join(substrings)
    s += '\n"""'
    return s


def replace(filename):
    with open(filename, 'r') as f:
        text = f.read()
    text = text.replace(
        '@SECURITY_PASSWORD_SALT@', get_quoted_random_string(1024, 48))
    text = text.replace('@SECRET_KEY@', get_quoted_random_string(128, 48))
    with open(filename, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    replace(sys.argv[1])
