from django.conf import settings
from django.views.generic.base import View
from importlib import import_module


class AsyncView(View):
    http_method_names = ('get', 'post')

    def get_async_view(self):
        app = self.kwargs['app']
        view = self.kwargs['view']
        fmt = self.kwargs['format']

        klassname = '%sView' % (
            view.replace('_', ' ').title().replace(' ', '')
        )

        module = import_module(
            '%s.%s.async' % (
                settings.ASYNCVIEWS_ROOT,
                app
            )
        )

        klass = getattr(module, klassname)
        return klass.as_view(
            app=app,
            viewname=view,
            format=fmt
        )

    def dispatch(self, request, *args, **kwargs):
        view = self.get_async_view()
        return view(request)
