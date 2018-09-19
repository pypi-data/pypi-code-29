# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from udata.models import db


class UserLdap(db.EmbeddedDocument):
    id = db.StringField()
