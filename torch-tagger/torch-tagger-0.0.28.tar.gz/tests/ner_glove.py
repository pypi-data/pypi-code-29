# -*- coding: utf-8 -*-
"""Test NER with GloVe

Download https://nlp.stanford.edu/projects/glove/
"""

import os
import uuid
import tempfile
import numpy as np

from torch_tagger import Tagger
from torch_tagger.utils import text_reader, PAD_TAG, UNK_TAG, build_vocabulary
from tests.ner import test_ner, generate_result_ner

def read_glove(train_txt='/tmp/train.txt', # pylint: disable=too-many-locals
               glove_path='tests/glove.6B/glove.6B.100d.txt',
               dim=100):
    """Reade GloVe vector"""

    x_data, y_data = text_reader(train_txt)
    vocabulary = build_vocabulary(x_data, y_data)

    def random_vec():
        return np.random.uniform(
            -np.sqrt(3. / dim),
            np.sqrt(3. / dim),
            size=(1, dim)
        )

    predefine_vecs = {}
    predefine_lower_vecs = {}
    with open(glove_path, 'r') as fobj:
        lines = fobj.read().split('\n')
        lines = [x.strip() for x in lines]
        lines = [x for x in lines if x.strip()]
        for line in lines:
            line = line.split()
            if len(line) >= 2:
                word = line[0]
                vec = np.array([float(i) for i in line[1:]])
                vec = vec.reshape(1, dim)
                # words.append(word)
                # vecs.append(vec)
                predefine_vecs[word] = vec
                if word.lower() != word:
                    predefine_lower_vecs[word.lower()] = vec
    vecs = [
        random_vec(),
        random_vec(),
    ]
    word_to_ix = {
        PAD_TAG: 0,
        UNK_TAG: 1
    }
    for word in vocabulary['word_to_ix']:
        if word not in word_to_ix:
            indx = len(word_to_ix)
            word_to_ix[word] = indx
            if word in predefine_vecs:
                vecs.append(predefine_vecs[word])
            elif word.lower() in predefine_lower_vecs:
                vecs.append(predefine_lower_vecs[word.lower()])
            else:
                vecs.append(random_vec())

    ix_to_word = {
        v: k
        for k, v in word_to_ix.items()
    }
    embedding = np.concatenate(vecs)

    return word_to_ix, ix_to_word, embedding

def train_ner():
    """Train NER model"""
    x_data, y_data = text_reader('/tmp/train.txt')
    x_val, y_val = text_reader('/tmp/valid.txt')
    word_to_ix, ix_to_word, embedding = read_glove()
    tag = Tagger(
        batch_size=10,
        epochs=100,
        embedding_dim=100,
        hidden_dim=100,
        embedding_dropout_p=0.5,
        rnn_dropout_p=0.5,
        optimizer='SGD',
        learning_rate=0.015,
        learning_rate_decay=0.05,
        weight_decay=1e-8,
        _word_to_ix=word_to_ix,
        _ix_to_word=ix_to_word,
        embedding_trainable=False
    )
    print('tag model', tag)

    tag_best_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + '.pkl')
    print('tag_best_path', tag_best_path)

    tag.fit(
        x_data, y_data, x_val, y_val,
        patient_dev=100,
        save_best=tag_best_path, pretrained_embedding=embedding
    )

    score = tag.score(x_data, y_data, verbose=1)
    print('train score', score)
    test_ner(tag_best_path)
    generate_result_ner(tag_best_path, tag_best_path + '.txt')

if __name__ == '__main__':
    # read_glove()
    train_ner()
    # test_ner()
