import json as jsonlib

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def json(value):
    uncleaned = jsonlib.dumps(value)
    return mark_safe(uncleaned)


# Duplicate code to improve autodoc
@register.inclusion_tag("react/react_root.html", takes_context=True)
def react_root(context):
    context['react_root_id'] = 'react_root'
    return context


@register.inclusion_tag("react/react_scripts.html", takes_context=True)
def react_scripts(context):
    context['react_root_id'] = 'react_root'
    return context


@register.inclusion_tag("react/react_full.html", takes_context=True)
def react(context):
    context['react_root_id'] = 'react_root'
    return context
