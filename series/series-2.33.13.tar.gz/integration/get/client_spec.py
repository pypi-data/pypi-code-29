from datetime import datetime, timedelta

from flexmock import flexmock

from tek.user_input import input_queue, input_queue

from tek_utils.sharehoster.torrent import TorrentDownloader

from golgi import Config
from amino import List, _, Just, Left
from amino.lazy import lazy

from series.get.client.rest_api import GetClient, purge_msg
from series.get import SeriesGetD, ReleaseMonitor
from series.get.model.show import Show
from series.get.torrent_handler import TorrentHandler
from series.etvdb import ETVDBFacade, Show as EShow
from series.get.model.release import ReleaseFactory, Release
from series.util import datetime_to_unix
from series.get.cli import SeriesGetC

from unit.get._support.db import DBTestMixinBase, DBTestMixin
from unit._fixtures.get.monitors import monitors
from integration._support.rest_api import ApiClientSpec


class _ApiSpec(ApiClientSpec):

    def setup(self, extra=[]):
        self._extra_services = extra
        ApiClientSpec.setup(self)
        Config.override('get', run=['rest_api'] + self._extra_services)

    @lazy
    def _getd(self) -> SeriesGetD:
        return SeriesGetD(self._db)

    @property
    def _create_api(self):
        self._shows = self._getd.shows
        return self._getd.rest_api


class HttpCliSpec(_ApiSpec, DBTestMixinBase):

    def setup(self, **kw) -> None:
        self._setup_db()
        _ApiSpec.setup(self, **kw)
        self.api

    def query_client(self):
        self._releases.create('show1', 1, 4)
        search_regex = 's.*4'
        Config.override('client', cli_cmd=['list'], cli_params=[search_regex])
        cli = SeriesGetC()
        response = cli.run()
        response.should.be.true

    def error(self):
        Config.override('client', cli_cmd=['show_release'], cli_params=[99])
        cli = SeriesGetC()
        response = cli.run()
        response.should.be.false


class _ApiClientBase(_ApiSpec):

    def setup(self, **kw):
        Config.override('client', query_etvdb=False)
        self._client = GetClient()
        _ApiSpec.setup(self, **kw)


class _DefaultMonitors(_ApiClientBase, DBTestMixin):

    def setup(self, **kw) -> None:
        _ApiClientBase.setup(self, **kw)
        DBTestMixin.setup(self)
        self.api


class _NoMonitors(_ApiClientBase, DBTestMixinBase):

    def setup(self, **kw) -> None:
        _ApiClientBase.setup(self, **kw)
        DBTestMixinBase.setup(self)
        self.api


