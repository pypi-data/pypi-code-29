from datetime import datetime, timedelta

from flexmock import flexmock

from series.get.torrent_cleaner import TorrentCleaner
from series.get.model.release import ReleaseFactory, Release
from series.util import datetime_to_unix
from series.get.search import TorrentSearch
from series.get.test.torrent import caching, downloadable

from tek_utils.sharehoster.torrent import SearchResult

from golgi import Config

from amino import List

from unit.get._support.db import DBTestMixin
from unit.get._support.spec import Spec


class TorrentCleanerSpec(DBTestMixin, Spec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        Config.override('torrent', cacher='spec')
        self._cleaner = TorrentCleaner(self._releases)

    def _before_monitors(self):
        Config.override('get', full_hd=False, min_seeders=3)

    @property
    def _name1(self):
        return 'Series1.S01E05.720p'

    @property
    def _name2(self):
        return 'Series1.S01E05'

    @property
    def _magnet1(self):
        return 'magnet:?xt=urn:btih:111&dn={}'.format(self._name1)

    @property
    def _magnet2(self):
        return 'magnet:?xt=urn:btih:222&dn={}'.format(self._name2)

    @property
    def _monitors(self):
        epi = dict(title='series1_s01e05', name='series1',
                   season=1, episode=5, is_series=True)
        link = [self._magnet1]
        last = datetime_to_unix(datetime.now() - timedelta(days=3))
        return List(
            ReleaseFactory().monitor(Release(**epi), [], link, downgrade_after=2, last_torrent_update_stamp=last)
        )

    @property
    def _release(self):
        return self._releases.all[0]

    def _mock_results(self, results):
        self._mock_search = flexmock(TorrentSearch)
        self._mock_search.should_receive('_search_kickass').and_return(results)

    def add_link(self):
        results = List(
            SearchResult('series1_s01e05_720p', 100000000, '100M', 500, self._magnet1),
            SearchResult('series1_s01e05', 100000000, '100M', 500, self._magnet2),
        )
        self._mock_results(results)
        self._release.resolutions.should.have.length_of(1)
        self._cleaner._check()
        self._release.resolutions.should.have.length_of(2)

    def describe(self):
        results = List(
            SearchResult('series1_s01e05_720p', 100000000, '100M', 500, self._magnet1),
            SearchResult('series1_s01e05', 100000000, '100M', 500, self._magnet2),
        )
        self._mock_results(results)
        self.log.info(self._cleaner.explain(self._release)['cond'])
        self._releases.update_by_id(self._release.id, downgrade_after=None)
        self.log.info(self._cleaner.explain(self._release)['cond'])

    def reset(self):
        results = List(
            SearchResult('series1_s01e05_720p', 100000000, '100M', 500, self._magnet1),
            SearchResult('series1_s01e05_720p', 100000000, '100M', 500, self._magnet2),
        )
        self._mock_results(results)
        flexmock(self._cleaner).should_call('_alternative_hd_releases').once()
        self._cleaner._check()
        self._release.torrent_links[0].dead.should.be.true
        self._cleaner._check()

    def aborted(self):
        caching[self._magnet1] = False
        downloadable[self._magnet1] = False
        self._releases.update_by_id(1, downgrade_after=0)
        self._releases.update_link(1, caching=True)
        self._cleaner._check()

__all__ = ('TorrentCleanerSpec',)
