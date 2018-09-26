import requests
import json

from django.db.models import CharField, ForeignKey, CASCADE, EmailField
from django.db.models import Manager
from django.conf import settings
from django_countries.fields import CountryField
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

from djangokarat.base import Model
from djangokarat.constraints import CheckKaratFields
from djangokarat.utils import has_karat_fields, convert__all__to_fields, get_karat_id_field

from . import Worker


class KaratModel(Model):
    # create delete call
    # delete in multiple tables
    # check thru multiple tables same unique name

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        convert__all__to_fields(self)

    @classmethod
    def check(cls, **kwargs):
        errors = super().check(**kwargs)
        convert__all__to_fields(cls)
        errors.extend(cls._check_karat_meta(**kwargs))
        return errors

    @classmethod
    def _check_karat_meta(cls, **kwargs):
        errors = []
        # if karat params aren't there, don't check errors for them
        if not has_karat_fields(cls):
            return errors

        karat_check = CheckKaratFields(cls)
        errors.extend(karat_check.check_karat_table())
        errors.extend(karat_check.check_karat_fields())
        errors.extend(karat_check.check_uniqueness())
        return errors

    def save(self, *args, **kwargs):
        if has_karat_fields(self):
            return
        prepared_karat_fields = self._prepare_karat_fields()
        prepared_data = self._prepare_data(prepared_karat_fields)
        self._send_data(prepared_data)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if not has_karat_fields(self):
            super().delete(*args, **kwargs)
            return
        unique_field = get_karat_id_field(self)

    def _prepare_karat_fields(self):
        if isinstance(self._meta.karat_fields, dict):
            extracted_dict = model_to_dict(self, fields=self._meta.karat_fields.keys())
            # rename fields to match karat fields
            prepared_karat_fields = {self._meta.karat_fields[k]: v for k, v in extracted_dict.items()}
        else:
            prepared_karat_fields = model_to_dict(self, fields=self._meta.karat_fields)
        return prepared_karat_fields

    def _prepare_data(self, karat_fields_dict):
        karat_fields_dict['_table'] = self._meta.karat_table
        return karat_fields_dict

    def _send_data(self, data):
        if hasattr(settings, 'AGENT_URL'):
            r = requests.post('{}/accept-data'.format(settings.AGENT_URL),
                              json=json.dumps(data, cls=DjangoJSONEncoder))