class ApiClient_(_NoMonitors):

    def list(self):
        n1 = 'name1'
        n2 = 'name2'
        self._releases.create(n1, 3, 3)
        self._releases.create(n2, 3, 3)
        self._releases.create('other3', 3, 3)
        result = List.wrap(self._client._list('n.*[12]'))
        def fmt(m):
            r = m['release']
            return [m['id'], r['series'], r['season'], r['episode']]
        check = result / fmt
        expected = List([1, n1, 3, 3], [2, n2, 3, 3])
        check.should.equal(expected)

    def add_link_metadata(self):
        url = 'http://host.com/file'
        series = 'name1'
        season = '4'
        episode = '2'
        self._releases.create('other', 1, 1)
        self._releases.create(series, season, episode)
        result = self._client.add_link(series, season, episode, url)
        result.should.be.right

    def add_link_id(self):
        self._releases.create('dummy', 1, 1)
        url = 'magnet:?xt=urn:btih:2342342534653'
        _id = 12345
        result = self._client.add_link(_id, url)
        result.should.be.left
        _id = 1
        result = self._client.add_link(_id, url)
        result.should.be.right
        torrent = self._releases[0].torrent / _.link
        torrent.should.just_contain(url)

    def _mock_show(self, eshow, airdate=None):
        tv = flexmock(ETVDBFacade)
        if airdate:
            tv.should_receive('airdate').and_return(airdate)
        tv.should_receive('show').and_return(eshow)
        tv.should_receive('shows').and_return(Just((List(eshow), List(111))))

    def _mock_season(self, eshow, season, epis):
        tv = flexmock(ETVDBFacade)
        tv.should_receive('season').with_args(str(eshow.showid),
                                              season).and_return(epis)

    def create_a_release(self):
        name = 'series_name'
        airdate = datetime(2016, 5, 5, 0, 0, 0)
        eshow = EShow(1, name, None, None)
        self._shows.add(name, eshow)
        self._mock_show(eshow, airdate)
        self._client.create_release(name, 5, 3)
        release = self._releases.all[-1].release
        release.title.should.equal('series_name_05x03')
        release.season.should.equal(5)
        release.episode.should.equal(3)
        release.airdate.should.equal(airdate)

    def delete_release(self):
        name = 'showname'
        season = 4
        episode = 5
        id = self._releases.create(name, season, episode).id
        response = self._client.delete_release(name, season, episode)
        response.should.be.right
        self._releases.find_by_id(id).should.be.none
        self._releases.find_release_by_metadata(name, season,
                                                episode).should.be.none

    def create_existing_release(self):
        n, s, e = 'name1', 34, 78
        self._releases.create(n, s, e)
        result = self._client.create_release(n, s, e)
        result.should.contain('Release already exists')

    def add_season(self):
        name = 'showshow'
        show = EShow(1, name, None, None)
        self._mock_show(show)
        old = (datetime.now() - timedelta(days=4)).strftime('%F')
        later = (datetime.now() + timedelta(days=4)).strftime('%F')
        e1 = dict(episode=1, season=3, date=old)
        e2 = dict(episode=2, season=3, date=old)
        e3 = dict(episode=3, season=3, date=later)
        e4 = dict(episode=1, season=4, date=old)
        self._mock_season(show, 3, [e1, e2, e3])
        self._mock_season(show, 4, [e4])
        self._client.add_show(name)
        self._client.add_season(1, 3)
        self._releases.all.should.have.length_of(2)
        self._client.add_season(name, 4).should.be.right
        self._releases.all.should.have.length_of(3)
        self._client.add_season(2, 3).should.be.left

    def delete_show(self):
        name = 'showshow'
        show = EShow(1, name, None, None)
        self._mock_show(show)
        self._client.add_show(name)
        self._shows.all.should.have.length_of(1)
        self._client.delete_show(1)
        self._shows.all.should.have.length_of(0)

    def list_shows(self):
        name = 'showshow'
        show = EShow(1, name, None, None)
        self._mock_show(show)
        self._client.add_show(name)
        self.log.info(self._client.list_shows())

    def help(self):
        self._client.help()

    def show_a_release(self):
        n = 'series_name'
        s = 5
        e = 3
        self._client.create_release(n, s, e)
        self._client.add_link(n, s, e, 'magnet:series_name_s05e3.720p')
        self._client.show_release(n, s, e).value % self.log.info

    def show_a_show(self):
        name = 'showshow'
        self._mock_show(EShow(1, name, None, None))
        self._client.add_show(name)
        self._client.show_show(name).value % self.log.info

    def update_a_release(self):
        r = '540p,'
        self._client.create_release('series_name', 5, 3)
        self._client.update_release('series_name', '5', '3',
                                    'resolutions={}'.format(r))
        self._releases[-1].resolutions.should.equal(List.wrap(r.split(',')))

    def update_a_show(self):
        n = 15
        name = 'update'
        self._mock_show(EShow(1, name, None, None))
        self._client.add_show(name, 1)
        self._client.update_show('1', 'downgrade_after={}'.format(n))
        self._shows.all[-1].downgrade_after.should.equal(n)

    def update_a_release_by_id(self):
        r = '540p,'
        self._client.create_release('series_name', 5, 3)
        self._client.update_release(str(self._releases.count),
                                    'resolutions={}'.format(r))
        self._releases[-1].resolutions.should.equal(List.wrap(r.split(',')))

    def activate_a_release(self):
        self._client.create_release('series_name', 5, 3)
        self._client.activate_release(str(self._releases.count))

    def activate_a_show(self):
        name = 'showshow'
        self._mock_show(EShow(1, name, None, None))
        self._client.add_show(name)
        self._client.activate_show(str(self._shows.count))

    def set_airdate(self):
        self._releases.create('dummy', 1, 1)
        self._client.set_airdate(1, '2018-02-02').should.be.right
        self._client.set_airdate(1).should.be.left

    def purge(self):
        old = datetime_to_unix(datetime.now() - timedelta(days=10))
        new = datetime_to_unix(datetime.now() - timedelta(days=4))
        self._releases.create('name1', 1, 1, download_date_stamp=old,
                              downloaded=True)
        self._releases.create('name1', 1, 2, download_date_stamp=old,
                              downloaded=True)
        self._releases.add_torrent_by_id(2, 'magnet:killme')
        self._releases.create('name1', 1, 3, download_date_stamp=new,
                              downloaded=True)
        self._releases.create('name2', 1, 1, download_date_stamp=old,
                              downloaded=True)
        self._releases.create('name2', 1, 2, download_date_stamp=new,
                              downloaded=True)
        self._releases.create('name2', 1, 3, download_date_stamp=old,
                              downloaded=False)
        self._releases.create('name2', 1, 4, download_date_stamp=None,
                              downloaded=True)
        result = self._client.purge(5) | dict()
        target = purge_msg.format(4, 1, 4)
        result.should.equal(target)
        self._releases.all.should.have.length_of(3)
        self._releases.query_release().all().should.have.length_of(3)

    def reset_torrent(self):
        self._releases.create('show', 1, 2)
        link = 'magnet:xyz'
        self._releases.add_torrent_by_id(1, link)
        self._client.reset_torrent(1)
        self._releases[0].torrent_links[0].dead.should.be.true

    def search_success(self) -> None:
        link = 'magnet:xyz'
        Config.override('torrent', search_engine='piratebay')
        flexmock(TorrentDownloader).should_receive('_search_tpb').and_return(True)
        flexmock(TorrentDownloader).should_receive('search_results').and_return(List(link))
        self._releases.create('series_name', 3, 5, airdate=datetime.now())
        self._client.search('1')
        (self._releases.by_id(1) // _.torrent / _.link).should.just_contain(link)

    def search_fail(self) -> None:
        Config.override('torrent', search_engine='piratebay')
        flexmock(TorrentDownloader).should_receive('_search_tpb').and_return(False)
        self._releases.create('series_name', 3, 5, airdate=datetime.now())
        self._client.search('series_name', 3, 5).lmap(_.cause).lmap(str).should.equal(Left('no search results'))


class ExplainSpec(_DefaultMonitors):

    def setup(self):
        extra = ['torrent_handler', 'torrent_finder', 'downloader', 'archiver', 'show_scheduler']
        super().setup(extra=extra)

    @property
    def _monitors(self):
        epi = dict(title='series1_s01e05', name='series1',
                   season=1, episode=5, is_series=True,
                   resolution='1080p')
        release_data = [epi]
        links = [
            ['magnet:?xt=urn:btih:beef&dn=Series1.S01E05.1080p'],
        ]
        return list(monitors(release_data, [[]], torrents=links))

    def releases(self):
        self.log.info(self._client.explain(1))


class ExplainShowSpec(_NoMonitors):

    def setup(self):
        extra = ['show_planner', 'show_scheduler']
        super().setup(extra=extra)
        self._db.add(Show(rage_id=1, etvdb_id=1, name='Series 1', canonical_name='series1'))

    def fresh(self):
        self.log.info(self._client.explain_show(1))

    def continuing(self):
        self._shows.update(1, dict(latest_season=1, latest_episode=6))
        self._releases.create('series1', 1, 1)
        self.log.info(self._client.explain_show(1))


class ActivateSpec(_NoMonitors):

    def setup(self):
        extra = ['torrent_handler']
        super().setup(extra=extra)

    def activate_release(self):
        self._releases.create('series1', 1, 5)
        self._releases.add_torrent_by_id(1, 'magnet:desc')
        th = self._getd.torrent_handler
        flexmock(TorrentHandler).should_receive('_check_error').and_return(0)
        th._check()
        th._last_check.should.have.key('1')
        self._client.activate_release('1')
        th._last_check.should_not.have.key('1')


class StatusSpec(_DefaultMonitors):

    def setup(self):
        extra = ['torrent_finder']
        _DefaultMonitors.setup(self, extra=extra)

    @property
    def _monitors(self):
        fact = ReleaseFactory()
        def epi(s, e):
            return Release(title='series1_s{}e{}', name='series1',
                           season=s, episode=e, is_series=True,
                           resolution='1080p')
        link = ['magnet:first', 'magnet:second']
        rel = lambda s, e, **k: fact.monitor(epi(s, e), [], link, **k)
        d1 = datetime_to_unix(datetime.now() - timedelta(days=10))
        d2 = datetime_to_unix(datetime.now() - timedelta(days=1))
        return List(
            rel(1, 1, download_date_stamp=d1, downloaded=True),
            rel(1, 2, download_date_stamp=d2, downloaded=True),
            rel(1, 3),
            rel(1, 4),
            rel(1, 5),
            rel(1, 7, downloading=True),
            rel(1, 8, failed_downloads=3),
        )

    def _setup_releases(self):
        (
            flexmock(ReleaseMonitor)
            .should_receive('caching_f')
            .and_return(True, False)
            .one_by_one()
        )
        ne = datetime_to_unix(datetime.now() + timedelta(days=2))
        ne2 = datetime_to_unix(datetime.now() + timedelta(days=21))
        ne3 = datetime_to_unix(datetime.now() + timedelta(days=3))
        self._db.add(Show(rage_id=1, etvdb_id=1, name='Series Name 1',
                          canonical_name='series_name_1', next_episode=6,
                          next_episode_stamp=ne, season=1, latest_season=1,
                          latest_episode=4))
        self._db.add(Show(rage_id=2, etvdb_id=2, name='Series 2',
                          canonical_name='series2', next_episode=6,
                          next_episode_stamp=ne2, season=1))
        self._db.add(Show(rage_id=3, etvdb_id=1, name='Series Name 2',
                          canonical_name='series_name_2', next_episode=8,
                          next_episode_stamp=ne3, season=1, latest_season=1,
                          latest_episode=4))
        self._releases.all[2].torrents[0].cached = True
        self._db.commit()
        r = self._releases[4]
        self._getd.torrent_finder._async = (
            self._getd.torrent_finder._create_async(r))

    def data(self):
        self._setup_releases()
        s = self._client._status
        (s['done'] / _['episode']).should.equal(List(1, 2))
        (s['caching'] / _['episode']).should.equal(List(4))
        (s['search'] / _['episode']).should.equal(List(5))
        (s['next'] / _['episode']).should.equal(List(6))
        (s['downloading'] / _['episode']).should.equal(List(7))
        (s['failed'] / _['episode']).should.equal(List(8))
        (s['current_search'] / _['episode']).should.equal(List(5))

    def output(self):
        self._setup_releases()
        r = self._client.status()
        r.should.be.right
        r.value % self.log.info


class AddShowSpec(ApiClient_):

    def setup(self):
        super().setup()
        Config.override('client', query_etvdb=True)
        self._tv = flexmock(ETVDBFacade)

    def _run(self, name, shows, good=True):
        i = shows.index_of(name) | -1
        query = 'show_name'
        ids = List.range(shows.length)
        (
            self._tv
            .should_receive('shows')
            .with_args(query)
            .and_return(Just((shows, ids)))
        )
        if good:
            (
                self._tv.should_receive('show')
                .with_args(query, i)
                .and_return(EShow(i + 1, name, None, None))
            )
        self._client.add_show(query)
        if good:
            s = self._shows.all[-1]
            s.canonical_name.should.equal(query)
            s.name.should.equal(name)

    def multi(self):
        input_queue.push('2')
        en = 'Show Name 2'
        shows = List('Show Name 1', en, 'The Show Name Show')
        self._run(en, shows)

    def unique(self):
        en = 'Show Name'
        self._run(en, List(en))

    def none(self):
        self._run('', List(), False)
        self._shows.all.should.be.empty

__all__ = ('ActivateSpec', 'ExplainShowSpec', 'ExplainSpec', 'ApiClient_', 'HttpCliSpec')
