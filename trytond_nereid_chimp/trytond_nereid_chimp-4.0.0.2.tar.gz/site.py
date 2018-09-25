# -*- coding: UTF-8 -*-
'''
    nereid_mailchimp.site

    MailChimp configuration fields in site

'''
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['WebSite']
__metaclass__ = PoolMeta


class WebSite:
    """MailChimp config fields in website
    """
    __name__ = "nereid.website"

    mailchimp_api_key = fields.Char('MailChimp API Key')
    mailchimp_default_list = fields.Char('Default List Name')
