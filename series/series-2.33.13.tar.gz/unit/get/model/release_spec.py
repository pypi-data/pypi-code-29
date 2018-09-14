import sure  # NOQA
from flexmock import flexmock

from golgi import Configurations

from tek_utils import sharehoster
from tek_utils.sharehoster.common import Downloader

from series.get.model.link import Link
from unit.get._support.db import DBSpec


class ReleaseMonitor_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        (flexmock(sharehoster.DownloaderFactory)
            .should_receive('__call__')
            .replace_with(Downloader))
        (flexmock(Link)
            .should_receive('valid')
            .and_return(True))
        Configurations.override('sharehoster', link_checker_url=None)

    def finds_a_valid_link(self):
        release = self._releases.all[0]
        release.link.valid.should.be.ok

    def prioritizes_preferred_hosters(self):
        Configurations.override('get', prefer_hosters=['prefer'])
        release = self._releases.all[0]
        release.add_http_link('http://prefer.bam/file')
        release.add_http_link('http://notprefer.blob/file')
        self._db.commit()
        release.link.domain.should.equal('prefer')

__all__ = ['ReleaseMonitor_']
