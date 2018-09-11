import copy

from django.dispatch import receiver
from django.template.loader import get_template
from django.urls import resolve, reverse
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

from pretix.base.models import Event, Order
from pretix.base.signals import (
    event_copy_data, item_copy_data, logentry_display, logentry_object_link,
    register_data_exporters,
)
from pretix.control.signals import item_forms, nav_event, order_info
from pretix.plugins.badges.forms import BadgeItemForm
from pretix.plugins.badges.models import BadgeItem, BadgeLayout


@receiver(nav_event, dispatch_uid="badges_nav")
def control_nav_import(sender, request=None, **kwargs):
    url = resolve(request.path_info)
    p = (
        request.user.has_event_permission(request.organizer, request.event, 'can_change_settings', request)
        or request.user.has_event_permission(request.organizer, request.event, 'can_view_orders', request)
    )
    if not p:
        return []
    return [
        {
            'label': _('Badges'),
            'url': reverse('plugins:badges:index', kwargs={
                'event': request.event.slug,
                'organizer': request.event.organizer.slug,
            }),
            'active': url.namespace == 'plugins:badges',
            'icon': 'id-card',
        }
    ]


@receiver(item_forms, dispatch_uid="badges_item_forms")
def control_item_forms(sender, request, item, **kwargs):
    try:
        inst = BadgeItem.objects.get(item=item)
    except BadgeItem.DoesNotExist:
        inst = BadgeItem(item=item)
    return BadgeItemForm(
        instance=inst,
        event=sender,
        data=(request.POST if request.method == "POST" else None),
        prefix="badgeitem"
    )


@receiver(item_copy_data, dispatch_uid="badges_item_copy")
def copy_item(sender, source, target, **kwargs):
    try:
        inst = BadgeItem.objects.get(item=source)
        BadgeItem.objects.create(item=target, layout=inst.layout)
    except BadgeItem.DoesNotExist:
        pass


@receiver(signal=event_copy_data, dispatch_uid="badges_copy_data")
def event_copy_data_receiver(sender, other, item_map, **kwargs):
    layout_map = {}
    for bl in other.badge_layouts.all():
        oldid = bl.pk
        bl = copy.copy(bl)
        bl.pk = None
        bl.event = sender
        bl.save()

        if bl.background and bl.background.name:
            bl.background.save('background.pdf', bl.background)

        layout_map[oldid] = bl

    for bi in BadgeItem.objects.filter(item__event=other):
        BadgeItem.objects.create(item=item_map.get(bi.item_id), layout=layout_map.get(bi.layout_id))


@receiver(register_data_exporters, dispatch_uid="badges_export_all")
def register_pdf(sender, **kwargs):
    from .exporters import BadgeExporter
    return BadgeExporter


@receiver(order_info, dispatch_uid="badges_control_order_info")
def control_order_info(sender: Event, request, order: Order, **kwargs):

    template = get_template('pretixplugins/badges/control_order_info.html')

    ctx = {
        'order': order,
        'request': request,
        'event': sender,
    }
    return template.render(ctx, request=request)


@receiver(signal=logentry_display, dispatch_uid="badges_logentry_display")
def badges_logentry_display(sender, logentry, **kwargs):
    if not logentry.action_type.startswith('pretix.plugins.badges'):
        return

    plains = {
        'pretix.plugins.badges.layout.added': _('Badge layout created.'),
        'pretix.plugins.badges.layout.deleted': _('Badge layout deleted.'),
        'pretix.plugins.badges.layout.changed': _('Badge layout changed.'),
    }

    if logentry.action_type in plains:
        return plains[logentry.action_type]


@receiver(signal=logentry_object_link, dispatch_uid="badges_logentry_object_link")
def badges_logentry_object_link(sender, logentry, **kwargs):
    if not logentry.action_type.startswith('pretix.plugins.badges.layout') or not isinstance(logentry.content_object,
                                                                                             BadgeLayout):
        return

    a_text = _('Badge layout {val}')
    a_map = {
        'href': reverse('plugins:badges:edit', kwargs={
            'event': sender.slug,
            'organizer': sender.organizer.slug,
            'layout': logentry.content_object.id
        }),
        'val': escape(logentry.content_object.name),
    }
    a_map['val'] = '<a href="{href}">{val}</a>'.format_map(a_map)
    return a_text.format_map(a_map)
