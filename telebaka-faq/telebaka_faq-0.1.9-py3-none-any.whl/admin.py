from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from telebaka_faq.models import FAQSection


@admin.register(FAQSection)
class FAQSectionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = 'command', 'title', 'bot', 'hidden',
    list_filter = 'bot',
