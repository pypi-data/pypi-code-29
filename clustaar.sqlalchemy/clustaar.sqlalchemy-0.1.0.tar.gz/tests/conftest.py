from __future__ import print_function, absolute_import, division

import os
import pytest

PROJECT_PATH = os.path.join(os.path.dirname(__file__), "..")
PACKAGE_PATH = os.path.join(PROJECT_PATH, "src")

os.sys.path.insert(0, PROJECT_PATH)
os.sys.path.insert(0, PACKAGE_PATH)

from tests.utils import create_database  # NOQA


db = create_database()
db.setup_all()


@pytest.fixture(scope="module")
def database():
    return db


def pytest_runtest_setup(item):
    db.truncate_tables()
