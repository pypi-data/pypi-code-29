from pathlib import Path
from functools import partial

import numpy as np

from .supproperty import supproperty


class decimal(supproperty):
    def __init__(self, *args, **kwargs):
        super(decimal, self).__init__(type=np.float, *args, **kwargs)


class positive_decimal(decimal):
    def __init__(self, *args, **kwargs):
        old_validator = kwargs.get('validator', lambda o, v: True)
        kwargs['validator'] = lambda o, v: old_validator(o, v) and v >= 0
        super(positive_decimal, self).__init__(*args, **kwargs)


class integer(supproperty):
    def __init__(self, *args, **kwargs):
        super(integer, self).__init__(type=np.int, *args, **kwargs)


class positive_integer(integer):
    def __init__(self, *args, **kwargs):
        old_validator = kwargs.get('validator', lambda o, v: True)
        kwargs['validator'] = lambda o, v: old_validator(o, v) and v > 0
        super(positive_integer, self).__init__(*args, **kwargs)


class non_negative_integer(integer):
    def __init__(self, *args, **kwargs):
        old_validator = kwargs.get('validator', lambda o, v: True)
        kwargs['validator'] = lambda o, v: old_validator(o, v) and v >= 0
        super(non_negative_integer, self).__init__(*args, **kwargs)


class pathlike(supproperty):
    def __init__(self, *args, **kwargs):
        super(pathlike, self).__init__(type=Path, *args, **kwargs)


class boolean(supproperty):
    def __init__(self, *args, **kwargs):
        super(boolean, self).__init__(type=bool, *args, **kwargs)


class float_vector(supproperty):
    def __init__(self, *args, **kwargs):
        super(float_vector, self).__init__(type=partial(np.array, dtype=np.float, ndmin=1), *args, **kwargs)
