# -*- coding: utf-8 -*-
"""Test Entry"""

from tests.grid import test_grid
from tests.model import test_model
from tests.tagger import test_tagger
from tests.utils import test_utils

if __name__ == '__main__':
    test_utils()
    test_model()
    test_tagger()
    test_grid()
