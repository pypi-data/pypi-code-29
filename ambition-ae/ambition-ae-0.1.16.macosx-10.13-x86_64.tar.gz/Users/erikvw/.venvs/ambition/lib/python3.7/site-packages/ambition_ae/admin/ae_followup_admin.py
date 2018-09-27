from django.contrib import admin
from edc_action_item import action_fieldset_tuple
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import AeFollowupForm
from ..models import AeFollowup
from .modeladmin_mixins import ModelAdminMixin, NonAeInitialModelAdminMixin


@admin.register(AeFollowup, site=ambition_ae_admin)
class AeFollowupAdmin(ModelAdminMixin, NonAeInitialModelAdminMixin, admin.ModelAdmin):

    form = AeFollowupForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'ae_initial',
                'report_datetime',
                'outcome_date',
                'outcome',
                'ae_grade',
                'relevant_history',
                'followup')},
         ),
        action_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'outcome': admin.VERTICAL,
        'followup': admin.VERTICAL,
        'ae_grade': admin.VERTICAL,
    }

    list_display = ('identifier', 'dashboard', 'outcome_date', 'initial_ae',
                    'description', 'severity', 'next', 'outcome', 'user_created')

    list_filter = ('ae_grade', 'followup', 'outcome_date', 'report_datetime')

    search_fields = [
        'action_identifier',
        'ae_initial__tracking_identifier',
        'ae_initial__subject_identifier',
        'ae_initial__action_identifier']
