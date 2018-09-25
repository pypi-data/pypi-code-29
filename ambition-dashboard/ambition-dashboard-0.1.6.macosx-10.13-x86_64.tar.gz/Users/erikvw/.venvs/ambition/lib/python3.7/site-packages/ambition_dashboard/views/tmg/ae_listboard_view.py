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
from ambition_prn.models.death_report import DeathReport

from ...model_wrappers import DeathReportModelWrapper, ActionItemModelWrapper


class AeListboardView(NavbarViewMixin, EdcBaseViewMixin,
                      ListboardFilterViewMixin, SearchFormViewMixin,
                      BaseListboardView):

    ae_tmg_model = 'ambition_ae.aetmg'

    listboard_template = 'tmg_ae_listboard_template'
    listboard_url = 'tmg_ae_listboard_url'
    listboard_panel_style = 'warning'
    listboard_fa_icon = "fa-chalkboard-teacher"
    listboard_model = 'edc_action_item.actionitem'
    listboard_panel_title = 'TMG AE Reports'
    listboard_view_permission_codename = 'edc_dashboard.view_tmg_listboard'

    model_wrapper_cls = ActionItemModelWrapper
    navbar_name = 'ambition_dashboard'
    navbar_selected_item = 'tmg_ae'
    ordering = '-report_datetime'
    paginate_by = 50
    search_form_url = 'tmg_ae_listboard_url'
    action_type_names = [AE_TMG_ACTION]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AE_TMG_ACTION'] = AE_TMG_ACTION
        context['status'] = NEW if self.request.GET.get('status') not in [
            NEW, OPEN, CLOSED] else self.request.GET.get('status')
        results = copy(context['results'])
        context['results_new'] = [
            r for r in results if r.object.status == NEW]
        context['results_open'] = [
            r for r in results if r.object.status == OPEN]
        context['results_closed'] = [
            r for r in results if r.object.status == CLOSED]
        context['utc_date'] = arrow.now().date()
        return context

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q

    def get_filtered_queryset(self, filter_options=None, exclude_options=None):
        """Returns a queryset after searching against AE TMG.
        """
        filter_options = filter_options or {}
        filter_options.update(action_type__name__in=self.action_type_names)
        if self.search_term and '|' not in self.search_term:
            ae_tmg_model_cls = django_apps.get_model(self.ae_tmg_model)
            search_terms = self.search_term.split('+')
            q = None
            q_objects = []
            for search_term in search_terms:
                q_objects.append(
                    Q(subject_identifier__icontains=slugify(search_term)))
                q_objects.append(
                    Q(action_identifier__icontains=slugify(search_term)))
                q_objects.append(
                    Q(ae_initial__ae_classification__icontains=slugify(search_term)))
                q_objects.append(
                    Q(user_created__iexact=slugify(search_term)))
                q_objects.append(
                    Q(parent_reference_identifier__icontains=slugify(search_term)))
                q_objects.append(
                    Q(related_reference_identifier__icontains=slugify(search_term)))
            for q_object in q_objects:
                if q:
                    q = q | q_object
                else:
                    q = q_object
            tmg_queryset = ae_tmg_model_cls._default_manager.filter(q or Q())
            queryset = self.listboard_model_cls._default_manager.filter(
                action_identifier__in=[
                    obj.action_identifier for obj in tmg_queryset],
                **filter_options).exclude(**exclude_options)
        else:
            queryset = super().get_filtered_queryset(
                filter_options=filter_options,
                exclude_options=exclude_options)

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def update_wrapped_instance(self, model_wrapper):
        model_wrapper.has_reference_obj_permissions = True
        model_wrapper.has_parent_reference_obj_permissions = True
        model_wrapper.has_related_reference_obj_permissions = True
        try:
            self.request.user.groups.get(name=TMG)
        except ObjectDoesNotExist:
            pass
        else:
            if (model_wrapper.reference_obj
                    and model_wrapper.reference_obj._meta.label_lower == self.ae_tmg_model):
                model_wrapper.has_reference_obj_permissions = (
                    model_wrapper.reference_obj.user_created == self.request.user.username)
            if (model_wrapper.parent_reference_obj
                    and model_wrapper.parent_reference_obj._meta.label_lower == self.ae_tmg_model):  # noqa
                model_wrapper.has_parent_reference_obj_permissions = (
                    model_wrapper.parent_reference_obj.user_created == self.request.user.username)  # noqa
            if (model_wrapper.related_reference_obj
                    and model_wrapper.related_reference_obj._meta.label_lower == self.ae_tmg_model):  # noqa
                model_wrapper.has_related_reference_obj_permissions = (
                    model_wrapper.related_reference_obj.user_created == self.request.user.username)  # noqa
        return model_wrapper
