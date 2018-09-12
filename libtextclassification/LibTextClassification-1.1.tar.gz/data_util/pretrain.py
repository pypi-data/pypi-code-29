#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import Word2Vec
from os import path
import csv
import time

import logging
import multiprocessing
import os
import re

from nltk.stem import WordNetLemmatizer


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

dataset_dir = path.join(path.dirname(__file__), "dataset/document_classification")
stoplist_csv = path.join(dataset_dir, "stoplist.csv")

pattern1 = re.compile(r'[a-zA-Z]*[0-9+-:#]+')
pattern2 = re.compile(r'[/\\\*\(\),=\?<>"\[\]]|0x')
pattern3 = re.compile(r'([a-zA-Z])\1{3,}')

def clean(raw_html):
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, ' ', raw_html)
    wnl = WordNetLemmatizer()
    # sentences = []
    # pattern1 = re.compile(r'<code>.*?</code>')
    # pattern2 = re.compile(r'<code>.*?</code>|<blockquote>.*?</blockquote>|<a.*?</a>|</?.*?>|&#x[AD];|\\t|\\n')
    # pattern3 = re.compile(r'</?code>|&#x[AD];|\\t|\\n')
    with open(stoplist_csv, "r", encoding='UTF-8') as f:
        reader = csv.reader(f)
        reader.__next__()
        stoplist = [row[0] for row in reader]
    words = re.split(' ', text)
    new_text = []
    for word in words:
        w = wnl.lemmatize(word.lower().strip(' ’!"$%&\'*,-./:;<=>?‘“”？，；…@[\\]^_`{|}~'))
        if (pattern1.match(word) is not None or pattern2.search(word) is not None or pattern3.search(word) is not None) or w in stoplist:
            continue
        new_text.append(w)
    return new_text


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for root, dirs, files in os.walk(self.dirname):
            for filename in files:
                file_path = root + '/' + filename
                for line in open(file_path):
                    sline = line.strip()
                    if sline == "":
                        continue
                    rline = clean(sline)
                    yield rline


if __name__ == '__main__':
    sentences = MySentences("enwiki")
    print("Training...")
    print("start time {}".format(time.asctime(time.localtime(time.time()))))
    model = Word2Vec(sentences, size=128, window=10, min_count=10, sg=1, hs=1, workers=multiprocessing.cpu_count())
    print("end time {}".format(time.asctime(time.localtime(time.time()))))
    model.save("./model/Word2Vec.model")
    model.wv.save("./model/vocab.txt")
