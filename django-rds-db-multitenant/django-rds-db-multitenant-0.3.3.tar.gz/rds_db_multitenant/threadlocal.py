import logging
from threading import local

LOGGER = logging.getLogger('rds_db_multitenant')

class MultiTenantThreadlocal(local):
    """Thread-local state.  An instance of this should be attached to a
    database connection.

    The first time a request is processed, the tenant name is looked up and
    set in this class.  When a cursor is accquired on that connection,
    the database wrapper will apply the tenant name.
    """

    def __init__(self):
        self.reset()

    def get_tenant_params(self):
        return self.tenant_params

    def set_tenant_params(self, tenant_params):
        self.tenant_params = tenant_params

    def set_cache_prefix(self, prefix):
        self.cache_prefix = prefix

    def get_cache_prefix(self):
        return self.cache_prefix

    def reset(self):
        self.tenant_params = None
        self.cache_prefix = None