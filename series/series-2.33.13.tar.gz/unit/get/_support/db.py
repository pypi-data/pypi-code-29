import shutil
from pathlib import Path

from sqlalchemy.pool import StaticPool
from series.get.db import Database
from series.get import ReleasesFacade

from amino.test import fixture_path, temp_file

from unit._fixtures.get.monitors import monitors_1
from unit.get._support.spec import Spec


class DBTestMixinBase():

    def _setup_db(self) -> None:
        self._db = Database(auto_upgrade=False, poolclass=StaticPool)
        self._releases = ReleasesFacade(self._db)

    def setup(self) -> None:
        self._setup_db()


class DBTestMixin(DBTestMixinBase):

    def setup(self):
        DBTestMixinBase.setup(self)
        self._before_monitors()
        self._db.load_data(self._monitors)
        self._db.commit()

    @property
    def _monitors(self):
        return monitors_1()

    def _before_monitors(self):
        pass


class DBBaseSpec(DBTestMixinBase, Spec):

    def setup(self) -> None:
        Spec.setup(self)
        DBTestMixinBase.setup(self)


class DBSpec(DBTestMixin, Spec):

    def setup(self) -> None:
        Spec.setup(self)
        DBTestMixin.setup(self)


def clone_migration_snapshot(rev):
    components = 'get', 'db', 'v{}.db'.format(rev)
    original = fixture_path(*components)
    clone = temp_file(*components)
    return Path(shutil.copy(str(original), str(clone)))


def create_migration_snapshot(source, rev):
    components = 'get', 'db', 'v{}.db'.format(rev)
    target = fixture_path(*components)
    return Path(shutil.copy(str(source), str(target)))
