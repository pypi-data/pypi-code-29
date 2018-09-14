import sure  # NOQA
from flexmock import flexmock  # NOQA

from series.etvdb import ETVDBFacade

from amino.test import Spec
from golgi import Config


class ETVDBFacade_(Spec):

    def __init__(self, *a, **kw):
        super().__init__(*a, configs=['series.etvdb'], **kw)
        self._etvdb = ETVDBFacade()

    def season_query(self):
        episodes = self._etvdb.season('the_simpsons', 24)
        episodes.should.have.length_of(22)
        episodes[0]['title'].should.equal('Moonshine River')

    def episode_query(self):
        episode = self._etvdb.episode('the_simpsons', 24, 1)
        episode['title'].should.equal('Moonshine River')

    def translate_name(self):
        alias = 'los simpsonados'
        real = 'the simpsons'
        Config.override('etvdb', series_name_map={alias: real})
        episode = self._etvdb.episode(alias, 24, 1)
        episode['title'].should.equal('Moonshine River')
