import sure  # NOQA

from flexmock import flexmock  # NOQA

import httpretty

from golgi import Config  # NOQA

from series.get.library_handler import LibraryHandler

from unit.get._support.db import DBSpec


class LibraryHandler_(DBSpec):

    def setup(self, *a, **kw):
        super().setup(*a, **kw)
        Config.override('series', library_url='http://library')
        Config.override('get', library=True)
        self._library_handler = LibraryHandler(self._releases)
        self._releases.all[0].added_to_library = True
        self._releases.all[0].downloaded = True
        self._releases.all[1].downloaded = True
        self._monitor = self._releases[1]

    @httpretty.activate
    def add_to_library(self):
        release = self._monitor.release
        path = '/series/{}/season/{}/episode/{}'
        path = path.format(release.name, release.season, release.episode)
        url = 'http://library' + path
        httpretty.register_uri(httpretty.POST, url)
        self._library_handler._check()
        httpretty.last_request().path.should.equal(path)
        self._monitor.added_to_library.should.be.ok

    @httpretty.activate
    def couldnt_connect(self):
        self._library_handler._check()
        self._monitor.added_to_library.should_not.be.ok

    @httpretty.activate
    def last_error(self):
        self._library_handler._check()
        last = self._library_handler._last_error
        last.should_not.be.none
        self._library_handler._check()
        last.should.equal(self._library_handler._last_error)

__all__ = ['LibraryHandler_']
