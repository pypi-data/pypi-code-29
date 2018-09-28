# -*- coding: utf-8 -*-
# @Time    : 18-9-28 下午1:47
# @Author  : duyongan
# @FileName: text_utils.py
# @Software: PyCharm
import re
from simple_pickle import utils
from jieba import posseg
from text_process.text import Text
import nltk
import os

def text2sencents_zh(text):
    text = re.sub('\u3000|\r|\t|\xa0', '', text)
    text = re.sub('？”|！”|。”', '”', text)
    sentences = re.split("([。！？……])", text)
    sentences.append('')
    sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
    last_sentences=[]
    for sentence in sentences:
        last_sentences+=[senten.replace('\n','').strip() for senten in sentence.split('\n\n')
                         if senten.replace('\n','').strip()]
    return last_sentences

def text2sencents_en(text):
    text = re.sub('\u3000|\r|\t|\xa0|\n', '', text)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences


def sort_keys_weights(keys,weights,return_tuple=False):
    keys_weights = dict(zip(keys, weights))
    keys_weights = sorted(keys_weights.items(), key=lambda k: k[1], reverse=True)
    if return_tuple:
        return keys_weights
    keys = [term[0] for term in keys_weights]
    return keys

def text_process_zh_single(text):
    here = os.path.dirname(__file__)
    text = re.sub('\u3000|\r|\t|\xa0|\n', '', text)
    stopwords=utils.read_pickle(here+'/stopwords')
    text=posseg.lcut(text)
    text_n_list = [word_.word for word_ in text if
                   len(word_.word) > 1 and word_.word not in stopwords and
                   word_.flag in ['n','v','ns','nt','nr','ni','nl','nz',
                                  'nrf','nsf','nrj','nr1','nr2']]
    return text_n_list

def text_process_zh_not_single(text):
    here = os.path.dirname(__file__)
    stopwords = utils.read_pickle(here+'/stopwords')
    words = [tuple_ for tuple_ in list(posseg.cut(text))
             if list(tuple_)[0].strip() and len(list(tuple_)[0].strip())>1]
    words2 = []
    temp = ''
    enstart = False
    for i in range(len(words)):
        if words[i].flag in ['n','ns','nt','nr','ni','nl',
                             'nz','nrf','nsf','nrj','nr1',
                             'nr2'] and len(temp) <3 and not enstart:
            if words[i].word not in stopwords:
                temp = temp + words[i].word
            if i == len(words) - 1:
                if temp.strip() != '':
                    words2.append(temp)
        else:
            if temp.strip() != '' and not enstart:
                words2.append(temp)
                temp = ''
    return words2

def text_process_en(text):
    text = re.sub('\u3000|\r|\t|\xa0|\n', '', text)
    text = text.replace(',', ' ')
    text_list = text.split()
    texter = Text(text_list)
    text_n_list = texter.collocations()
    return text_n_list

def range_easy(a_object):
    return range(len(a_object))

def duplicate(a_list):
    return list(set(a_list))