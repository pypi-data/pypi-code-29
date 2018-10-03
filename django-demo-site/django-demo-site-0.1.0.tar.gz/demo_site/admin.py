from django.contrib import admin

from .models import DemoSiteSettings, AccessToken


class DemoSiteSettingsAdmin(admin.ModelAdmin):
    """

    """
    def has_add_permission(self, request, obj=None):
       return False

admin.site.register(DemoSiteSettings, DemoSiteSettingsAdmin)


class AccessTokenAdmin(admin.ModelAdmin):
    """

    """
    pass

admin.site.register(AccessToken, AccessTokenAdmin)
