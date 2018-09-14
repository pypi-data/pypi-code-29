from golgi import Config
from amino.test import temp_dir

from unit._support.spec import Spec as SpecBase


class Spec(SpecBase):

    def setup(self, configs=['series.get'], *a, **kw):
        super().setup(*a, configs=configs, **kw)
        download_dir = temp_dir('get', 'download')
        Config.override('get', download_dir=download_dir)

__all__ = ['Spec']
