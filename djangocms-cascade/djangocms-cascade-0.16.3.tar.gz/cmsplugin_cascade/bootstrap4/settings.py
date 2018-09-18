# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


def set_defaults(config):
    config.setdefault('bootstrap4', {})
    config['bootstrap3'].setdefault(
        'breakpoints', (
            ('xs', (768, 'mobile', _("mobile phones"), 750, 768)),
            ('sm', (768, 'tablet', _("tablets"), 750, 992)),
            ('md', (992, 'laptop', _("laptops"), 970, 1200)),
            ('lg', (1200, 'desktop', _("large desktops"), 1170, 1980)),))

    config['bootstrap4'].setdefault('gutter', 30)
