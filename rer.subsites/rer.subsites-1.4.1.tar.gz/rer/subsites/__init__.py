# -*- coding: utf-8 -*-
"""Init and utils."""

from logging import getLogger
from zope.i18nmessageid import MessageFactory


subsitesMessageFactory = MessageFactory('rer.subsites')
logger = getLogger('rer.subsites')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
