# -*- coding: utf-8 -*-
"""Test Entry"""

import os
from sklearn.model_selection import GridSearchCV

from torch_tagger import Tagger
from torch_tagger.utils import text_reader

CURRENT = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(CURRENT, 'train.txt')

def test_grid():
    """Test GridSearch"""
    x_data, y_data = text_reader(PATH)
    parameters = {
        'embedding_dim': (16, 32),
        'hidden_dim': (16, 32),
        'bidirectional': (True, False),
        'rnn_type': ('lstm', 'gru'),
        'num_layers': (1, 2),
        'optimizer': ('SGD', 'Adam'),
    }
    x_train = x_data + x_data + x_data
    y_train = y_data + y_data + y_data
    tag = Tagger(batch_size=2, epochs=1, verbose=0, device='cpu')
    clf = GridSearchCV(tag, parameters, verbose=1, n_jobs=1)
    clf.fit(x_train, y_train)
    print(clf.cv_results_['mean_test_score'])
    print(clf.best_estimator_)
