# -*- coding:utf-8 -*-

from django.contrib import admin
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
    list_display = ['id', 'basket', 'name', 'desc', 'create_dt', 'update_dt']
    list_filter = ['create_dt', 'update_dt']
    search_fields = ['id', 'name', 'desc',
                     'basket__uri', 'basket__name']
