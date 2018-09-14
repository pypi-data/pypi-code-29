from datetime import datetime, timedelta

from flexmock import flexmock

import httpretty

from unit.get._support.link import LinkTestMixin

from tek_utils.sharehoster.torrent import SearchResult

from amino import List
from amino.test.spec_spec import later

from series.util import datetime_to_unix
from series.get.search import TorrentSearch
from series.get.test.torrent import caching, downloadable

from integration.get.reset_torrent_spec import ResetTorrentSpecBase


class DowngradeSpec(LinkTestMixin, ResetTorrentSpecBase):

    @httpretty.activate
    def downgrade(self):
        results = List(
            SearchResult('the.showname.s01e05.720p.mkv', 100000000, '100M', 500, self._torrent1),
            SearchResult('the.showname.s01e05.mkv', 100000000, '100M', 500, self._torrent2),
        )
        last = datetime_to_unix(datetime.now() - timedelta(days=3))
        get = self._init(['torrent_finder'])
        downloadable[self._torrent1] = False
        get.torrent_finder._initial_wait = 0
        get.torrent_cleaner._initial_wait = 0.5
        (
            flexmock(TorrentSearch)
            .should_receive('_search_kickass')
            .and_return(results)
        )
        get.torrent_handler._cooldown = 0
        get.start()
        self._releases.update_by_id(self.release.id,
                                    last_torrent_update_stamp=last,
                                    downgrade_after=48)
        later(lambda: self.release.torrent_links[0].dead.should.be.ok)
        caching[self._torrent2] = True
        later(lambda: self.release.torrent_links.should.have.length_of(2),
              timeout=10)
        later(lambda: self.release.torrent_links[1].valid.should.be.ok,
              timeout=10)
        self._wait_dld()
        get.interrupt()
        self._out_content('second')


__all__ = ('DowngradeSpec',)
