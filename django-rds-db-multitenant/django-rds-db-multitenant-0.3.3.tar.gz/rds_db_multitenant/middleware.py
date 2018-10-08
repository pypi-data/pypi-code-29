from django.conf import settings
from django.db import connection
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # Not required for Django <= 1.9, see:
    # https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
    MiddlewareMixin = object

from rds_db_multitenant import utils


class MultiTenantMiddleware(MiddlewareMixin):
    """Should be placed first in your middlewares.

    This middleware sets up the database and cache prefix from the request."""
    def process_request(self, request):
        mapper = utils.get_mapper()

        threadlocal = connection.get_threadlocal()
        tenant_params = mapper.get_tenant_params(request)
        threadlocal.set_tenant_params(tenant_params)
        # cache_prefix = mapper.get_cache_prefix(request)
        # threadlocal.set_cache_prefix(cache_prefix)

        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            # Clear the sites framework cache.
            from django.contrib.sites.models import Site
            Site.objects.clear_cache()

    def process_response(self, request, response):
        connection.get_threadlocal().reset()
        return response
