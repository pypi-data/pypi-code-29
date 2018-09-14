from flexmock import flexmock

from unit.get._support.db import DBTestMixinBase
from unit.get._support.spec import Spec

from series.get.model.link import Link
from series.get.downloader import ValidLinks, ValidLink
from series.get.handler import R


class ConditionSpec(DBTestMixinBase, Spec):

    def valid_link(self):
        (flexmock(Link)
            .should_receive('valid')
            .and_return(True))
        r = self._releases.create('series', '1', '1')
        self._releases.add_link(r, 'http://host/file')
        l = r.links.first()
        attrs = R('downloaded') | R('nuked') | R('downloading')
        link = ValidLink(l)
        links = ValidLinks()
        attrs.ev(r).should_not.be.ok
        link.ev(r).should.be.ok
        links.ev(r).should.be.ok
        cond = ~attrs & links
        cond.ev(r).should.be.ok

__all__ = ('ConditionSpec',)
