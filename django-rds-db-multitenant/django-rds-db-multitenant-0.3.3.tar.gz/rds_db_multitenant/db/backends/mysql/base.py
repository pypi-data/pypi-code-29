from importlib import import_module
import logging
import time

from django.core.exceptions import ImproperlyConfigured

from rds_db_multitenant.threadlocal import MultiTenantThreadlocal
from rds_db_multitenant.utils import update_database_from_env

WRAPPED_BACKEND = import_module('django.db.backends.mysql.base')

LOGGER = logging.getLogger('rds_db_multitenant')

class DatabaseWrapper(WRAPPED_BACKEND.DatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.threadlocal = MultiTenantThreadlocal()

    def get_threadlocal(self):
        return self.threadlocal


    def get_new_connection(self, conn_params):
        tenant_params = self.threadlocal.get_tenant_params()
        custom_params = conn_params.copy()
        if type(tenant_params) == dict:
            custom_params.update(tenant_params)
        return super(DatabaseWrapper, self).get_new_connection(custom_params)
