from django.views.generic.base import TemplateView


class AsyncViewBase(TemplateView):
    app = ''
    viewname = ''
    format = ''
    placeholder_template = 'async/placeholder.inc.html'
    error_template = 'async/error.inc.html'
    accepts_kwargs = ()
    http_method_names = ('get', 'post')

    def __init__(self, **kwargs):
        self.app = kwargs['app']
        self.viewname = kwargs['viewname']
        self.format = kwargs['format']

    def get_template_names(self):
        templates = []
        if self.format == 'html':
            templates.append(
                '%s/async/%s.inc.html' % (
                    self.app,
                    self.viewname.replace('_', '/')
                )
            )

            templates.append(
                '%s/async/%s.inc.html' % (
                    self.app,
                    self.viewname.replace(
                        '_', '/',
                        self.viewname.count('_') - 1
                    )
                )
            )

            templates.append('async/base.inc.html')
        elif self.format == 'js':
            templates.append(
                '%s/async/%s.inc.js' % (
                    self.app,
                    self.viewname.replace('_', '/')
                )
            )

            templates.append(
                '%s/async/%s.inc.js' % (
                    self.app,
                    self.viewname.replace(
                        '_', '/',
                        self.viewname.count('_') - 1
                    )
                )
            )

            templates.append('async/base.inc.js')
        else:  # pragma: no cover
            raise Exception(
                'Invalid format: %s' % self.format
            )

        return templates

    def get(self, request):
        response = super().get(request)

        if self.format == 'js':
            import json

            response.render()
            data = json.dumps(
                self.get_js_context(
                    **self.get_accepted_kwargs()
                )
            )

            response.content = '[%s, %s]' % (
                response.content.decode('utf-8'),
                data
            )

            response['Content-Type'] = 'text/javascript'

        return response

    def get_accepted_kwargs(self):
        kwargs = {}
        for key in self.accepts_kwargs:
            if key in self.request.GET:
                kwargs[key] = self.request.GET[key]

        return kwargs

    def get_html_context(self, **kwargs):  # pragma: no cover
        return {}

    def get_js_context(self, **kwargs):  # pragma: no cover
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.format == 'html':
            context.update(
                self.get_html_context(
                    **self.get_accepted_kwargs()
                )
            )

        return context

    @classmethod
    def get_placeholder_templates(cls, app, viewname):
        templates = []
        templates.append(
            '%s/async/%s.loading.html' % (
                app,
                viewname.replace('_', '/')
            )
        )

        templates.append(cls.placeholder_template)
        return templates

    @classmethod
    def get_error_templates(cls, app, viewname):
        templates = []
        templates.append(
            '%s/async/%s.error.html' % (
                app,
                viewname.replace('_', '/')
            )
        )

        templates.append(cls.error_template)
        return templates
