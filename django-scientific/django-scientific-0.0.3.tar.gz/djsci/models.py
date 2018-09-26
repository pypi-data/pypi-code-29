# -*- coding:utf-8 -*-

import six
from django.db import models
from knob.dt import local_now
from .fields import DataField


@six.python_2_unicode_compatible
class Basket(models.Model):
    class Meta:
        pass

    uri = models.CharField(max_length=128, primary_key=True, unique=True)
    name = models.CharField(max_length=128, default='', null=True, blank=True)
    desc = models.TextField(default='', null=True, blank=True)

    create_dt = models.DateTimeField(default=local_now)
    update_dt = models.DateTimeField(default=local_now)

    def __str__(self):
        return u'[{}] {}'.format(self.uri, self.name)

    @property
    def varnames(self):
        return self.variables.values_list('name', flat=True)

    def get(self, varname, default=None):
        try:
            var = self.variables.get(name=varname)
            return var.data
        except Variable.DoesNotExist:
            return default

    def set(self, varname, data=None):
        if isinstance(varname, dict):
            vars = varname
        else:
            vars = {varname: data}

        now = local_now()
        for vn, d in six.iteritems(vars):
            var, created = self.variables.update_or_create(basket=self, name=vn, defaults={"data": d, "update_dt": now})

        self.update_dt = now
        self.save(update_fields=['update_dt'])


@six.python_2_unicode_compatible
class Variable(models.Model):
    class Meta:
        unique_together = [('basket', 'name')]

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='variables')
    name = models.CharField(max_length=32)
    desc = models.TextField(default='', null=True, blank=True)
    data = DataField(null=True, blank=True, compress=True)
    preview = models.TextField(default='', null=True, blank=True)
    # storage_size = models.PositiveIntegerField(default=0)

    create_dt = models.DateTimeField(default=local_now)
    update_dt = models.DateTimeField(default=local_now)

    def __str__(self):
        return u"[{}] {}".format(self.basket.uri, self.name)

    def set_data(self, data):
        self.data = data
        self.update_dt = local_now()
        self.save(update_fields=['data', 'update_dt'])

    def save(self, **kwargs):
        update_fields = kwargs.get('update_fields')
        if isinstance(update_fields, (list, tuple)):
            update_fields = set(update_fields)
            update_fields.update(['preview'])
            kwargs['update_fields'] = list(update_fields)

        self.preview = repr(self.data)
        super(Variable, self).save(**kwargs)
