#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Peng Yong
# @Date: 2018-10-08
# @Github username: @ppengkkang
# @Last Modified time: 2018-10-08


import re
import nltk
from unidecode import unidecode

def generate_tree(text, grammar):
    text = unidecode(text)
    chunker = nltk.RegexpParser(grammar)
    tokenized_text = nltk.tokenize.word_tokenize(text)
    postokens = nltk.tag.pos_tag(tokenized_text)
    tree = chunker.parse(postokens)
    return tree


def leaves(text,grammar,label):
    for subtree in generate_tree(text,grammar).subtrees(filter = lambda t: t.label() == label):
        yield subtree.leaves()

def get_terms(text, grammar,label):
    for leaf in leaves(text,grammar,label):
        term = [ w for w,t in leaf]
        yield term

def get_phrases(text, grammar, label):
    """ Extract important keywords, returns a list"""
    text = text.replace('“', '"') #to preserve quotes in text, primarily news content
    text = text.replace('”', '"')
    text = text.replace('’', "'")
    text = unidecode(text)
    terms = get_terms(text,grammar,label)
    phrases = []
    for all_terms in terms:
        phrase = re.sub('\s+', ' ', " ".join(all_terms)).strip()
        if len(phrase.split()) > 1:
            phrases.append(phrase)
        else:
            pass
    return phrases

