# -*- coding: utf-8 -*-
"""Test utils class"""

from torch_tagger.utils import default_spliter

def test_utils():
    """test utils"""
    print(default_spliter(['a']))
    print(default_spliter('a b c'))
    try:
        default_spliter(12)
    except: # pylint: disable=bare-except
        pass
