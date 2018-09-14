import httpretty

class TvrageTestMixin:

    def setup(self, *a, **kw):
        super().setup(*a, **kw)

    def _mock(self):
        def show(request, uri, headers):
            q = request.querystring
            if 'show' in q:
                key = '100' + list(q['show'])[0][-1]
            else:
                key = list(q['sid'])[0]
            body = self._series_info[key]
            return (200, headers, body)

        def showinfo(request, uri, headers):
            q = request.querystring
            body = self._series_info[list(q['sid'])[0]]
            return (200, headers, body)

        def episodes(request, uri, headers):
            q = request.querystring
            body = self._series_episodes[list(q['sid'])[0]]
            return (200, headers, body)

        httpretty.register_uri(
            httpretty.GET,
            'http://services.tvrage.com/feeds/search.php',
            body=show
        )
        httpretty.register_uri(
            httpretty.GET,
            'http://services.tvrage.com/feeds/showinfo.php',
            body=show
        )
        httpretty.register_uri(
            httpretty.GET,
            'http://services.tvrage.com/feeds/episode_list.php',
            body=episodes
        )

__all__ = ['TvrageTestMixin']
