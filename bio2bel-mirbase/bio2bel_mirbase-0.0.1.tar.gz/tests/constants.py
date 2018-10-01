# -*- coding: utf-8 -*-

"""Test constants for Bio2BEL miRBase."""

import json
import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_mirbase import Manager

HERE = os.path.dirname(os.path.realpath(__file__))
MOCK_JSON = os.path.join(HERE, 'mirbase_test.json')


class TemporaryCacheClass(AbstractTemporaryCacheClassMixin):
    """A test case containing a temporary database and a Bio2BEL miRBase manager."""

    Manager = Manager

    @classmethod
    def populate(cls):
        """Populate the mock database."""
        with open(MOCK_JSON) as file:
            cls.manager._populate_list(json.load(file))
