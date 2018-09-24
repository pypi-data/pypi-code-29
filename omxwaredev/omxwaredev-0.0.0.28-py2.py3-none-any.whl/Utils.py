# -*- coding: utf-8 -*-
"""
OMXWare Utils
"""
import string
import random

"""
Generate a random string 

Returns:
    A random string with Uppercase alphabets and numbers.
"""
def rand(size=36, chars=string.ascii_uppercase + string.digits):
    N = 36
    return ''.join(random.choice(chars) for _ in range(size))
