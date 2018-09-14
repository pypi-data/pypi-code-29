from datetime import date, datetime
from flexmock import flexmock

from golgi import Config

from tek_utils.sharehoster.torrent import SearchResult

from amino import List, _
from amino.test.spec_spec import later

from series.get import ShowsFacade
from series.get.torrent_finder import TorrentFinder, SearchQuery
from series.get.search import SearchResults, TorrentSearch

from unit.get._support.db import DBTestMixinBase
from unit.get._support.spec import Spec


class TorrentFinderSpec(DBTestMixinBase, Spec):

    def setup(self):
        DBTestMixinBase.setup(self)
        Spec.setup(self)
        self._shows = ShowsFacade(self._db)
        self._finder = TorrentFinder(self._releases)
        Config.override('get', full_hd=False, min_seeders=3)
        self._releases.create('the_showname', 1, 5, datetime.now())
        self.hd7_title = 'the.showname.s01e05.720p.mkv'

    def _mock_results(self, f):
        (
            flexmock(TorrentSearch)
            .should_receive('_search')
            .and_return(lambda self, q: f())
        )

    def _results_present(self):
        (self._finder._async / _.proc / _.done.value).should.contain(True)

    def _run_search(self):
        self._finder._check()
        later(self._results_present)
        self._finder._check()

    def add_link(self):
        results = [SearchResult(self.hd7_title, 100000000, '100M', 500,
                                'magnet:?xt=urn:btih:23425623141234124')]
        self._mock_results(lambda: results)
        self._run_search()
        self._releases[0].torrents[-1].url.should.equal(results[0].magnet_link)

    def date_enum(self):
        stamp = date.today().strftime('%F')
        f = flexmock(self._finder)
        res = iter([List(),
                    List(SearchResult('the.showname.{}.720p'.format(stamp),
                                      100000000, '100M', 500,
                                      'magnet:?xt=urn:btih:23425623141234124'))
                    ])
        self._mock_results(lambda: next(res))
        f.should_call('_process_results').twice()
        f.should_call('_add_link').once()
        self._run_search()

    def reset_torrent(self):
        results = [SearchResult(self.hd7_title, 10e8, '100M', 500, 'magnet:?xt=urn:btih:23425623141234124')]
        self._mock_results(lambda: results)
        self._run_search()
        later(lambda: self._releases[0].cachable_torrents.should_not.be.empty)
        self._releases.reset_torrent(1)
        self._run_search()
        later(lambda: self._releases[0].cachable_torrents.should.be.empty)

    def year_suffix(self):
        magnet = 'magnet:?xt=urn:btih:23425623141234124'
        results = [SearchResult('the.showname.2016.s01e05.720p.mkv', 100000000, '100M', 500, magnet)]
        self._mock_results(lambda: results)
        self._run_search()
        self._releases[0].torrents[-1].url.should.equal(results[0].magnet_link)

    def min_seeders(self):
        results = List(
            SearchResult(self.hd7_title, 100000000, '100M', 2, 'magnet:?xt=a'),
            SearchResult(self.hd7_title, 100000000, '100M', 5, 'magnet:?xt=b'),
        )
        q = SearchQuery(self._releases[0], '720p')
        r = SearchResults(q, results, self._finder._min_seeders, 0)
        choice = r.choose(q.monitor)
        mag = choice / _.magnet_link
        (
            results
            .index_where(lambda a: mag.contains(a.magnet_link))
            .should.contain(1)
        )

    def recheck(self):
        self._mock_results(lambda: [])
        self._finder._handle(self._releases[0])
        stamp = self._releases[0].last_torrent_search_stamp
        stamp.should.be.greater_than(0)
        self._finder._handle(self._releases[0])
        self._releases[0].last_torrent_search_stamp.should.equal(stamp)

    def max_size(self) -> None:
        results = List(
            SearchResult(self.hd7_title, 1.6e9, '1.6G', 100, 'magnet:?xt=a'),
            SearchResult(self.hd7_title, 1.4e9, '1.4G', 100, 'magnet:?xt=b'),
        )
        q = SearchQuery(self._releases[0], '720p')
        r = SearchResults(q, results, 1, 1.5)
        choice = r.choose(q.monitor)
        mag = choice / _.magnet_link
        (
            results
            .index_where(lambda a: mag.contains(a.magnet_link))
            .should.contain(1)
        )


class TorrentFinderHdSpec(TorrentFinderSpec):

    def _before_monitors(self):
        Config.override('get', full_hd=True)

    def full_hd(self):
        self._releases.update_by_id(1, resolutions=['1080p', '720p'])
        self._mock_results(lambda: [])
        flexmock(self._finder)
        self._finder.should_call('_process_results').times(4)
        self._run_search()

    def with_sd(self):
        self._mock_results(lambda: [])
        flexmock(self._finder)
        self._releases.update_by_id(1, resolutions=('1080p', '720p', ''))
        self._finder.should_call('_process_results').times(6)
        self._run_search()

__all__ = ('TorrentFinderSpec', 'TorrentFinderHdSpec')
