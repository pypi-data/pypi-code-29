import threading

import sure  # NOQA
from flexmock import flexmock
import httpretty

import sqlalchemy

from golgi import Configurations
from amino.test import temp_dir, temp_file
from amino.test.spec_spec import later
from unit.get._support.spec import Spec

from tek_utils import sharehoster
from tek_utils.sharehoster.common import Downloader

from series.get.model.link import Link, Torrent
from series.get.db import FileDatabase
from series.get.model.release import ReleaseMonitor
from series.get import SeriesGetD, ReleasesFacade

from unit.get._support.db import (clone_migration_snapshot,
                                  create_migration_snapshot)
from unit._fixtures.get.monitors import monitors_1


class MigrationsSpec(Spec):

    def _migrate_to_head(self):
        db_file = clone_migration_snapshot(1)
        db = FileDatabase(db_file, connect=False)
        db.connect(create=False)
        cached_access = lambda: db.query(Torrent).first().cached
        cached_access.when.called_with().should.throw(
            sqlalchemy.exc.OperationalError)
        db.upgrade('head')
        db.connect()
        link = db.query(Torrent).first()
        link.cached.should_not.be.ok


class ReopeningSpec(Spec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        (flexmock(sharehoster.DownloaderFactory)
            .should_receive('__call__')
            .replace_with(Downloader))
        (flexmock(Link)
            .should_receive('valid')
            .and_return(True))
        download_dir = temp_dir('get', 'db', 'download')
        Configurations.override('get', download_dir=download_dir,
                                min_size=0, auto_upgrade_db=False,
                                run=['downloader'])
        Configurations.override('sharehoster', link_checker_url=None)
        path = temp_file('get', 'db', 'persistence', 'db')
        Configurations.override('get', db_path=path)

    @httpretty.activate
    def downloaded_flag_persistence(self):
        get = SeriesGetD()
        get.downloader._interval = 0.5
        get.downloader._initial_wait = 0
        db = get.db
        db.load_data(monitors_1())
        for monitor in get.releases.all:
            httpretty.register_uri(httpretty.GET, monitor.link.url,
                                   body='success')
        threading.Thread(target=get.run).start()
        later(lambda: get.releases.all[0].downloaded.should.be.ok, timeout=5)
        get.interrupt(0, 0)
        db = FileDatabase(temp_file('get', 'db', 'persistence', 'db'),
                          auto_upgrade=False)
        monitor = db.query(ReleaseMonitor).first()
        monitor.downloaded.should.be.true


class _RevisionsSpec(Spec):

    def add_data(self):
        db_file = clone_migration_snapshot(1)
        db = FileDatabase(db_file, auto_upgrade=False)
        db.load_data(monitors_1())
        releases = ReleasesFacade(db, sync=True)
        releases.add_link(releases.all[0], 'magnet:xfoobar')
        create_migration_snapshot(db_file, 1)

    def revision(self, snapshot, message):
        db_file = clone_migration_snapshot(snapshot)
        FileDatabase(db_file, connect=False).revision(message)
        create_migration_snapshot(db_file, snapshot + 1)

    def torrent_link_cached(self):
        message = 'add Torrent.cached'
        self.revision(1, message)

    def release_monitor_added_to_library(self):
        message = 'add ReleaseMonitor.added_to_library'
        self.revision(2, message)

    def release_monitor_last_torrent_search_stamp(self):
        message = 'add ReleaseMonitor.last_torrent_search_stamp'
        self.revision(3, message)

    def release_monitor_airdate_stamp(self):
        message = 'add ReleaseMonitor.airdate_stamp'
        self.revision(4, message)

    def show_etvdb_id(self):
        message = 'add Show.etvdb_id'
        self.revision(5, message)

    def torrent_link_dead(self):
        message = 'add Torrent.dead'
        self.revision(6, message)

    def release_monitor_resolutions(self):
        message = 'add ReleaseMonitor._resolutions'
        self.revision(7, message)

    def remove_link_polymorphism(self):
        message = 'remove link polymorphism'
        self.revision(8, message)

    def downgrade_after(self):
        message = 'add downgrade_after'
        self.revision(9, message)

    def release_show_search_name(self):
        message = 'add search_name to Release and Show'
        self.revision(10, message)

    def release_monitor_activated(self):
        message = 'add activated to ReleaseMonitor'
        self.revision(11, message)

__all__ = ('ReopeningSpec', 'MigrationsSpec')
