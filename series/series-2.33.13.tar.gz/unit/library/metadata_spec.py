import sure  # NOQA
from flexmock import flexmock  # NOQA
from golgi import Configurations  # NOQA

from series.library import LibraryFacade
from series.library.metadata import Metadata
from series.etvdb import ETVDB, ETVDBFacade

from unit._fixtures.library import create_episodes
from unit.library._support.db import DBSpec
from unit._support.etvdb import EtvdbTestMixin


class Metadata_(EtvdbTestMixin, DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        episodes = [
            ['2', 'series2', 3, 1, 0],
            ['2', 'series2', 3, 2, 0],
            ['1', 'series1', 5, 1, 0],
            ['1', 'series1', 5, 2, 0],
            ['1', 'series1', 5, 3, 0],
            ['1', 'series1', 6, 4, 0],
            ['1', 'series1', 6, 5, 0],
            ['1', 'series1', 6, 6, 0],
            ['1', 'series1', 6, 7, 0],
        ]
        epi_dict = dict()
        for id, ser, sea, epi, _ in episodes:
            epi_dict.setdefault(id, {}).setdefault(sea, []).append(epi)
        def etvdb(params):
            sea = int(params[3])
            season = epi_dict[params[1]][sea]
            epi = int(params[5])
            if epi == 0:
                return [self.etv_epi(sea, ep) for ep in season]
            else:
                return [self.etv_epi(sea, epi)]
        args = (a[1:] for a in episodes)
        _, self._episodes = create_episodes(['metadata'], args)
        self._lib = LibraryFacade(self._db)
        self._lib.scan()
        self._lib.episode('series1', 5, 1).new = False
        self._lib.episode('series1', 5, 3).new = False
        self._lib.episode('series2', 3, 2).new = False
        for num in range(4, 8):
            self._lib.episode('series1', 6, num).new = False
        self._meta = Metadata(self._lib, None)
        flexmock(ETVDB).should_receive('__call__').replace_with(etvdb)

    def fetch_metadata(self):
        def fetched():
            return self._lib.episodes(extra=dict(metadata_fetched=True))
        def ibn(name):
            return '1' if name == 'series1' else '2'
        flexmock(ETVDBFacade).should_receive('id_by_name').replace_with(ibn)
        for season in self._lib.seasons():
            self._lib.alter_season(season.series.name, season.number,
                                   dict(metadata_fetched=True))
        self._meta._check()
        epis = fetched()
        epis.should.have.length_of(1)
        epis[-1].series.name.should.equal('series1')
        epis[-1].number.should.equal(2)
        epis[-1].title.should.equal('title 2')
        epis[-1].overview.should.equal('overview 5')
        epis[-1].info['title'].should.equal('title 2')
        epis[-1].info['overview'].should.equal('overview 5')
        self._meta._check()
        epis = fetched()
        epis.should.have.length_of(2)
        epis[-1].series.name.should.equal('series2')
        epis[-1].number.should.equal(1)
        epis[-1].title.should.equal('title 1')
        for season in self._lib.seasons():
            self._lib.alter_season(season.series.name, season.number,
                                   dict(metadata_fetched=False))
        self._meta._check()
        fetched().should.have.length_of(4)
        self._meta._check()
        fetched().should.have.length_of(8)
        self._meta._check()
        fetched().should.have.length_of(9)
        self._meta._check()
        fetched().should.have.length_of(9)

__all__ = ['Metadata_']
