import json

import httpretty
from flexmock import flexmock  # NOQA

from golgi import Configurations  # NOQA
from amino.test import temp_dir

from tek_utils import sharehoster
from tek_utils.sharehoster.common import LinkCheckingDownloader


class LinkTestMixin:

    def setup(self, *a, **kw):
        super().setup()
        (flexmock(sharehoster.DownloaderFactory)
            .should_receive('__call__')
            .replace_with(LinkCheckingDownloader))
        self._link_check_url = 'http://link_check/moo'
        Configurations.override('sharehoster',
                                link_checker_url=self._link_check_url,
                                out_dir=temp_dir('get', 'link_test', 'dl'))
        self._working = []

    def _mock_content(self):
        for release in self._releases.all:
            for link in release.links:
                httpretty.register_uri(httpretty.GET, link.url, body='success')

    def _mock_link_check(self, all_=False):
        def response(request, uri, headers):
            fname = request.parsed_body['link'][0].rsplit('/', 1)[-1]
            status = 'working' if fname in self._working else 'dead'
            response = dict(result='success', status=status)
            return 200, headers, json.dumps(response)
        if all_:
            body = json.dumps(dict(result='success', status='working'))
        else:
            body = response
        httpretty.register_uri(httpretty.POST, self._link_check_url,
                               body=body, content_type="application/json")

__all__ = ['LinkTestMixin']
