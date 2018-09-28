# -*- coding: utf-8 -*-
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from plone.indexer.decorator import indexer

from collective.smartlink.behaviors.interfaces import ISmartLinkExtension
from collective.smartlink import logger


@indexer(ISmartLinkExtension)
def getRemoteUrl(obj):
    if obj.internal_link and obj.remoteUrl and obj.remoteUrl != "http://":
        logger.warning(
            'for the %s link there are both internal:%s and external:%s url',
            obj.absolute_url(), obj.internal_link.to_path, obj.remoteUrl)
    if obj.internal_link:
        return obj.internal_link.to_path
    else:
        return replace_link_variables_by_paths(obj, obj.remoteUrl)
