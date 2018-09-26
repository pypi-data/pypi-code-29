from django.contrib import admin

from .models import NLxService


@admin.register(NLxService)
class NLxServiceAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'service', 'address')
    list_filter = ('organisation', 'service')
    search_fields = ('organisation', 'service', 'address')
    ordering = ('organisation', 'service')
