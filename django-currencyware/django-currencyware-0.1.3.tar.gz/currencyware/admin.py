from django.contrib import admin

from .models import Currency, Rate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol', 'number', 'unit', 'country', )
    search_fields = ('code', 'name', 'number',)
    ordering = ['code', 'name']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('code', 'rate', 'date', 'name',)
    search_fields = ('code', 'name',)
    ordering = ['code', 'name',]
