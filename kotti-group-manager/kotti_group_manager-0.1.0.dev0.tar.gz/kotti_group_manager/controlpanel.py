import colander

import deform
from kotti.views.form import ObjectType, CommaSeparatedListWidget
from kotti.fanstatic import tagit
from kotti_controlpanel.util import add_settings
from kotti_controlpanel.util import get_setting
from kotti_group_manager import _


@colander.deferred
def deferred_tag_it_widget(node, kw):
    tagit.need()
    all_tags = get_setting('domains', default=[])
    if not all_tags:
        all_tags = []
    available_tags = [tag.encode('utf-8') for tag in all_tags]
    widget = CommaSeparatedListWidget(template='tag_it',
                                      available_tags=available_tags)
    return widget


class GroupRulesSchema(colander.MappingSchema):
    
    email_domain_as_group = colander.SchemaNode(
        colander.Boolean(),
        description=_(u'Check the box above to enable this feature'),
        widget=deform.widget.CheckboxWidget(),
        title='Allow groups to be created from email domain',
        default=False
    )
    
    domains = colander.SchemaNode(
        ObjectType(),
        title=_('Black listed Domains'),
        widget=deferred_tag_it_widget,
        missing=[],
    )
    
    group_as_content = colander.SchemaNode(
        colander.Boolean(),
        description='Check the box above to enable this feature',
        widget=deform.widget.CheckboxWidget(),
        title='Create a page for each group created',
        default=False
    )


GroupRulesControlPanel = {
    'name': 'kotti_group_rules',
    'title': _(u'Group Rules'),
    'description': _(u"Set rules for group members"),
    'success_message': _(u"Successfully saved settings."),
    'schema_factory': GroupRulesSchema,
}