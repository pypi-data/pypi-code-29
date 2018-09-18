# -*- coding: utf-8 -*-
"""Test Tagger class"""

import os
import pickle
# import torch
# import numpy as np
from torch_tagger import Tagger
from torch_tagger.utils import text_reader

CURRENT = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(CURRENT, 'train.txt')

def test_tagger():
    """Test tagger entry"""
    x_data, y_data = text_reader(PATH)
    tagger = Tagger(batch_size=4, debug=True)
    params = tagger.get_params(True)
    tagger.set_params(**params)
    tagger.fit(x_data, y_data)
    with open('/tmp/test_tagger.pkl', 'wb') as fobj:
        pickle.dump(tagger, fobj)
    with open('/tmp/test_tagger.pkl', 'rb') as fobj:
        tagger = pickle.load(fobj)
    tagger.predict(x_data)
    tagger.predict(x_data, verbose=1)
    tagger.score(x_data, y_data)
    tagger.score(x_data, y_data, verbose=1)

    for device in ('auto', 'gpu', 'cpu'):
        tagger = Tagger(device=device)
        try:
            tagger._get_device()# pylint: disable=protected-access
        except: # pylint: disable=bare-except
            pass

if __name__ == '__main__':
    test_tagger()
