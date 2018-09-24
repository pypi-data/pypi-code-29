from django.contrib import admin
from .models import Configuration
from .forms import AdminForm

# Register your models here.
class PaasAdmin(admin.ModelAdmin):
    list_display = ('end_point', 'trigger', 'default')
    list_editable = ['default']
    form = AdminForm

admin.site.register(Configuration, PaasAdmin)