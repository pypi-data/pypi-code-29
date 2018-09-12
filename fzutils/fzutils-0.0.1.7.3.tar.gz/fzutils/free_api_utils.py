# coding:utf-8

'''
@author = super_fazai
@File    : free_api_utils.py
@connect : superonesfazai@gmail.com
'''

"""
一些免费api 接口的封装
"""

from .spider.fz_requests import Requests
from .common_utils import json_2_dict

def get_jd_one_goods_price_info(goods_id):
    '''
    京东获取单个商品价格
    :param goods_id:
    :return:
    '''
    base_url = 'http://p.3.cn/prices/mgets'
    params = (
        ('skuIds', 'J_' + goods_id),
    )

    body = Requests.get_url_body(url=base_url, use_proxy=False, params=params)

    return json_2_dict(body)


