from flexmock import flexmock  # NOQA

from series.etvdb import ETVDB


class EtvdbTestMixin(object):

    def etv_epi(self, sea, epi, date=''):
        return '{}|{}|000|title {}|000|overview {}|{}'.format(
            sea, epi, epi, sea, date
        )

    @property
    def any_epi(self):
        return self.etv_epi(2, 1, '1900-01-01')

    def _mock(self):
        def etvdb(params, skip=1):
            return next(self.responses)
        flexmock(ETVDB).should_receive('__call__').replace_with(etvdb)

__all__ = ['EtvdbTestMixin']
