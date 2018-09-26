# -*- coding:utf-8 -*-

import six
import numpy as np
try:
    from django.contrib.gis import geos
    HAS_GEODJANGO = True
except ImportError:
    HAS_GEODJANGO = False


def to_geos_multi_polygon(region):
    if not HAS_GEODJANGO:
        raise RuntimeError("Requires GeoDjango!")

    pass


def gen_region_mask(region, x, y):
    pass

