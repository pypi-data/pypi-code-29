# -*- coding: utf-8 -*-
"""Test NER"""

import os
import uuid
import pickle
import tempfile

from torch_tagger import Tagger
from torch_tagger.utils import text_reader

def train_ner():
    """Train NER model"""
    x_data, y_data = text_reader('/tmp/train.txt')
    x_val, y_val = text_reader('/tmp/valid.txt')
    tag = Tagger(
        batch_size=10,
        epochs=1000,
        embedding_dim=100,
        hidden_dim=100,
        embedding_dropout_p=0.5,
        rnn_dropout_p=0.5,
        optimizer='Nadam',
        learning_rate=2e-3,
        learning_rate_decay=0.0,
        weight_decay=1e-8,
        crf=True,
        num_layers=1
    )
    # tag = Tagger(
    #     batch_size=10,
    #     epochs=1000,
    #     embedding_dim=100,
    #     hidden_dim=100,
    #     embedding_dropout_p=0.5,
    #     rnn_dropout_p=0.5,
    #     optimizer='SGD',
    #     learning_rate=0.015,
    #     learning_rate_decay=0.05,
    #     weight_decay=1e-8,
    #     crf=False,
    #     num_layers=1
    # )
    print('tag model', tag)

    tag_best_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + '.pkl')
    print('tag_best_path', tag_best_path)
    tag.fit(
        x_data, y_data, x_val, y_val,
        patient_dev=100,
        save_best=tag_best_path
    )
    test_ner(tag_best_path)
    generate_result_ner(tag_best_path, tag_best_path + '.txt')

def test_ner(model_path):
    """Test NER model"""
    x_data, y_data = text_reader('/tmp/test.txt')
    print('load model', model_path)
    tag = pickle.load(open(model_path, 'rb'))
    pre, rec, f1s = tag.score(x_data, y_data, verbose=1, detail=True)
    print('test precision {:.4f} recall {:.4f} f1 {:.4f}'.format(
        pre, rec, f1s
    ))
    pred = tag.predict(x_data[:3])

    for i, indy in enumerate(y_data[:3]):
        print(indy)
        print(pred[i])
        print('-' * 30)

def generate_result_ner(model_path, output_path='/tmp/test_pred.txt'):
    """Generate file could evel by conll eval script"""
    x_data, y_data = text_reader('/tmp/test.txt')
    print('load model', model_path)
    tag = pickle.load(open(model_path, 'rb'))
    pred = tag.predict(x_data)
    with open(output_path, 'w') as fobj:
        for xbch, ybch, pbch in zip(x_data, y_data, pred):
            for ind, x_one in enumerate(xbch):
                fobj.write('{} {} {}\n'.format(
                    x_one, ybch[ind], pbch[ind]
                ))

if __name__ == '__main__':
    train_ner()
