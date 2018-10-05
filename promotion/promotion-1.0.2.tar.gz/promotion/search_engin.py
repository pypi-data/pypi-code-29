#-*- coding:utf-8 -*-

""" 提供各种搜索引擎关键词搜索结果 """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import requests
from urllib.parse import quote

__author__ = "TANG BIN <bintang.hit@gmail.com>"
__date__ = "24 Sep 2018"


__all__ = [
    'SearchEnginBase',
    'BaiduSearchEngin',
]


class SearchEnginBase(object):
    def index_page(self, keywords):
        """ 获取关键词搜索结果页
        
        Aargs:
            keywords: 搜索关键词列表

        Returns:
            搜索结果页链接
        """
        raise NotImplementedError


    def next_page(self, response):
        """ 返回下一页链接 """
        raise NotImplementedError


    def results(self, response):
        """ 获取搜索结果列表

        Returns:
            搜索结果列表，每条结果是一个dict
        """
        raise NotImplementedError


class BaiduSearchEngin(SearchEnginBase):
    def __init__(self):
        super(BaiduSearchEngin, self).__init__()


    def index_page(self, keywords):
        keywords = quote(' '.join(keywords))
        return 'https://www.baidu.com/baidu?wd=%s&tn=monline_dg&ie=utf-8' % keywords


    def next_page(self, response):
        items = list(response.doc('a[class="n"]').items())
        if len(items) == 0:
            print(response.doc())
            return None
        else:
            if items[-1].attr.href.strip().startswith('http'):
                return items[-1].attr.href.strip()
            return 'https://www.baidu.com' + items[-1].attr.href.rstrip()


    def results(self, response):
        for item in response.doc('a[class="c-showurl"]').items():
            header = requests.head(item.attr.href.rstrip()).headers
            url = header['Location']
            yield {'url': url}


