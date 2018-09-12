#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from data_util.preprocess_data import TextPreprocessor
import json
import random
from gensim.models import KeyedVectors
from tflearn.data_utils import pad_sequences
# help(gensim.models.keyedvectors.Word2VecKeyedVectors)


def load_vocab(path, using_pretrained=True):
    if using_pretrained:
        wv = KeyedVectors.load(path)
        vocab = list(wv.vocab.keys())
    else:
        with open(path, "r", encoding="utf-8") as f:
            vocab = json.load(f)
    vocab.insert(0, "_UNKNOWN_")
    word2index = {}
    for i, v in enumerate(vocab):
        word2index[v] = i
    return set(vocab), word2index


# def split_dataset(word2index, dataset_json, valid_portion=0.1):
#     print("spliting... {}".format(time.asctime(time.localtime(time.time()))))
#     train, validation, test = load_dataset(word2index, dataset_json=dataset_json)
#     with open(train_json, "w", newline="", encoding='UTF-8') as f:
#         json.dump(train, f)
#     with open(validation_json, "w", newline="", encoding='UTF-8') as f:
#         json.dump(validation, f)
#     with open(test_json, "w", newline="", encoding='UTF-8') as f:
#         json.dump(test, f)

def gen_dataset(word2index, original_json, processed_json, valid_portion=0.1):
    with open(original_json, "r", encoding="utf-8") as f:
        dataset = json.load(f)
    X, Y = [], []
    for i, data in enumerate(dataset):
        x = []
        for word in data['text'].split():
            index = word2index.get(word, 0)
            if index > 0:
                x.append(index)
        if len(x) == 0:
            continue
        y = int(data['label'])
        # ys_mulithot_list = transform_multilabel_as_multihot(y, tag_vocab_size)
        X.append(x)
        Y.append(y)

    dataset_size = len(X)
    print("dataset size: %i" % dataset_size)
    train = padding(X[:int((1 - 2 * valid_portion) * dataset_size)], 100) + (Y[:int((1 - 2 * valid_portion) * dataset_size)],)
    valid = padding(X[int((1 - 2 * valid_portion) * dataset_size) + 1:int((1 - valid_portion) * dataset_size)], 100) + \
        (Y[int((1 - 2 * valid_portion) * dataset_size) + 1:int((1 - valid_portion) * dataset_size)], )
    test = padding(X[int((1 - valid_portion) * dataset_size) + 1:], 100) + (Y[int((1 - valid_portion) * dataset_size) + 1:],)
    with open(processed_json, "w", encoding="utf-8") as f:
        json.dump((train, valid, test), f, indent="\t")


def load_dataset(dataset_json):
    with open(dataset_json, "r", encoding="utf-8") as f:
        (train, valid, test) = json.load(f)
    return train, valid, test


def text2index(text, word2index):
    index = []
    if type(text) == str:
        text = [text]
    for t in text:
        x = []
        for word in t.split():
            x.append(word2index.get(word, 0))
        if len(x) == 0:
            x = [0]
        index.append(x)
    return index


def padding(index, maxlen):
    length = [[len(s) if len(s) <= maxlen else maxlen] for s in index]
    seq = pad_sequences(index, maxlen=maxlen, value=0.)
    return seq.tolist(), length


if __name__ == "__main__":
    original = path.join(path.dirname(__file__), "../dataset/dataset.json")
    processed = path.join(path.dirname(__file__), "../dataset/processed.json")
    # preprocess(positive_json, negative_json, dataset_json, vocab_json)
    vocab, word2index = load_vocab(path.join(path.dirname(__file__), "../wv/API_WV/vocab.txt"))
    gen_dataset(word2index, original, processed)
    # split_dataset(word2index)
