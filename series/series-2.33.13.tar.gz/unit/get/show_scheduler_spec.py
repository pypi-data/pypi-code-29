from datetime import datetime, timedelta

import httpretty

from flexmock import flexmock

from series.get.model.show import Show
from series.get.shows_facade import ShowsFacade
from series.get.show_scheduler import ShowScheduler
from series.util import datetime_to_unix
from series.etvdb import ETVDBFacade

from unit.get._support.db import DBBaseSpec
from unit.get._support.spec import Spec
from unit._support.etvdb import EtvdbTestMixin


class _ShowSchedulerSpec(EtvdbTestMixin, DBBaseSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        self._shows = ShowsFacade(self._db)
        self._scheduler = ShowScheduler(self._releases, self._shows)
        self._create_releases()
        self._create_shows()

    @property
    def _today_d(self):
        return datetime.now().replace(microsecond=0) - timedelta(hours=17)

    @property
    def _later_d(self):
        return datetime.now().replace(microsecond=0) + timedelta(days=3)

    @property
    def _today_s(self):
        return datetime_to_unix(self._today_d)

    @property
    def _later_s(self):
        return datetime_to_unix(self._later_d)

    def _add_show(self, num, ls, le, s, ne, t):
        self._db.add(Show(
            name='Series {}'.format(num),
            canonical_name='series{}'.format(num),
            latest_season=ls,
            latest_episode=le,
            season=s,
            next_episode=ne,
            next_episode_stamp=t,
        ))

    def _mock_airdate(self, airdate):
        return (
            flexmock(ETVDBFacade)
            .should_receive('airdate')
            .and_return(airdate)
        )


class QualifySpec(_ShowSchedulerSpec):

    def _create_releases(self):
        self._releases.create('series1', 4, 2)
        self._releases.create('series2', 2, 7)
        self._releases.create('series3', 1, 5)

    def _create_shows(self):
        self._add_show(1, 4, 3, -1, -1, self._today_s)
        self._add_show(2, 2, 9, 2, 10, self._today_s)
        self._add_show(3, 1, 5, 1, 5, self._today_s)
        self._add_show(4, 1, 9, 1, 10, self._today_s)
        self._add_show(1, 4, 2, -1, -1, self._later_s)
        self._add_show(1, 4, 3, -1, -1, self._later_s)
        self._add_show(5, 2, 1, 2, 2, self._later_s)

    def qualify(self):
        shows = self._shows.all
        # latest db release is older than last episode
        self._scheduler._qualify(shows[0]).should.be.true
        # same, but has next episode
        self._scheduler._qualify(shows[1]).should.be.true
        # latest db release is same as next episode
        self._scheduler._qualify(shows[2]).should.be.false
        # airs self._today_s
        self._scheduler._qualify(shows[3]).should.be.true
        # airs in future, no next episode
        self._scheduler._qualify(shows[4]).should.be.false
        # airs in future, no next episode, db release older than last episode
        self._scheduler._qualify(shows[5]).should.be.true
        # airs in future, has next episode
        self._scheduler._qualify(shows[6]).should.be.false

    def next_episode_not_imminent(self):
        self._mock_airdate(None)
        self._scheduler._handle(self._shows.all[5])
        release = self._releases.all[-1].release
        release.name.should.equal('series1')
        release.season.should.equal(4)
        release.episode.should.equal(3)


class _SimpleSSSpec(_ShowSchedulerSpec):

    @property
    def _show(self):
        return self._shows.all[0]


class SingleSpec(_SimpleSSSpec):

    def _create_releases(self):
        self._releases.create('series2', 2, 9)

    def _create_shows(self):
        self._add_show(2, 2, 9, 2, 10, self._today_s)

    def single_episode(self):
        self._mock_airdate(self._today_d)
        self._scheduler._handle(self._show)
        release = self._releases.all[-1].release
        release.name.should.equal('series2')
        release.season.should.equal(2)
        release.episode.should.equal(10)


class MultiSpec(_SimpleSSSpec):

    def _create_releases(self):
        self._releases.create('series2', 2, 7)

    def _create_shows(self):
        self._add_show(2, 2, 9, 2, 10, self._later_s)

    def multiple_episodes(self):
        self._mock_airdate(None)
        self._scheduler._handle(self._show)
        self._releases.all[-2].release.name.should.equal('series2')
        self._releases.all[-2].release.episode.should.equal(8)
        self._releases.all[-1].release.episode.should.equal(9)


class NoEpisodeSpec(_SimpleSSSpec):

    def _create_releases(self):
        pass

    def _create_shows(self):
        self._add_show(3, 1, 5, 1, 5, None)

    @httpretty.activate
    def no_episode(self):
        self._scheduler._handle(self._show)
        self._releases.all.should.be.empty


class RecheckSpec(EtvdbTestMixin, DBBaseSpec):

    def setup(self):
        super().setup()
        self._shows = ShowsFacade(self._db)
        self._scheduler = ShowScheduler(self._releases, self._shows)
        self._today_s = datetime_to_unix(datetime.now() - timedelta(hours=17))
        self._db.add(Show(
            name='series1',
            canonical_name='series1',
            latest_season=4,
            latest_episode=3,
            season=4,
            next_episode=4,
            next_episode_stamp=self._today_s,
        ))
        self._releases.create('series1', 4, 3)

    @httpretty.activate
    def recheck(self):
        show = lambda: self._shows.all[0]
        self._scheduler._handle(show())
        release = self._releases.all[-1].release
        release.season.should.equal(4)
        release.episode.should.equal(4)
        self._scheduler._qualify(show()).should.be.false


class RescheduleSpec(_SimpleSSSpec):

    def _create_releases(self):
        self._releases.create('series1', 1, 2)

    def _create_shows(self):
        self._add_show(1, 1, 2, 1, 3, self._today_s)

    def reschedule(self):
        self._mock_airdate(self._later_d)
        self._show.next_episode_date.should.equal(self._today_d)
        self._scheduler._check()
        self._show.next_episode_date.should.equal(self._later_d)

__all__ = ('QualifySpec', 'SingleSpec', 'MultiSpec', 'NoEpisodeSpec',
           'RecheckSpec', 'RescheduleSpec')
