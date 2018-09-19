""" Select widget
"""
from eea.facetednavigation.widgets.select.widget import Widget
from eea.facetednavigation import EEAMessageFactory as _
from eea.facetednavigation.widgets import ViewPageTemplateFile


class Widgettaxonomy(Widget):
    """ Widget
    """
    widget_type = 'select'
    widget_label = _('taxonomy_widget')
    index = ViewPageTemplateFile('widget.pt')

    def taxonomy(self):
        taxonomy = Taxonomy(default_value=self.default or '')
        for term in self.vocabulary():
            taxonomy.add_term(
                term[0],
                self.translate(term[1]),
            )
        return taxonomy


class Taxonomy(object):

    def __init__(self, default_value, groups=False):
        self.default_value = default_value
        self.groups = groups
        self._items = []
        self._parents = [None]
        self._last_level = None

    def add_term(self, id, label):
        element = TaxonomyElement(id, label)
        if self._last_level is None:
            self._last_level = element.level

        if element.level > self._last_level:
            self._parents.append(self._items[-1])
        elif element.level < self._last_level:
            self._parents = self._parents[:element.level]
        element.define_parent(self._parents[-1])

        self._items.append(element)
        self._last_level = element.level

    def render(self):
        html = []
        for element in [e for e in self._items if e.level == 1]:
            html.append(element.render(self.default_value, groups=self.groups))
        return u''.join(html)


class TaxonomyElement(object):

    def __init__(self, id, label):
        self.id = id
        self.label = label.split(u'\xbb')[-1]
        self.level = len(label.split(u'\xbb'))
        self.parent = None
        self.childs = []

    def __iter__(self):
        yield self.id
        yield self.id_label

    def __repr__(self):
        return u'<TaxonomyElement ({0})>'.format(self.id)

    @property
    def css_class(self):
        css = [u'taxonomy-level-{0}'.format(self.level)]
        if self.has_child is True:
            css.append(u'taxonomy-meta-level-{0}'.format(self.level))
            css.append(u'meta')
        return u' '.join(css)

    def define_parent(self, parent):
        if parent:
            self.parent = parent
            self.parent.add_child(self)

    def add_child(self, child):
        self.childs.append(child)

    @property
    def has_child(self):
        return len(self.childs) > 0

    def render(self, default_value, groups=False):
        html = []
        if self.has_child is True:
            group = u'<optgroup label="{label}" class="{css} taxonomy-group">'
            html.append(group.format(
                css=u'group-level-{0}'.format(self.level),
                label=self.label,
            ))
            if groups is False:
                html.append(u'</optgroup>')
            html.append(self.render_option(default_value))
            for child in self.childs:
                html.append(child.render(default_value, groups=groups))
            if groups is True:
                html.append(u'</optgroup>')
        else:
            html.append(self.render_option(default_value))
        return u''.join(html)

    def render_option(self, default_value):
        html = (u'<option {selected} value="{id}" title="{label}" '
                u'class="{css_class}">{label}</option>')
        selected = ''
        if self.id == default_value:
            selected = u'selected="selected"'
        return html.format(
            selected=selected,
            id=self.id,
            label=self.label,
            css_class=self.css_class,
        )
