from django.contrib import admin
from django.utils.safestring import mark_safe
from edc_action_item import action_fieldset_tuple, action_fields
from edc_model_admin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import ambition_ae_admin
from ..email_contacts import email_contacts
from ..forms import AeInitialForm
from ..models import AeInitial
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AeInitial, site=ambition_ae_admin)
class AeInitialAdmin(ModelAdminMixin, SimpleHistoryAdmin):

    form = AeInitialForm
    email_contact = email_contacts.get('ae_reports')
    additional_instructions = mark_safe(
        'Complete the initial AE report and forward to the TMG. '
        f'Email to <a href="mailto:{email_contact}">{email_contact}</a>')

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'ae_classification',
                'ae_classification_other',
                'report_datetime',
                'ae_description',
                'ae_awareness_date',
                'ae_start_date',
                'ae_grade',
                'ae_study_relation_possibility',
                # 'ambisome_relation',
                'fluconazole_relation',
                # 'amphotericin_b_relation',
                'flucytosine_relation',
                'amphotericin_relation',
                'details_last_study_drug',
                'med_administered_datetime',
                'ae_cause',
                'ae_cause_other',
                'ae_treatment',
                'ae_cm_recurrence',
                'sae',
                'sae_reason',
                'susar',
                'susar_reported')},
         ),
        action_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'ae_cause': admin.VERTICAL,
        'ae_classification': admin.VERTICAL,
        'ae_cm_recurrence': admin.VERTICAL,
        'ae_grade': admin.VERTICAL,
        'ae_study_relation_possibility': admin.VERTICAL,
        # 'ambisome_relation': admin.VERTICAL,
        # 'amphotericin_b_relation': admin.VERTICAL,
        'amphotericin_relation': admin.VERTICAL,
        'fluconazole_relation': admin.VERTICAL,
        'flucytosine_relation': admin.VERTICAL,
        'sae': admin.VERTICAL,
        'sae_reason': admin.VERTICAL,
        'susar': admin.VERTICAL,
        'susar_reported': admin.VERTICAL,
    }

    ordering = ['-tracking_identifier']

    list_display = ['identifier', 'dashboard',
                    'ae_classification', 'ae_awareness_date',
                    'ae_grade', 'sae', 'sae_reason',
                    'susar', 'susar_reported']

    list_filter = ['ae_awareness_date', 'ae_grade', 'ae_classification',
                   'sae', 'sae_reason', 'susar',
                   'susar_reported']

    search_fields = ['subject_identifier',
                     'action_identifier',
                     'tracking_identifier']

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj=obj)
        return fields + action_fields
