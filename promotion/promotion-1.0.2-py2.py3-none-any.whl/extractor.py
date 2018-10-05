#-*- coding:utf-8 -*-

""" 各类新闻类网站的正文抽取 """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import re
import requests

__author__ = "TANG BIN <bintang.hit@gmail.com>"
__date__ = "1 Oct 2018"


class BaseExtractor(object):
    def __init__(self):
        pass


    def extract(self, response):
        raise NotImplementedError


class News163Extractor(BaseExtractor):
    def __init__(self):
        super(News163Extractor, self).__init__()
        self.hyperlink_remover = re.compile('</?a[^>]*>')


    def extract(self, response):
        title = response.doc('title').text().rstrip('_网易新闻')
        text = str(response.doc('div[id="endText"]'))
        text = self.hyperlink_remover.sub('', text)
        return {'title': title, 'text': text}


class ToutiaoExtractor(BaseExtractor):
    def __init__(self):
        super(ToutiaoExtractor, self).__init__()


    def extract(self, response):
        pass


class TencentNewsExtractor(BaseExtractor):
    def __init__(self):
        super(TencentNewsExtractor, self).__init__()


    def extract(self, response):
        pass


class SouhuNewsExtractor(BaseExtractor):
    def __init__(self):
        super(SouhuNewsExtractor, self).__init__()

    def extract(self, response):
        pass


class TaobaoExtractor(BaseExtractor):
    def __init__(self):
        super(TaobaoExtractor, self).__init__()

    def extract(self, response):
        pass



