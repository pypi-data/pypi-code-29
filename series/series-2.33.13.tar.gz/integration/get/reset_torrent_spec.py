import re

from flexmock import flexmock

import httpretty

from golgi import Config
from amino.test import temp_dir, temp_file
from amino.test.spec_spec import later
from amino.lazy import lazy

from series.get import SeriesGetD
from series.get.search import TorrentSearch
import series.get.test.torrent  # NOQA

from unit.get._support.link import LinkTestMixin
from unit._fixtures.get.monitors import monitors

from integration._support.spec import Spec


class ResetTorrentSpecBase(Spec):

    def setup(self):
        super().setup()
        self.download_dir = temp_dir('get', 'db', 'download')
        Config.override('get', download_dir=self.download_dir, min_size=0, auto_upgrade_db=False)
        Config.override('torrent', cacher='spec')
        path = temp_file('get', 'db', 'integration', 'db')
        Config.override('get', db_path=path)
        self._series_dir = temp_dir('series', 'archiver', 'series')

    @property
    def _torrent1(self):
        return 'magnet:first'

    @property
    def _torrent2(self):
        return 'magnet:second'

    @property
    def _monitors(self):
        epi = dict(title='the.showname.s01e05', name='the_showname', group='guppy', season=1, episode=5, is_series=True,
                   resolution='1080p')
        release_data = [epi]
        return list(monitors(release_data, [[]], [[self._torrent1]]))

    @property
    def release(self):
        return self._releases.all[0]

    def _good_links(self, num):
        later(lambda: len(self.release.cachable_torrents) == num)

    @property
    def _wait_dlable(self):
        return lambda: later(lambda: self.release.downloadable.should.be.ok, timeout=10)

    @property
    def _wait_dld(self):
        return lambda: later(lambda: self.release.downloaded.should.be.ok,
                             timeout=10)

    def _init(self, add=[]):
        services = ['torrent_handler', 'archiver', 'downloader', 'torrent_cleaner']
        Config.override('get', run=services + add, library=False)
        Config.override('series', series_dir=self._series_dir)
        get = SeriesGetD()
        self._releases = get.releases
        get.torrent_handler._initial_wait = 0
        get.torrent_handler._interval = 0.5
        get.archiver._initial_wait = 0
        get.archiver._interval = 0.5
        get.downloader._initial_wait = 0
        get.downloader._interval = 0.5
        get.db.load_data(self._monitors)
        httpretty.register_uri(httpretty.GET, re.compile('.*first.*'), body='first')
        httpretty.register_uri(httpretty.GET, re.compile('.*second.*'), body='second')
        return get

    @lazy
    def _out(self):
        return self._series_dir / 'the.showname' / 's1' / 'the.showname_01x05.mkv'

    def _out_content(self, data):
        later(lambda: self._out.is_file() and self._out.read_text() == data)


class ResetTorrentSpec(LinkTestMixin, ResetTorrentSpecBase):

    @httpretty.activate
    def _check(self):
        (
            flexmock(TorrentSearch)
            .should_receive('_search_kickass')
            .and_return([])
        )
        get = self._init()
        get.start()
        self._wait_dld()
        self._out_content('first')
        self._releases.reset_torrent(1)
        self._good_links(0)
        later(lambda: not self.release.downloadable)
        self._releases.add_torrent_by_id(1, self._torrent2)
        self._wait(0.1)
        later(lambda: self.release.torrent_links[-1].caching.should.be.true)
        self._wait_dld()
        get.interrupt()
        self._out_content('second')

__all__ = ('ResetTorrentSpec',)
