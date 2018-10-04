#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      mongo_helper.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    tangmi(tangmi360@gmail.com)
    @date:      September 04, 2018
    @desc:      Mongo Helper
"""

from tomato.store.item import Item


class MongoHelper(object):

    def __init__(self, *args, **kwargs):
        self.key_map = {}
        self._coll = args[0]

    def mapping(self, item, result=None):
        if result == None:
            result = {}
        for k, v in item.items():
            k = self.key_map.get(k, k)
            if isinstance(v, dict):
                result[k] = {}
                mapping(v, result[k])
            else:
                result[k] = v
        return result

    async def insert_one(self, item: Item):
        await self._coll.insert_one(item)

    async def update_one(self, key, item: Item, upsert=True):
        await  self._coll.update_one(key, item, upsert=upsert)

    async def query_data(self, key=None, sort=None, start=0, limit=0):
        data_list = []
        async for doc in self._coll.find(key, sort=sort, skip=start, limit=limit):
            item = Item()
            item.data = doc
            data_list.append(item)
        return data_list

    async def query_by_id(self, _id):
        doc = await self._coll.find_one({'_id': ObjectId(_id)})
        item = Item()
        item.data = doc
        return item
