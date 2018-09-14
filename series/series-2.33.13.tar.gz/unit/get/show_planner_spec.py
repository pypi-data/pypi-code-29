import sure  # NOQA

import httpretty

from flexmock import flexmock  # NOQA
from golgi import Config  # NOQA

from series.get.show_planner import ShowPlanner
from series.get.shows_facade import ShowsFacade
from series.get.model.show import Show

from unit.get._support.db import DBTestMixin
from unit.get._support.spec import Spec
from unit.get._support.show_planner import ShowPlannerTestMixin
from unit._support.etvdb import EtvdbTestMixin
from unit.get._support.tvrage import TvrageTestMixin


class ShowPlanner_(ShowPlannerTestMixin, DBTestMixin, Spec,):
    _show_db = None  # type: str

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        Config.override('show_planner', show_db=self._show_db)
        self._shows = ShowsFacade(self._db)
        self._handler = ShowPlanner(self._releases, self._shows)

    def _create_shows(self):
        id1 = '1001'
        self._db.add(Show(rage_id=id1, etvdb_id=id1, name='Series 1',
                          canonical_name='series1'))
        id2 = '1002'
        self._db.add(Show(rage_id=id2, etvdb_id=id2, name='Series 2',
                          canonical_name='series2'))

    def _initialize_shows(self):
        self._mock()
        flexmock(self._handler)
        self._handler.should_call('_add_show').twice()
        self._handler._init()
        query = self._shows.all
        len(query).should.equal(2)
        query[0].canonical_name.should.equal('series1')
        query[0].name.should.equal('Series 1')
        query[0].latest_episode.should.equal(1)

    def _check_next_episode(self):
        self._mock()
        self._create_shows()
        flexmock(self._handler)
        self._handler.should_receive('_add_show').never()
        self._handler._check()
        query = self._shows.all
        query[0].season.should.equal(2)
        query[0].next_episode.should.equal(2)


class TvrageShowPlanner_(ShowPlanner_, TvrageTestMixin, ):
    _show_db = 'tvrage'

    @httpretty.activate
    def initialize_shows(self):
        self._initialize_shows()

    @httpretty.activate
    def check_next_episode(self):
        self._check_next_episode()


class EtvdbShowPlanner_(ShowPlanner_, EtvdbTestMixin, ):
    _show_db = 'etvdb'

    def _epi(self, index):
        data = self._data[index]
        return self.etv_epi(2, 2, data[-1])

    def initialize_shows(self):
        self.responses = iter([
            '1001', 'Series 1', self.any_epi, self._epi(0),
            '1002', 'Series 2', self.any_epi, self._epi(1),
        ])
        self._initialize_shows()

    def check_next_episode(self):
        self.responses = iter([
            'Series 1', self.any_epi, self._epi(0),
            'Series 2', self.any_epi, self._epi(1),
        ])
        self._check_next_episode()

__all__ = ['ShowPlanner_']
