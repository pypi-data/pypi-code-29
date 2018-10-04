#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      mongo_client.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    tangmi(tangmi360@gmail.com)
    @date:      June 4, 2018
    @desc:      Mongodb storage access class
"""

from motor.motor_asyncio import AsyncIOMotorClient


"""
mc = MongoClient(host=27.0.0.1:27017,
                 authSource='mydb',
                 username='user', password='pwd')
db = mc.db
collection = db.collection
doc = await collection.find_one()
"""

class MongoClient(AsyncIOMotorClient):

    def __init__(self, *args, **kwargs):
        if kwargs.get('authMechanism') == None:
            kwargs['authMechanism'] = 'SCRAM-SHA-1'
        super(MongoClient, self).__init__(*args, **kwargs)
