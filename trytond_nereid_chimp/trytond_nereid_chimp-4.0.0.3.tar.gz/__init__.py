# -*- coding: utf-8 -*-
'''
    Nereid Integration with MailChimp

'''
from trytond.pool import Pool
from site import WebSite
from party import NereidUser


def register():
    Pool.register(
        WebSite,
        NereidUser,
        module='nereid_chimp', type_='model'
    )
