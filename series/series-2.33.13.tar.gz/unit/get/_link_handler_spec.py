import time

import sure  # NOQA
from flexmock import flexmock  # NOQA
import httpretty
from golgi import Configurations  # NOQA

from series.get.link_handler import LinkHandler

from unit.get._support.spec import Spec
from unit.get._support.db import DBTestMixin
from unit.get._support.link import LinkTestMixin


class LinkHandler_(DBTestMixin, LinkTestMixin, Spec, ):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        self._handler = LinkHandler(self._releases)
        Configurations.override('get', link_check_procs=2)

    def teardown(self, *a, **kw):
        self._handler.terminate()

    def _check(self):
        self._handler._check()
        self._handler.wait()

    @httpretty.activate
    def _critical_links_first(self):
        self._mock_content()
        self._mock_link_check(all_=True)
        r1, r2, r3 = self._releases.all
        self._check()
        r1.links[0].valid.should.be.ok
        r1.links[1].valid.should_not.be.ok
        r3.links[0].valid.should_not.be.ok
        r1.downloadable.should.be.ok
        r2.downloadable.should.be.ok
        r3.downloadable.should_not.be.ok
        self._check()
        r1.links[1].valid.should_not.be.ok
        r3.links[0].valid.should.be.ok
        r3.downloadable.should.be.ok
        self._check()
        r1.links[1].valid.should.be.ok

    def invalid_url(self):
        self._check()
        self._releases.all[0].links[0].valid.should_not.be.ok

    @httpretty.activate
    def _broken_links(self):
        self._mock_content()
        self._mock_link_check()
        self._working.extend([
            'file1b',
            'file2a',
            'file2b',
        ])
        r1, r2, r3 = self._releases.all
        self._check()
        r1.links[0].valid.should_not.be.ok
        r2.links[0].valid.should.be.ok
        r3.links[0].valid.should_not.be.ok
        r1.downloadable.should_not.be.ok
        r2.downloadable.should.be.ok
        r3.downloadable.should_not.be.ok
        self._check()
        r1.downloadable.should.be.ok
        self._check()
        r3.downloadable.should_not.be.ok

    def _recheck(self):
        Configurations.override('get', link_check_retry_coefficient=1./30.)
        r1, r2, r3 = self._releases.all
        link = r1.links[0]
        for i in range(4):
            self._check()
        link.valid.should_not.be.ok
        first = link.last_check
        time.sleep(1)  # timestamp has only second-precision
        self._check()
        link.last_check.should.equal(first)
        time.sleep(1)  # wait for retry period to end
        self._check()
        link.last_check.should_not.equal(first)

__all__ = ['LinkHandler_']
