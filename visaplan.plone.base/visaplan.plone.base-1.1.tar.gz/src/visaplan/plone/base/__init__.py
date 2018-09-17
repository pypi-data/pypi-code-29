"""\
visaplan.plone.base: simple base modules
"""
# "BrowserView implements Interface":
from .browserview import BrowserView
from zope.interface import implements, Interface
from .adapter import Base

from Products.CMFCore.utils import getToolByName
