# coding:utf-8

'''
@author = super_fazai
@File    : free_api_utils.py
@connect : superonesfazai@gmail.com
'''

"""
一些免费api 接口的封装
"""

from requests import get

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



