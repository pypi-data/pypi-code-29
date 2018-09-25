import arrow
import re

from ambition_ae.action_items import AE_TMG_ACTION
from ambition_auth import TMG
from copy import copy
from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import CLOSED, NEW, OPEN
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView as BaseListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import DeathReportModelWrapper


class DeathListboardView(NavbarViewMixin, EdcBaseViewMixin,
                         ListboardFilterViewMixin, SearchFormViewMixin,
                         BaseListboardView):

    listboard_template = 'tmg_death_listboard_template'
    listboard_url = 'tmg_death_listboard_url'
    listboard_panel_style = 'warning'
    listboard_fa_icon = "fa-chalkboard-teacher"
    listboard_model = 'ambition_prn.deathreport'
    listboard_panel_title = 'TMG Death Reports'
    listboard_view_permission_codename = 'edc_dashboard.view_tmg_listboard'

    model_wrapper_cls = DeathReportModelWrapper
    navbar_name = 'ambition_dashboard'
    navbar_selected_item = 'tmg_death'
    ordering = '-report_datetime'
    paginate_by = 15
    search_form_url = 'tmg_death_listboard_url'

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
