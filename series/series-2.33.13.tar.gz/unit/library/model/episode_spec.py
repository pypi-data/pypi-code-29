import sure  # NOQA
from flexmock import flexmock  # NOQA

from series.library.library_facade import LibraryFacade

from unit.library._support.db import DBSpec
from unit._fixtures.library import create_episodes


class Episode_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        episodes = [
            ['series1', 1, 1, 0],
            ['series1', 1, 2, 0],
            ['series1', 2, 1, 0],
            ['series2', 1, 1, 0],
        ]
        self._collections, self._episodes = create_episodes(['lib1'], episodes)
        self._lib = LibraryFacade(self._db)
        self._lib.scan()

    def ordering(self):
        epi1 = self._lib.episode('series1', 1, 1)
        epi2 = self._lib.episode('series1', 1, 2)
        epi3 = self._lib.episode('series1', 2, 1)
        epi4 = self._lib.episode('series2', 1, 1)
        epi2.should.be.greater_than(epi1)
        epi1.should.be.lower_than(epi2)
        epi1.should_not.be.greater_than(epi2)
        epi2.should.be.lower_than(epi3)
        epi2.should.be.lower_than(epi4)
        epi3.should.be.lower_than(epi4)
        epi3.should_not.be.lower_than(epi2)

__all__ = ['Episode_']
