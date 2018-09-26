# -*- coding:utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['uri', 'name', 'desc', 'varnames_', 'create_dt', 'update_dt']
    list_filter = ['create_dt', 'update_dt']
    search_fields = ['uri', 'name', 'desc']

    def varnames_(self, obj):
        return u', '.join(obj.varnames)


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ['id', 'basket', 'name', 'desc', 'preview_', 'create_dt', 'update_dt']
    list_filter = ['create_dt', 'update_dt']
    search_fields = ['id', 'name', 'desc',
                     'basket__uri', 'basket__name']

    def preview_(self, obj):
        if not obj.preview:
            return ''
        else:
            first_line = obj.preview.split('\n', 1)[0]
            return format_html(u'<span title="{}">{}</span>', obj.preview, first_line)
    preview_.allow_tags = True
