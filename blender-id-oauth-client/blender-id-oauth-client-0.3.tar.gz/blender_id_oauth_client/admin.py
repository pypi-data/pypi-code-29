from django.contrib import admin
from . import models


@admin.register(models.OAuthToken)
class OAuthTokenAdmin(admin.ModelAdmin):
    model = models.OAuthToken

    list_display = ('user', 'provider', 'expires_at')
    list_filter = ('provider', 'expires_at')
