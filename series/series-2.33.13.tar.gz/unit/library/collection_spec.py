import sure  # NOQA
from flexmock import flexmock  # NOQA
from golgi import Configurations  # NOQA

from series.library.model.collection import EpisodeCollection
from unit.library._support.spec import Spec


class EpisodeCollection_(Spec, ):

    def formatter(self):
        Configurations.override('library', name_formatter='echo {}')
        c = EpisodeCollection('')
        c._format_name('foo_bar').should.equal('foo_bar')

__all__ = ['EpisodeCollection_']
