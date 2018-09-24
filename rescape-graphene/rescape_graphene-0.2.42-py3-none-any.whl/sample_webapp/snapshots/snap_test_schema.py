# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['GenaralTypeCase::test_create 1'] = {
    'email': '',
    'firstName': 'T',
    'isActive': True,
    'isStaff': False,
    'isSuperuser': False,
    'lastName': 'Rex',
    'username': 'dino'
}

snapshots['GenaralTypeCase::test_create_user 1'] = {
    'firstName': 'T',
    'isActive': True,
    'lastName': 'Rex',
    'username': 'dino'
}

snapshots['GenaralTypeCase::test_create_foo 1'] = {
    'data': {
        'example': 1.5,
        'friend': {
        }
    },
    'geoCollection': {
    },
    'key': 'luxembourg',
    'name': 'Luxembourg',
    'user': {
    }
}

snapshots['GenaralTypeCase::test_update 1'] = {
    'firstName': 'Al',
    'isActive': True,
    'lastName': 'Lissaurus',
    'username': 'dino'
}
