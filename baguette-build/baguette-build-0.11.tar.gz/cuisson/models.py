#-*- coding:utf-8 -*-
import datetime
from farine.connectors.sql import *#pylint:disable=wildcard-import,unused-wildcard-import

class Build(Model):
    """
    Build table representation:
     - uid
     - owner
     - repo
     - branch
     - date_created
    """
    uid = UUIDField(primary_key=True)
    owner = CharField()
    repo = CharField()
    branch = CharField()
    date_created = DateTimeField(default=datetime.datetime.now)

class Status(Model):
    """
    Status table representation:
     - uid
     - status
     - context
     - fail
     - date_created
    """
    uid = ForeignKeyField(Build)
    status = CharField()
    fail = BooleanField(default=False)
    context = JSONField()
    date_created = DateTimeField(default=datetime.datetime.now)
