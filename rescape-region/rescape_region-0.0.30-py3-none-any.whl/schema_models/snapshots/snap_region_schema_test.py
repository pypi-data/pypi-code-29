# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['RegionSchemaTestCase::test_create 1'] = {
    'boundary': {
        'geometryCollection': {
        }
    },
    'data': {
    },
    'id': '2',
    'key': 'luxembourg',
    'name': 'Luxembourg'
}

snapshots['RegionSchemaTestCase::test_update 1'] = {
    'boundary': {
        'geometryCollection': {
        }
    },
    'data': {
    },
    'id': '6',
    'key': 'luxembourg',
    'name': 'Luxembourg'
}
