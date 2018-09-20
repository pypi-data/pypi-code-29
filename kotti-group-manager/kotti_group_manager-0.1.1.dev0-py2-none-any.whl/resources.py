# -*- coding: utf-8 -*-

"""
Created on 2018-09-19
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Document
from kotti.security import get_principals
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from kotti_group_manager import _


class GroupPage(Document):
    """ A custom content type. """

    implements(IDefaultWorkflow)

    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    group_name = Column(Unicode(100), ForeignKey('principals.name'))

    type_info = Document.type_info.copy(
        name=u'GroupPage',
        title=_(u'Group Page'),
        add_view=u'add_group_page',
        addable_to=[u'Document', u'Content']
    )

    @property
    def group(self):
        principals = get_principals()
        group = principals.search(name=self.group_name).first()
        return group
    
    @property
    def group_id(self):
        return self.group_name.replace("group:", '')
        