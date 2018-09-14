import os
import shutil

import sure  # NOQA
from flexmock import flexmock  # NOQA

from golgi import Config

from series.get.archiver import Archiver
from series.get.errors import ArchiverError
from unit.get._support.db import DBSpec
from amino.test import temp_file, temp_dir


class ArchiverSpec(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        path_template = '{name}_{season}/{name}_{season}x{episode}.{ext}'
        self._series_dir = temp_dir('series', 'archiver', 'series')
        Config.override('series', series_dir=self._series_dir)
        Config.override('get', path_template=path_template, library=False)
        self._dest_path = (temp_dir(self._series_dir, 'series1_1') /
                           'series1_1x5.mkv')
        self._download_dir = temp_dir('series', 'archiver', 'download')
        self._archiver = Archiver(self._releases)
        self._monitor = self._releases.all[0]

    def format_a_series_path(self):
        path = self._archiver._format_path(self._monitor)
        path.should.equal(self._dest_path)

    def store_a_file(self):
        download_path = self._download_dir / 'store_test'
        with download_path.open('w') as _file:
            _file.write('success')
        self._monitor.download_path = download_path
        self._archiver._store(self._monitor, self._dest_path)
        with self._dest_path.open() as _file:
            _file.read().should.equal('success')

    def external_archiver(self):
        self._monitor.download_path = 'name with whitespace'
        self._monitor.release.name = 'it\'s sunny'
        Config.override(
            'get', archive_exec='/bin/true',
            archive_exec_args=
            '{download_path} --foo="{name} {season} {episode}"')
        self._archiver._archive(self._monitor)

    class check_downloaded_file(object):

        def setup(self):
            self._monitor.download_path = str(self._download_dir / 'series1_1x5.mkv')

        def download_missing(self):
            (self._archiver._check_downloaded_file
             .when.called_with(self._monitor, self._dest_path)
             .should.throw(ArchiverError))
            self._monitor.archived.should.be.false

        def download_missing_and_archived_existing(self):
            with self._dest_path.open('w') as _file:
                _file.write('success')
            (self._archiver._check_downloaded_file
             .when.called_with(self._monitor, self._dest_path)
             .should.throw(ArchiverError))
            self._monitor.archived.should.be.true

        def download_existing(self):
            with open(self._monitor.download_path, 'w') as _file:
                _file.write('success')
            (self._archiver._check_downloaded_file
             .when.called_with(self._monitor, self._dest_path)
             .should_not.throw(ArchiverError))
            self._monitor.archived.should.be.false

    class check_target_dir(object):

        def existing_file(self):
            _path = temp_file('check_target_dir')
            with _path.open('w') as _file:
                _file.write('success')
            (self._archiver._check_target_dir.when.called_with(_path)
             .should.throw(ArchiverError))

        def existing_dir(self):
            _path = temp_dir('check_target_dir')
            (self._archiver._check_target_dir.when.called_with(_path)
             .should_not.throw(ArchiverError))

        def nonexisting(self):
            _path = temp_dir('check_target_dir')
            shutil.rmtree(str(_path))
            (self._archiver._check_target_dir.when.called_with(_path)
             .should_not.throw(ArchiverError))

__all__ = ('ArchiverSpec',)
