#coding=utf-8

from fmtlabels.fmt import analyze
from fmtlabels.fmt import marshal
from fmtlabels.fmt import aspect_mapping
import json


def lbl_fmtlines(output, category, mapping, input):
    for text in input:
        if text == '':
            continue
        data = {text : analyze(category, text)}
        if mapping:
            aspect_mapping(category, data)
        marshal(output, category, data)
