from golgi import Config
from golgi.test.spec import SpecConfigConcern

from amino.test.spec_spec import IntegrationSpec
from amino.test import temp_dir


class Spec(SpecConfigConcern, IntegrationSpec):

    def setup(self, configs=['series.get', 'series.library'], **kw):
        SpecConfigConcern.setup(self, configs=configs, **kw)
        IntegrationSpec.setup(self)
        download_dir = temp_dir('get', 'download')
        Config.override('get', download_dir=download_dir)

__all__ = ('Spec',)
