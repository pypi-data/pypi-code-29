import re
from datetime import timedelta

import httpretty
import sure  # NOQA
from flexmock import flexmock

from golgi import Configurations, ConfigClient

from tek_utils import sharehoster
from tek_utils.sharehoster.common import Downloader as Retriever

from amino.test.spec_spec import later

from series.get.model.link import Link
from series.get.downloader import Downloader
from unit.get._support.db import DBSpec


class DownloaderSpec(DBSpec):

    def setup(self):
        super().setup()
        (flexmock(sharehoster.DownloaderFactory)
            .should_receive('__call__')
            .replace_with(Retriever))
        (flexmock(Link)
            .should_receive('valid')
            .and_return(True))
        Configurations.override('sharehoster', link_checker_url=None, retry=0)
        self._outfile = ConfigClient('get')('download_dir') / 'file1a'

    @property
    def _release(self):
        return self._releases.all[0]

    @httpretty.activate
    def _download(self):
        httpretty.register_uri(httpretty.GET, re.compile("foo.bum/file\d\w"), body='SUCCESS')
        self._downloader = Downloader(self._releases)
        self._downloader._handle(self._release)
        later(lambda: self._outfile.exists().should.be.ok)
        later(lambda: self._outfile.read_text().should.equal('SUCCESS'))

    def correct(self):
        self._download()
        self._downloader._cleanup()
        self._release.downloaded.should.be.ok

    def wrong_size(self):
        Configurations.override('get', min_size=100)
        self._download()
        self._outfile.write_text('NO')
        self._downloader._cleanup()
        self._release.downloaded.should.be.false
        self._release.failed_downloads.should.equal(1)

    def timeout(self):
        downloader = Downloader(self._releases)
        downloader._timeout = timedelta(seconds=1)
        downloader._handle(self._release)
        self._wait(1)
        downloader._proc % downloader._clean_timeout
        downloader._proc.should.be.empty

__all__ = ('DownloaderSpec',)
