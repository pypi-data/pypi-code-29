import shutil

from sqlalchemy.pool import StaticPool
from series.db import Database
from series.library import LibraryFacade

from amino.test import fixture_path, temp_file

from unit.library._support.spec import Spec


class DBTestMixin:

    def setup(self):
        self._db = Database('series.library', 'sqlite://', poolclass=StaticPool, auto_upgrade=False)
        self._db.commit()
        self._lib = LibraryFacade(self._db)

    def teardown(self):
        self._db.disconnect()


class DBSpec(DBTestMixin, Spec):

    def setup(self) -> None:
        Spec.setup(self)
        DBTestMixin.setup(self)


def clone_migration_snapshot(rev):
    components = 'library', 'db', 'v{}.db'.format(rev)
    original = fixture_path(*components)
    clone = temp_file(*components)
    return shutil.copy(str(original), str(clone))


def create_migration_snapshot(source, rev):
    components = 'library', 'db', 'v{}.db'.format(rev)
    target = fixture_path(*components)
    return shutil.copy(str(source), str(target))
