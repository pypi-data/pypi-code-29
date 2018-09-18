from jennifer.wrap.wsgi import wrap_wsgi_app
from jennifer.agent import jennifer_agent
from jennifer.api.format import format_function

__hooking_module__ = 'django'


def hook(django):
    from django.core.handlers.wsgi import WSGIHandler
    def wrapper(origin):
        def handler(self, environ, start_response):
            origin_path_info = environ.get('PATH_INFO')
            request = self.request_class(environ)
            resolver = None
            if hasattr(django, 'urls') and hasattr(django.urls, 'get_resolver'):
                get_resolver = django.urls.get_resolver
                if hasattr(request, 'urlconf'):
                    urlconf = request.urlconf
                    resolver = get_resolver(urlconf)
                else:
                    resolver = get_resolver()
            elif hasattr(django.core, 'urlresolvers'):
                urlresolvers = django.core.urlresolvers
                settings = django.conf.settings
                urlconf = settings.ROOT_URLCONF
                urlresolvers.set_urlconf(urlconf)
                resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)
                if hasattr(request, 'urlconf'):
                    urlconf = request.urlconf
                    urlresolvers.set_urlconf(urlconf)
                    resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)

            if resolver is not None:
                try:
                    resolver_match = resolver.resolve(request.path_info)
                    name = format_function(resolver_match.func)
                    profiler = jennifer_agent().current_transaction().profiler
                    profiler.set_root_name(name)
                except:
                    pass
            if origin_path_info is not None:
                environ['PATH_INFO'] = origin_path_info
            return origin(self, environ, start_response)
        return handler
    WSGIHandler.__call__ = wrapper(WSGIHandler.__call__)
    WSGIHandler.__call__ = wrap_wsgi_app(
        WSGIHandler.__call__,
        'django.core.handlers.wsgi.WSGIHandler.__call__')
