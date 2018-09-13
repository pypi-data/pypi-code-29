#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : models.py
# @Date : 2018/9/4 13:52
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

Base = declarative_base()
metadata = Base.metadata


class IfDatabaseRole(Base):
    __tablename__ = 'user'
    attributes = ['id', 'name', 'age', 'email']
    detail_attributes = attributes
    summary_attributes = attributes

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)
    email = Column(String(255))
