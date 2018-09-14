from datetime import datetime, timedelta, date
from flexmock import flexmock

import httpretty

from series.get.rest_api import RestApi
from series.get.model.release import Release, ReleaseMonitor
from series.get import ShowsFacade
from series.get.model.show import Show
from unit.get._support.db import DBSpec
from unit._support.rest_api import RestApiTestMixin
from unit.get._support.show_planner import ShowPlannerTestMixin
from unit._support.etvdb import EtvdbTestMixin

from tek.tools import datetime_to_unix

from amino.test.spec_spec import later


class RestApiSpec(ShowPlannerTestMixin, EtvdbTestMixin, RestApiTestMixin, DBSpec):

    def setup(self, *a, **kw):
        super().setup()
        self._shows = ShowsFacade(self._db)
        self._api = RestApi(self._releases, self._shows)
        self._api.app.config['TESTING'] = True
        self._client = self._api.app.test_client()
        self._api.setup_routes()

    def create_a_release(self):
        self._query('/release/series_name/5/3', method='post')
        release = self._releases.all[-1].release
        release.title.should.equal('series_name_05x03')
        release.season.should.equal(5)
        release.episode.should.equal(3)

    def create_existing_release(self):
        response = self._query('/release/series1/4/2', method='post')
        response.should.equal('Release already exists')

    def update_release(self):
        response = self._query('/release/1', method='put',
                               data=dict(downloaded=True))
        response['downloaded'].should.equal(True)
        response = self._query('/release/1', method='put',
                               data=dict(downloaded=False))
        response['downloaded'].should.equal(False)

    @httpretty.activate
    def add_season(self):
        self._mock()
        now = datetime.now()
        d = timedelta(days=5)
        before = now - d
        later = now + d
        self._db.add(Show(
            etvdb_id='1001',
            name='Series 1',
            canonical_name='series1',
        ))
        self.responses = iter([
            [self.etv_epi(2, 1, before), self.etv_epi(2, 2, before),
             self.etv_epi(2, 3, later)]
        ])
        self._query('/show/1/season/2', method='post')
        season = self._db.query(Release).filter_by(name='series1',
                                                   season=2).all()
        season.should.have.length_of(2)
        season[1].name.should.equal('series1')
        season[1].season.should.equal(2)
        season[1].episode.should.equal(2)

    @httpretty.activate
    def add_show(self):
        self._mock()
        self.responses = iter([
            '1001', 'Series 1', self.any_epi, self.any_epi,
        ])
        self._query('/show', method='post', data=dict(name='series1'))
        show = self._db.query(Show)
        show.first().name.should.equal('Series 1')

    @httpretty.activate
    def delete_show_id(self):
        self._mock()
        self._db.add(Show(
            etvdb_id='1001',
            name='Series 1',
            canonical_name='series1',
            latest_season=4,
            latest_episode=3,
            season=-1,
            next_episode=-1,
        ))
        show = self._db.query(Show)
        show.count().should.equal(1)
        self._query('/show', method='delete', data=dict(name='1'))
        show.count().should.equal(0)

    @httpretty.activate
    def delete_show(self):
        self._mock()
        self.responses = iter([
            '1001', 'Series 1', self.any_epi, self.any_epi,
        ])
        can = 'series1'
        add = lambda: self._db.add(Show(
            etvdb_id='1001',
            name='Series 1',
            canonical_name=can,
            latest_season=4,
            latest_episode=3,
            season=-1,
            next_episode=-1,
        ))
        add()
        show = self._db.query(Show)
        show.count().should.equal(1)
        self._query('/show', method='delete', data=dict(name=can))
        later(lambda: show.count() == 0)
        add()
        show.count().should.equal(1)
        self._query('/show', method='delete', data=dict(name=1))
        later(lambda: show.count() == 0)

    @httpretty.activate
    def list_shows(self):
        self._mock()
        name1 = 'Series 1'
        canname1 = name1.lower().replace(' ', '')
        self._db.add(Show(
            etvdb_id='1001',
            name=name1,
            canonical_name='series1',
            latest_season=4,
            latest_episode=3,
            season=-1,
            next_episode=-1,
        ))
        self._db.add(Show(
            etvdb_id='1002',
            name='Series 2',
            canonical_name='series2',
            latest_season=4,
            latest_episode=3,
            season=-1,
            next_episode=-1,
        ))
        response = self._query('/show', method='get',
                               data=dict(regex=canname1[3:]))
        response.should.have.length_of(1)
        response[0][1].should.equal(name1)

    @httpretty.activate
    def next_shows(self):
        self._mock()
        tomorrowDt = datetime.now() + timedelta(days=1)
        tomorrowD = tomorrowDt.date()
        tomorrow = datetime_to_unix(tomorrowDt)
        laterDt = datetime.now() + timedelta(days=3)
        laterD = laterDt.date()
        later = datetime_to_unix(laterDt)
        yesterdayDt = datetime.now() - timedelta(days=1)
        yesterdayD = yesterdayDt.date()
        name1 = 'Series 1'
        self._db.add(Show(
            etvdb_id='1001',
            name=name1,
            canonical_name='series1',
            latest_season=8,
            latest_episode=3,
            season=8,
            next_episode=4,
            next_episode_stamp=tomorrow,
        ))
        self._db.add(Show(
            etvdb_id='1002',
            name='Series 2',
            canonical_name='series2',
            latest_season=2,
            latest_episode=4,
            season=2,
            next_episode=5,
            next_episode_stamp=later,
        ))
        self._db.add(Show(
            etvdb_id='1003',
            name='Series 3',
            canonical_name='series3',
            latest_season=2,
            latest_episode=4,
            season=-1,
            next_episode=-1,
        ))
        self._db.add(Show(
            etvdb_id='1004',
            name='Series 4',
            canonical_name='series4',
            latest_season=7,
            latest_episode=9,
            season=-1,
            next_episode=-1,
        ))
        self._db.add(Show(
            etvdb_id='1005',
            name='Series 5',
            canonical_name='series5',
            latest_season=2,
            latest_episode=3,
            season=2,
            next_episode=4,
            next_episode_stamp=tomorrow,
        ))
        self._db.add(Show(
            etvdb_id='1006',
            name='Series 6',
            canonical_name='series6',
            latest_season=2,
            latest_episode=3,
            season=2,
            next_episode=4,
            next_episode_stamp=tomorrow,
        ))
        (flexmock(ReleaseMonitor).should_receive('torrent_valid')
         .and_return(False, True)
         .one_by_one()
         )
        self._releases.create('series1', 8, 4, tomorrowDt)
        self._releases.create('series4', 7, 9, yesterdayDt)
        self._releases.create('series5', 2, 4, tomorrowDt)
        self._releases.create('series6', 2, 4, tomorrowDt)
        rel = self._releases.all[-4]
        rel2 = self._releases.all[-3]
        rel3 = self._releases.all[-2]
        self._releases.add_torrent(rel, 'magnet://asdfwer')
        self._releases.add_torrent(rel3, 'magnet://asdfwer')
        self._releases.update_by_id(rel2.id, downloaded=True)
        response = self._query('/show/info', method='get')
        s1 = ['Series 1', 'next episode: {}'.format(tomorrowD),
              'release with invalid torrent', 3]
        s2 = ['Series 2', 'next episode: {}'.format(laterD),
              'no release yet', 0]
        s3 = ['Series 3', 'no next episode', 'no release yet', 0]
        s4 = ['Series 4', 'no next episode',
              'release for 7x9 downloaded ({})'.format(yesterdayD), 1]
        s5 = ['Series 5', 'next episode: {}'.format(tomorrowD),
              'release with valid torrent', 2]
        s6 = ['Series 6', 'next episode: {}'.format(tomorrowD),
              'release without torrent', 0]
        desired = [s1, s2, s3, s4, s5, s6]
        response.should.equal(desired)
        response = self._query('/show/next', method='get')
        desired = [s1, s2, s5, s6]
        response.should.equal(desired)
        response = self._query('/show/ready', method='get')
        desired = [s1, s5, s6]
        response.should.equal(desired)
        response = self._query('/show/done', method='get')
        desired = [s4]
        response.should.equal(desired)

    def set_airdate(self):
        go = lambda d: self._query('/release/1/airdate', method='put',
                                   data=dict(date=d))
        date_long = '2044-12-12'
        date_short = '05-05'
        this_year = date.today().year
        rel_date = lambda: self._releases[0].release.airdate_fmt
        go(date_long)
        rel_date().should.equal(date_long)
        go(date_short)
        rel_date().should.equal('{}-{}'.format(this_year, date_short))
        go('invalid').should.have.key('error')

__all__ = ('RestApiSpec',)
