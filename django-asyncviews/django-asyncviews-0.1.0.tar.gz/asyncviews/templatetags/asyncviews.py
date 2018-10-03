from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import Library
from django.template.loader import render_to_string
from django.utils.http import urlencode
from hashlib import md5
from importlib import import_module
from ..helpers import unique_id

register = Library()


@register.inclusion_tag('async/include.inc.html', takes_context=True)
def async_view(context, viewname, **kwargs):
    app, view = viewname.split('.', 1)
    filters = kwargs.pop('filters', {})

    for key, value in filters.items():
        kwargs['filter__%s' % key] = value

    html_url = '%s?%s' % (
        reverse('async_view_html', args=[app, view]),
        urlencode(kwargs)
    )

    js_url = '%s?%s' % (
        reverse('async_view_js', args=[app, view]),
        urlencode(kwargs)
    )

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
    placeholder = render_to_string(
        klass.get_placeholder_templates(app, view)
    )

    error = render_to_string(
        klass.get_error_templates(app, view)
    )

    return {
        'html': html_url,
        'placeholder': placeholder,
        'error': error,
        'js': js_url,
        'hash': md5(
            str(
                '%s.%s(%s)' % (
                    app,
                    view,
                    unique_id()
                )
            ).encode('utf-8')
        ).hexdigest()
    }
