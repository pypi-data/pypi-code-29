from pathlib import Path

import sure  # NOQA
from flexmock import flexmock  # NOQA

import sqlalchemy


from series.library.db import FileDatabase
from series.library.library_facade import LibraryFacade

from unit.library._support.db import (clone_migration_snapshot,
                                       create_migration_snapshot)
from unit.library._support.spec import Spec


class Db_(Spec):

    class migrations(Spec):

        def setup(self, *a, **kw):
            self._parent.setup(self, *a, **kw)

        def migrate_to_head(self):
            db_file = clone_migration_snapshot(1)
            db = FileDatabase(Path(db_file), auto_upgrade=False)
            lib = LibraryFacade(db)
            lib.episodes.when.called_with().should.throw(
                sqlalchemy.exc.OperationalError)
            db.disconnect()
            db.upgrade('head')
            db.connect()
            lib.episodes()[0].removed.should.be.false
            lib.episodes()[0].subfps.should.equal('')

class _RevisionsSpec(Spec):

    def revision(self, snapshot, message):
        db_file = clone_migration_snapshot(snapshot)
        FileDatabase(Path(db_file), connect=False).revision(message)
        create_migration_snapshot(db_file, snapshot + 1)

    def metadata(self):
        message = 'add metadata attributes'
        self.revision(1, message)

    def stopped_at(self):
        message = 'add WatchEvent.stopped_at column'
        self.revision(2, message)

    def episode_subdelay(self):
        message = 'add Episode.subdelay'
        self.revision(3, message)


__all__ = ['Db_']
