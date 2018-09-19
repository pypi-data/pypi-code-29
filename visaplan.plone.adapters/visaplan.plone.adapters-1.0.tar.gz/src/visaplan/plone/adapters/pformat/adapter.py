# -*- coding: utf-8 -*-
# Adapter pformat: Zugriff auf die Standardfunktion pprint.pformat
from visaplan.plone.base import Base, Interface
from pprint import pformat

class IPFormat(Interface):
    pass

class Adapter(Base):

    def __call__(self, *args, **kwargs):
        return pformat(*args, **kwargs)

#  vim: ts=8 sts=4 sw=4 si et tw=79
