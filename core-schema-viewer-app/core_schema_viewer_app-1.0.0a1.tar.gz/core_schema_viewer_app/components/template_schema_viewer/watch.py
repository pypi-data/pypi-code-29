""" Handle signals.
"""
from core_main_app.commons import exceptions
from core_main_app.components.template.models import Template
from core_schema_viewer_app.components.template_schema_viewer import api as template_schema_viewer_api
from core_schema_viewer_app.components.template_schema_viewer.models import TemplateSchemaViewer
from signals_utils.signals.mongo import connector, signals


def init():
    """ Connect to Template object events.
    """
    connector.connect(post_save_template, signals.post_save, Template)


def post_save_template(sender, document, **kwargs):
    """ Method executed after a saving of a Template object.
    Args:
        sender: Class.
        document: Template document.
        **kwargs: Args.

    """
    try:
        template_schema_viewer_api.get_by_template_id(document.pk)
    except exceptions.DoesNotExist as e:
        # upsert if does not exist for this template
        template_schema_viewer = TemplateSchemaViewer(template=document)
        return template_schema_viewer_api.upsert(template_schema_viewer)
