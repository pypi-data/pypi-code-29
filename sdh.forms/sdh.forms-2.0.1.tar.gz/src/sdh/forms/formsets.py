from django.forms import formsets


class RequestFormSet(formsets.BaseFormSet):
    def __init__(self, *args, **kwargs):
        self._request = kwargs.pop('request', None)
        self.form_args = kwargs.pop('args', [])

        super(RequestFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        """
        Instantiates and returns the i-th form instance in a formset.
        """
        defaults = {
            'auto_id': self.auto_id,
            'prefix': self.add_prefix(i),
            'error_class': self.error_class,
            }
        if self.is_bound:
            defaults['data'] = self.data
            defaults['files'] = self.files
        if self.initial and 'initial' not in kwargs:
            try:
                defaults['initial'] = self.initial[i]
            except IndexError:
                pass
        # Allow extra forms to be empty.
        if i >= self.initial_form_count():
            defaults['empty_permitted'] = True
        defaults.update(kwargs)
        defaults['request'] = self._request

        form = self.form(*self.form_args, **defaults)
        self.add_fields(form, i)
        return form

    @property
    def empty_form(self):
        form = self.form(
            *self.form_args,
            auto_id=self.auto_id,
            prefix=self.add_prefix('__prefix__'),
            empty_permitted=True,
            request=self._request)
        self.add_fields(form, None)
        return form
