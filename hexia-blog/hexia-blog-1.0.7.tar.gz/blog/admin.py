from django.contrib import admin

from blog.models import *
# Register your models here.

admin.site.register(Blog)

class TagAdmin(admin.ModelAdmin):
    readonly = ['slug']
admin.site.register(Tag, TagAdmin)
