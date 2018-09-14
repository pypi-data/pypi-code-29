from datetime import date
from concurrent import futures

from amino import _, __

from unit.get._support.db import DBBaseSpec
from unit._fixtures.get.monitors import monitors_4, empty_monitors


class ReleasesFacadeSpec(DBBaseSpec):

    def latest_for_season(self):
        self._db.load_data(monitors_4())
        self._releases.latest_for_season('series3', 1).should.contain(17)

    def find_by_metadata(self):
        self._db.load_data(monitors_4())
        self._releases.find_by_metadata('series3', None, 3)\
            .release.name\
            .should.equal('series3')

    @property
    def _monitors5(self):
        def rel():
            for episode in range(1, 11):
                yield dict(title='series_name_s01e{}'.format(episode),
                           name='series_name', season=1, episode=episode,
                           is_series=True)
        return empty_monitors(list(rel()))

    def filter_by_metadata(self):
        self._db.load_data(self._monitors5)
        self._releases.filter_by_metadata('series_name', None, 3).all()\
            .should.have.length_of(1)
        self._releases.filter_by_metadata('series_name', None, None).all()\
            .should.have.length_of(10)

    def add_links(self):
        ''' parallel update to ensure thread safety '''
        self._db.load_data(self._monitors5)
        with futures.ThreadPoolExecutor() as executor:
            rel = self._releases.all
            ids = rel / _.id
            urls = ids / 'magnet:{}'.format
            list(executor.map(self._releases.add_link_by_id, ids, urls))
        (self._releases.all / __.links.all() / len).forall(_ == 1).should.be.ok

    def set_airdate(self):
        date_long = '2000-04-04'
        date_short = '05-05'
        this_year = date.today().year
        rel_date = lambda: self._releases[0].release.airdate_fmt
        self._db.load_data(self._monitors5)
        self._releases.set_airdate(self._releases.all[0].id, date_long)
        rel_date().should.equal(date_long)
        self._releases.set_airdate(self._releases.all[0].id, date_short)
        rel_date().should.equal('{}-{}'.format(this_year, date_short))

__all__ = ('ReleasesFacadeSpec',)
