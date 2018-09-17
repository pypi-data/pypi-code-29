from __future__ import unicode_literals

from django.forms import Select, SelectMultiple, DateInput


class SelectCallback(Select):
    def __init__(self, attrs=None):
        super(Select, self).__init__(attrs)
        self.choices_callback = None

    def render(self, name, value, attrs=None, renderer=None):
        self.choices = list(self.choices_callback())
        return super(SelectCallback, self).render(name, value, attrs, renderer)


class SelectCallbackMultiple(SelectCallback, SelectMultiple):
    pass


class DatePickerWidget(DateInput):
    def build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(DatePickerWidget, self).build_attrs(extra_attrs, **kwargs)
        attrs['class'] = attrs.get('class', '') + ' date-picker'
        attrs['data-date-autoclose'] = 'true'
        attrs['data-date-format'] = self.format.replace('y', 'yy')\
            .replace('Y', 'yyyy')\
            .replace('M', 'mm')\
            .replace('D', 'dd')\
            .replace('%', '')
        return attrs


class Select2AjaxWidget(Select):

    def __init__(self, attrs=None, choices=(), add_empty=False, data_url=None, **kwargs):
        self.add_empty = add_empty
        self.data_url = data_url
        super(Select2AjaxWidget, self).__init__(attrs=attrs, choices=choices)

    def build_attrs(self, *args, **kwargs):
        """
        Set select2's AJAX attributes.
        """
        attrs = super(Select2AjaxWidget, self).build_attrs(*args, **kwargs)
        if 'class' in attrs:
            attrs['class'] += ' select2'
        else:
            attrs['class'] = 'select2'
        if self.add_empty:
            attrs.setdefault('data-allow-clear', 'true')
        else:
            attrs.setdefault('data-allow-clear', 'false')
        if self.data_url:
            attrs.setdefault('data-ajax--url', self.data_url)
        attrs.setdefault('data-ajax--cache', 'false')
        attrs.setdefault('data-ajax--type', 'GET')
        attrs.setdefault('data-minimum-input-length', 0)
        return attrs


class Select2AjaxMultipleWidget(Select2AjaxWidget, SelectMultiple):
    pass


class LabelWidget(Select):
    template_name = 'sdh/forms/widgets/label_select.html'
