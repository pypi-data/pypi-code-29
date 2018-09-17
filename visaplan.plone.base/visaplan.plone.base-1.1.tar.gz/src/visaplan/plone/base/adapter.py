# -*- coding: utf-8 -*- äöü vim: sw=4 sts=4 ts=8 scrolloff=3 cul si
from Products.CMFCore.utils import getToolByName
from .mixin import GetContextMixin


class Base(GetContextMixin):
    def __init__(self, context):
	self.context = context
