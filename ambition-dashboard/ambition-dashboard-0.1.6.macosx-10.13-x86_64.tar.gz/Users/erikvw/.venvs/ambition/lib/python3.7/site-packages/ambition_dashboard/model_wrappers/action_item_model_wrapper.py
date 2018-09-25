from ambition_prn.action_items import DEATH_REPORT_TMG_ACTION
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item.model_wrappers import ActionItemModelWrapper as BaseActionItemModelWrapper
from edc_action_item.models import ActionItem

from .death_report_model_wrapper import DeathReportModelWrapper
from .death_report_tmg_model_wrapper import DeathReportTmgModelWrapper


class ActionItemModelWrapper(BaseActionItemModelWrapper):
    next_url_name = settings.DASHBOARD_URL_NAMES.get('tmg_ae_listboard_url')

    death_report_model = 'ambition_prn.deathreport'
    death_report_tmg_model = 'ambition_prn.deathreporttmg'

    @property
    def death_report_tmg_verbose_name(self):
        return django_apps.get_model(self.death_report_tmg_model)._meta.verbose_name

    @property
    def death_report_obj(self):
        model_cls = django_apps.get_model(self.death_report_model)
        try:
            obj = model_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except ObjectDoesNotExist:
            obj = None
        else:
            obj = DeathReportModelWrapper(model_obj=obj)
        return obj

    @property
    def death_report_tmg_obj(self):
        death_report_tmg_obj = None
        if self.death_report_obj:
            model_cls = django_apps.get_model(self.death_report_tmg_model)
            death_report_tmg_obj = DeathReportTmgModelWrapper(
                model_obj=model_cls.objects.get(
                    subject_identifier=self.subject_identifier))
            if not death_report_tmg_obj:
                action_item = ActionItem.objects.get(
                    parent_reference_identifier=self.death_report_obj.object.action_identifier,
                    action_type__name=DEATH_REPORT_TMG_ACTION)
                death_report_tmg_obj = DeathReportTmgModelWrapper(
                    model_obj=model_cls(
                        death_report=self.death_report_obj.object,
                        subject_identifier=self.death_report_obj.object.subject_identifier,
                        action_identifier=action_item.action_identifier,
                        parent_reference_identifier=action_item.parent_reference_identifier,
                        related_reference_identifier=action_item.related_reference_identifier))
        return death_report_tmg_obj
