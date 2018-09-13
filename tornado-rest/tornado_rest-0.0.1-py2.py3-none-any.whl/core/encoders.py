#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : encoders.py
# @Date : 2018/9/6 10:20
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import json
from sqlalchemy.orm.query import Query


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Query):
            fields = []
            for rec in obj.all():
                record = {}
                for field in [x for x in dir(rec) if
                              not x.startswith('_')
                              and hasattr(rec.__getattribute__(x), '__call__') == False
                              and x != 'metadata'
                              and ('attributes' not in x)]:
                    data = rec.__getattribute__(field)
                    try:
                        record[field] = data
                    except TypeError:
                        record[field] = None
                fields.append(record)
            return fields
        return json.JSONEncoder.default(self, obj)
