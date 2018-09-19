from csefemerideak.models import Efemeridea
from django.contrib import admin

from tinymce.widgets import TinyMCE


class EfemerideaAdmin(admin.ModelAdmin):
    """ """
    list_display = ('pk', 'text', 'date', 'has_moretext','is_public',)
    list_display_links = ('pk','text')
    ordering = ('-date',)
    search_fields = ['text','moretext',]
    list_filter = ('is_public',)

    fieldsets = (
        ('Efemeridea', {
            'fields': ('date', 'text', 'is_public',)
        }),
        ('Informazio gehigarria', {
            'fields': ('moretext',),
            'classes': ['collapse',]
        }),
    )


class TinyMCEEfemerideaAdmin(EfemerideaAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('moretext', ):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'theme' : "advanced",
                    'mode' : "textareas",
                    'extended_valid_elements' : "iframe[src|width|height|name|align]",
                    'theme_advanced_buttons1' : "formatselect,bold,italic,underline,separator,justifyleft,justifycenter,justifyright, justifyfull,bullist,numlist,undo,redo,link,unlink,image,code,removeformat",
                    'theme_advanced_buttons2' : "",
                    'theme_advanced_buttons3' : "",
                    'theme_advanced_toolbar_location' : "top",
                    'theme_advanced_toolbar_align' : "left",
                    'theme_advanced_resizing' : 'false',
                    },
            ))
        return super(TinyMCEEfemerideaAdmin, self).formfield_for_dbfield(db_field, **kwargs)



 
#admin.site.register(Efemeridea,TinyMCEEfemerideaAdmin)
admin.site.register(Efemeridea,EfemerideaAdmin)
