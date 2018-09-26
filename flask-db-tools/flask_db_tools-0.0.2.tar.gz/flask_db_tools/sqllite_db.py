# -*- coding: utf-8 -*-

from migrate.versioning import api
import os.path
import imp


class DBTools(object):

    def __init__(self, db, database_uri, migrate_repo):
        self.db = db
        self.database_uri = database_uri
        self.migrate_repo = migrate_repo

    def create_db(self):
        self.db.create_all()
        if not os.path.exists(self.migrate_repo):
            api.create(self.migrate_repo, 'database repository')
            api.version_control(self.database_uri, self.migrate_repo)
        else:
            api.version_control(self.database_uri, self.migrate_repo, api.version(self.migrate_repo))

    def migrate_db(self):
        migration = self.migrate_repo + '/versions/%03d_migration.py' % (
        api.db_version(self.database_uri, self.migrate_repo) + 1)
        tmp_module = imp.new_module('old_model')
        old_model = api.create_model(self.database_uri, self.migrate_repo)
        exec old_model in tmp_module.__dict__
        script = api.make_update_script_for_model(self.database_uri, self.migrate_repo, tmp_module.meta,
                                                  db.metadata)
        open(migration, "wt").write(script)
        api.upgrade(self.database_uri, self.migrate_repo)
        print 'New migration saved as ' + migration
        print 'Current database version: ' + str(api.db_version(self.database_uri, self.migrate_repo))

    def upgrade_db(self):
        v = api.db_version(self.database_uri, self.migrate_repo)
        api.downgrade(self.database_uri, self.migrate_repo, v - 1)
        print 'Current database version: ' + str(api.db_version(self.database_uri, self.migrate_repo))




