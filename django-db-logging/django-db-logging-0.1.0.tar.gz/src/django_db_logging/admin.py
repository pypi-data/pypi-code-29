# -*- coding: utf-8 -*-
import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from admin_extra_urls.extras import ExtraUrlMixin, link
from admin_extra_urls.mixins import _confirm_action
from django.contrib.admin.views.main import ChangeList
from django.core.paginator import Paginator, InvalidPage
from django.utils.html import format_html

from django_db_logging.handlers import DBHandler
from django_db_logging.settings import config
from .models import Record


class PlainPaginator(Paginator):
    def _get_count(self):
        return config.MAX_LOG_ENTRIES  # we never have more than this
    count = property(_get_count)


class CustomChangeList(ChangeList):
    def get_results(self, request):
        paginator = PlainPaginator(self.queryset, self.list_per_page)
        try:
            result_list = paginator.page(self.page_num + 1).object_list
        except InvalidPage:  # pragma: no cover
            result_list = ()

        self.full_result_count = "~"
        self.result_count = "~"
        self.result_list = result_list
        self.can_show_all = False
        self.multi_page = True
        self.paginator = paginator


@admin.register(Record)
class RecordAdmin(ExtraUrlMixin, ModelAdmin):
    list_display = ('timestamp', 'lvl', 'logger', 'message', 'exception')
    list_filter = ('timestamp', 'level',)
    search_fields = ('logger', )
    date_hierarchy = 'timestamp'
    change_list_template = 'django_db_logging/change_list.html'
    change_form_template = 'django_db_logging/change_form.html'

    def has_add_permission(self, request):
        return False

    def get_changelist(self, request, **kwargs):
        return CustomChangeList

    def lvl(self, instance):
        level = instance.get_level_display()
        return format_html(f'<span class="badge {level}">{level}</span>')
    lvl.short_description = 'Level'

    def exception(self, instance):
        return bool(instance.exc_type)
    exception.short_description = 'Exception'
    exception.boolean = True


    @link(label='Cleanup')
    def cleanup(self, request):
        self.model.objects.cleanup()
        self.message_user(request, "Log cleaned")

    @link(label='Empty Log', css_class="btn btn-danger",
          permission=lambda *a: config.ALLOW_TRUNCATE,
          icon="icon-trash icon-white")
    def empty_log(self, request):
        def _action(request):
            self.model.objects.truncate()

        return _confirm_action(self, request, _action,
                               "Confirm deletion whole error log",
                               "Successfully executed",
                               template='django_db_logging/confirm.html', )

    @link(permission=lambda *a: config.ENABLE_TEST_BUTTON)
    def test(self, request):
        logger = logging.getLogger('django_db_logging_test_logger')
        logger.propagate = False

        handler = DBHandler()
        formatter = logging.Formatter('%(extra_param)s : %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        extra = {'extra_param': 'EXTRA_PARAM'}
        logger.info("DBLogger [INFO] test log entry", extra=extra)
        logger.debug("DBLogger [DEBUG] test log entry", extra=extra)
        logger.error("DBLogger [ERROR] test log entry", extra=extra)
        logger.warning("DBLogger [WARNING] test log entry", extra=extra)
        logger.critical("DBLogger [CRITICAL] test log entry", extra=extra)
        logger.info("DBLogger [INFO] test log entry", extra=extra)

        try:
            raise Exception("DBLogger [EXCEPTION] test log entry")
        except Exception as e:
            logger.exception(e, extra=extra)
