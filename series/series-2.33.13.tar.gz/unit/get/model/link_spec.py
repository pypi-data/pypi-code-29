from flexmock import flexmock

from golgi import Configurations

from tek_utils.sharehoster import DownloaderFactory
from tek_utils.sharehoster.models.link_status import LinkStatus

from series.get.model.link import Link

from unit.get._support.db import DBSpec


class Link_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        Configurations.override('get', sync_link_check=True)
        url = 'http://fake.com/file1a'
        self._link = Link(url=url)
        self._good_status = LinkStatus(dict(result='success', status='working'))
        self._failed_status = LinkStatus(dict(result='failed', status='unknown'))

    def _mock_dl(self, **args):
        fake_downloader = flexmock(close=lambda: True, **args)
        (flexmock(DownloaderFactory)
            .should_receive('__call__')
            .and_return(fake_downloader))

    def valid(self):
        Configurations.override('get', min_size=100)
        self._mock_dl(file_size=10000000, file_path='foo.tar',
                      status=self._good_status)
        self._link.valid.should.be.ok
        self._link.status_str.should.equal(
            'Valid link (http://fake.com/file1a)'
        )

    def valid_by_size(self):
        Configurations.override('get', min_size=100)
        self._mock_dl(file_size=10000000, file_path='foo.tar',
                      status=self._failed_status)
        self._link.valid.should.be.ok
        self._link.status_str.should.equal(
            'Valid link (http://fake.com/file1a)'
        )

    def multipart(self):
        self._mock_dl(file_size=10000000, file_path='foo.part1.rar',
                      status=self._good_status)
        self._link.valid.should_not.be.ok
        self._link.multipart.should.be.ok
        self._link.potential.should_not.be.ok
        self._link.status_str.should.equal(
            'Invalid link: multipart archive (http://fake.com/file1a)'
        )

    def too_small(self):
        Configurations.override('get', min_size=100)
        self._mock_dl(file_size=10, file_path='foo.tar', file_size_str='10 B',
                      status=self._good_status)
        self._link.valid.should_not.be.ok
        self._link.potential.should_not.be.ok
        status = 'Invalid link: too small (10.0 B) (http://fake.com/file1a)'
        self._link.status_str.should.equal(status)

__all__ = ['Link_']
