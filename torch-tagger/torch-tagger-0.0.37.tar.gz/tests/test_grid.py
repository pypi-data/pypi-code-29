# -*- coding: utf-8 -*-
"""Test Entry"""

import os
import unittest

from sklearn.model_selection import GridSearchCV
from torch_tagger import Tagger
from torch_tagger.utils import text_reader

CURRENT = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(CURRENT, 'train.txt')


class TestGrid(unittest.TestCase):
    def test_grid(self):
        """Test GridSearch"""
        x_data, y_data = text_reader(PATH)
        parameters = {
            'bidirectional': (True, False),
            'rnn_type': ('lstm', 'gru'),
            'num_layers': (1, 2),
            'use_char': ('cnn', 'rnn', None),
            'use_crf': (True, False),
        }
        x_train = x_data + x_data + x_data
        y_train = y_data + y_data + y_data
        tag = Tagger(batch_size=2, epochs=1, verbose=0, device='cpu')
        clf = GridSearchCV(tag, parameters, verbose=1, n_jobs=1)
        clf.fit(x_train, y_train)
        self.assertIsInstance(clf.cv_results_['mean_test_score'][0], float)


if __name__ == '__main__':
    unittest.main()
