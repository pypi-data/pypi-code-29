# Copyright 2013-2014 Oliver Cope
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from copy import copy
from functools import partial
from itertools import repeat, count
import json
import operator

from .compat import ustr
from .htmlbuilder import Tag
from .types import Undefined
from .iterable import iterable
from .choices import expand_choices, OptGroup

null_ids = repeat(None)


def _selectedonce(current, selected='selected', comparator=operator.eq):
    """
    Return a function returning the string 'selected' the first time (and
    only the first time) that a value matching  ``current`` is passed into it.
    """
    _toggle = []

    def _selectedonce(v):
        if comparator(current, v) and not _toggle:
            _toggle.append(1)
            return selected
        return None
    return _selectedonce


def _selectedmany(
        current, selected='selected', comparator=operator.contains):
    """
    Return a function returning the string 'selected' whenever
    a value contained in ``current`` is passed to it.
    """
    def _selectedmany(v):
        if comparator(current, v):
            return selected
        return None
    return _selectedmany


class Widget(object):
    """
    Renders a HTML form control widget.
    """

    #: HTML attributes to add to the input element
    attrs = {}

    #: Whether this widget generates user-visible output
    is_visible = True

    #: The raw input value. This can be either the raw value converted from the
    #: bound object or the input direct from the user when redisplaying a form
    #: with validation errors
    raw = None

    #: The original bound value, or the user's input converted into the
    #: destination type. Named field_value so as not to clash with an <input>
    #: widget's value attribute.
    field_value = None

    #: The fully qualified fieldname used for the widget.
    fieldname = None

    #: The choice of values allowable for input
    choices = None

    def __init__(self, **kwargs):
        super(Widget, self).__init__()
        self.choices = kwargs.pop('choices', None)
        self.attrs = dict(self.attrs, **kwargs)

    def configure(self, fieldname, raw, value, choices=None, required=True):
        self.fieldname = fieldname
        self.raw = raw
        self.field_value = value
        if required:
            self.attrs = dict(self.attrs, required='')
        if choices is not None:
            self.choices = choices

    def render(self, **kwargs):
        raise NotImplementedError

    def extract_raw(self, raw):
        return raw

    def copy(self):
        """
        Return a copy of the Widget.

        All top-level attributes are independently copied.
        """
        ob = object.__new__(self.__class__)
        ob.__dict__.update((k, copy(v)) for k, v in self.__dict__.items())
        return ob


class _Input(Widget):
    """
    Base <input type="..."/> widget
    """
    type = 'text'

    def render(self, **kwargs):
        return Tag.input(type=self.type, name=self.fieldname, value=self.raw,
                         **dict(self.attrs, **kwargs))


class HiddenInput(_Input):
    is_visible = False
    type = 'hidden'


class TextInput(_Input):
    """
    An HTML text input
    """


class PasswordInput(_Input):
    """
    An HTML password input
    """
    type = 'password'


class ColorInput(_Input):
    type = 'color'


class DateInput(_Input):
    type = 'date'


class DatetimeInput(_Input):
    type = 'datetime'


class EmailInput(_Input):
    type = 'email'


class MonthInput(_Input):
    type = 'month'


class NumberInput(_Input):
    type = 'number'


class RangeInput(_Input):
    type = 'range'


class SearchInput(_Input):
    type = 'search'


class TelInput(_Input):
    type = 'tel'


class TimeInput(_Input):
    type = 'time'


class UrlInput(_Input):
    type = 'url'


class WeekInput(_Input):
    type = 'week'


class HiddenJSON(Widget):
    """
    A <input type="hidden" /> field with a JSON encoded value.
    """

    is_visible = False
    encoder = json.JSONEncoder
    decoder = json.JSONDecoder

    def extract_raw(self, raw):
        if raw is Undefined:
            return Undefined
        try:
            return json.loads(raw, cls=self.decoder)
        except (TypeError, ValueError):
            return Undefined

    def render(self, **kwargs):
        if self.field_value is Undefined:
            return Tag()
        return Tag.input(type='hidden',
                         name=self.fieldname,
                         value=json.dumps(self.field_value, cls=self.encoder),
                         **dict(self.attrs, **kwargs))


class Checkbox(_Input):
    type = 'checkbox'
    value = 'Y'
    default_checked = False

    def __init__(self, *args, **kwargs):
        self.default_checked = kwargs.pop('default_checked',
                                          self.default_checked)
        super(Checkbox, self).__init__(*args, **kwargs)

    def configure(self, fieldname, raw, value, choices=None, required=True):
        """
        TODO: support required attribute on checkboxes
        """
        return super(Checkbox, self).configure(
            fieldname, raw, value, choices, False)

    def render(self, **kwargs):
        checked = self.default_checked
        if self.raw is not Undefined:
            checked = bool(self.raw)

        control = super(Checkbox, self).render(**kwargs)
        control.attrs['value'] = self.value
        control.attrs['checked'] = 'checked' if checked else None
        return control


class ChoiceMapper(object):
    """
    Map from object choice values to strings and back again
    """
    OPTGROUP = object()

    def indexed_choices(self, choices):
        """
        Return an iterator over the list of choices annotated with
        the key to use as the ``value`` attribute in the widget
        """
        raise NotImplementedError()

    def choice_map(self, choices):
        """
        Return a mapping from key values as generated by ``indexed_choices``
        back to the original choice value objects
        """
        raise NotImplementedError()


class JSONChoiceMapper(ChoiceMapper):
    """
    A :class:`ChoiceMapper` implementation that encodes values as JSON strings
    """
    def indexed_choices(self, choices):
        from json import dumps
        for v, l in choices:
            if isinstance(l, OptGroup):
                yield (self.OPTGROUP, self.indexed_choices(l), ustr(v))
            else:
                yield dumps(v), v, ustr(l)

    def choice_map(self, choices):
        return self

    def __getitem__(self, key):
        from json import loads
        try:
            return loads(key)
        except (TypeError, ValueError):
            return Undefined


class IndexChoiceMapper(ChoiceMapper):
    """
    A :class:`ChoiceMapper` implementation that adds a integer index based
    key to map to and from choice values
    """

    def indexed_choices(self, choices, counter=None):
        """
        Return an iterator over the list of choices annotated with
        the key to use as the ``value`` attribute in the widget
        """
        if counter is None:
            counter = count()

        for v, l in choices:
            if isinstance(l, OptGroup):
                yield (self.OPTGROUP,
                       self.indexed_choices(l, counter),
                       ustr(v))
            else:
                yield ustr(next(counter)), v, ustr(l)

    def choice_map(self, choices):
        """
        Return a mapping from choice indices to values
        """
        def build_list(choices):
            items = []
            for v, l in choices:
                if isinstance(l, OptGroup):
                    items.extend(build_list(l))
                else:
                    items.append(v)
            return items
        return dict((ustr(ix), item)
                    for ix, item in enumerate(build_list(choices)))


class SingleChoiceWidget(Widget):
    """
    A widget with a fixed list of choices
    """
    choices = None
    choice_mapper = JSONChoiceMapper()

    def __init__(self, *args, **kwargs):
        self.choice_mapper = kwargs.pop('mapper', self.choice_mapper)
        super(SingleChoiceWidget, self).__init__(*args, **kwargs)

    def configure(self, fieldname, raw, value, choices=None, required=True):
        if choices is not None:
            choices = expand_choices(choices)
        return super(SingleChoiceWidget, self).configure(fieldname,
                                                         raw,
                                                         value,
                                                         choices,
                                                         required)

    def extract_raw(self, raw):
        if raw is Undefined:
            return raw

        choice_map = self.choice_mapper.choice_map(self.choices)
        try:
            return choice_map[raw]
        except KeyError:
            return Undefined

    def currentselection(self):
        try:
            return self.raw
        except (TypeError, ValueError):
            return Undefined

    def render(self, **kwargs):
        if self.choices is not None:
            choices = list(self.choice_mapper.indexed_choices(self.choices))
        else:
            choices = []
        items = self.render_items(choices, **kwargs)
        return self.render_container(items, **kwargs)

    def render_container(self, items, **kwargs):
        raise NotImplementedError()

    def render_optgroup(self, choices, label, ids=null_ids, **kwargs):
        raise NotImplementedError()

    def render_items(self, choices, **kwargs):
        raise NotImplementedError()


class MultipleChoiceWidget(SingleChoiceWidget):
    """
    Extends the selection to multiple values
    """

    def extract_raw(self, raw):
        if raw is Undefined:
            return raw
        choice_map = self.choice_mapper.choice_map(self.choices)
        try:
            return [choice_map[v] for v in raw]
        except KeyError:
            return Undefined

    def currentselection(self):
        """
        Return the set of currently selected indices
        """
        empty = set()
        raw = self.raw
        try:
            if raw is Undefined:
                return empty
            elif not iterable(raw):
                return set([raw])
            else:
                return set(raw)
        except (TypeError, ValueError):
            return empty


class Select(SingleChoiceWidget):

    selected_decider = partial(_selectedonce, selected='selected')

    def render_container(self, items, **kwargs):
        return Tag.select(items, name=self.fieldname,
                          **dict(self.attrs, **kwargs))

    def render_items(self, choices, **kwargs):
        current = self.currentselection()
        selected = self.selected_decider(
            current, comparator=kwargs.pop('_comparator', operator.eq))

        for ix, v, l in choices:
            if ix is ChoiceMapper.OPTGROUP:
                og_label, og_choices = l, v
                yield self.render_optgroup(og_choices, og_label)
            else:
                yield Tag.option(l,
                                 value=ix,
                                 selected=selected(v))

    def render_optgroup(self, choices, label, ids=null_ids):
        return Tag.optgroup(self.render_items(choices), label=label)


class SelectMulti(Select, MultipleChoiceWidget):

    selected_decider = partial(_selectedmany, selected='checked')

    def render_container(self, items, **kwargs):
        return Tag.select(items, name=self.fieldname, multiple='multiple',
                          **dict(self.attrs, **kwargs))

    def render_items(self, *args, **kwargs):
        comparator = lambda cur, v: cur is not Undefined and v in cur

        return super(SelectMulti, self).render_items(
            _comparator=comparator, *args, **kwargs)


class MultiWidgetRenderingStrategy(object):
    """
    Base rendering strategy for MultiWidgets
    """

    def item(self, widget, labeltext, id):
        raise NotImplementedError()

    def container(self, items):
        return Tag(items)

    def label(self, contents, id):
        return Tag.label(contents, for_=id)

    def optgroup(self, choices, label):
        return Tag.fieldset(Tag.legend(label), choices)


class WidgetFirstMultWidget(MultiWidgetRenderingStrategy):
    """
    Render a MultiWidget as a sequence of label elements, widgets preceding
    labels::

        <input .../><label> option 1</label>
        <input .../><label> option 2</label>
    """

    tag = None

    def _strip_trailing_space(self, items):
        """
        Each label element is rendered with a trailing space.
        Trim this space off the last label tag
        """
        items = list(items)
        if items:
            last = items[-1]
            if last.children and last.children[-1] == ' ':
                last.children = last.children[:-1]
        return items

    def container(self, items):
        return Tag(self._strip_trailing_space(items), name=self.tag)

    def item(self, widget, labeltext, id):
        return Tag(widget, ' ', self.label(labeltext, id), u' ')

    def optgroup(self, choices, label):
        return Tag.fieldset(Tag.legend(label),
                            self._strip_trailing_space(choices))


class LabelFirstMultiWidget(WidgetFirstMultWidget):
    """
    Render a MultiWidget as a sequence of label elements, labels preceding
    widgets::

        <label>option 1 <input .../></label>
        <label>option 2 <input .../></label>
    """
    def item(self, widget, labeltext, id):
        return Tag(self.label([labeltext, u' ', widget], id), u' ')


class ULMultiWidget(MultiWidgetRenderingStrategy):
    """
    Render a MultiWidget as an unordered list::

        <ul>
            <li><label>option 1 <input .../></label></li>
            <li><label>option 2 <input .../></label></li>
        </ul>
    """

    def item(self, widget, labeltext, id):
        return Tag.li(widget, ' ', self.label(labeltext, id))

    def container(self, items):
        return Tag.ul(*list(items))


class TableMultiWidget(MultiWidgetRenderingStrategy):
    """
    Render a MultiWidget as a table::

        <table>
            <tbody>
                <tr>
                    <td><input .../></td>
                    <td><label>option 1</label></td>
                </tr>
            </tbody>
        </table>
    """

    def item(self, widget, labeltext, id):
        return Tag.tr(Tag.td(widget), Tag.td(self.label(labeltext, id)))

    def container(self, items):
        return Tag.table(Tag.tbody(items))


class RadioGroup(SingleChoiceWidget):
    """
    Use this widget for radio buttons to chose between items::

        color = fields.Str(choices=['red', 'yellow'],
                        widget=widgets.RadioGroup())

    Variants exist to render the input controls in different HTML markup
    structures:

        - ``RadioGroup.label_first()`` - render each option with
          the label preceding the input control
        - ``RadioGroup.as_table()`` - render options inside an HTML table
        - ``RadioGroup.as_ul()`` - render options as an HTML unordered list

    If you need to customize radio group rendering,
    you can do so by creating a custom subclass of
    :class:`MultiWidgetRenderingStrategy`
    """

    type = 'radio'
    rendering_strategy = WidgetFirstMultWidget()
    selected_decider = partial(_selectedonce, selected='checked')

    def __init__(self, *args, **kwargs):
        self.input_attrs = {}
        self.rendering_strategy = kwargs.pop('rendering_strategy',
                                             self.rendering_strategy)
        super(RadioGroup, self).__init__(*args, **kwargs)

    def configure(self, fieldname, raw, value, choices, required):
        if required:
            self.input_attrs['required'] = ''
        return super(RadioGroup, self).configure(fieldname,
                                                         raw,
                                                         value,
                                                         choices,
                                                         False)

    def label_textfirst(widget, labeltext):
        return [labeltext, u' ', widget]

    def label_widgetfirst(widget, labeltext):
        return [widget, u' ', labeltext]

    @classmethod
    def as_ul(cls, *args, **kwargs):
        return cls(rendering_strategy=ULMultiWidget(), *args, **kwargs)

    @classmethod
    def as_table(cls, *args, **kwargs):
        return cls(rendering_strategy=TableMultiWidget(), *args, **kwargs)

    @classmethod
    def label_first(cls, *args, **kwargs):
        return cls(rendering_strategy=LabelFirstMultiWidget(), *args, **kwargs)

    def render_container(self, items, **kwargs):
        container = self.rendering_strategy.container(items)
        if self.attrs or kwargs:
            # Ensure we promote to an element container if we have to add
            # attributes
            container.name = container.name or 'div'
        container.update(**dict(self.attrs, **kwargs))
        return container

    def render_optgroup(self, choices, l, ids=null_ids):
        return self.rendering_strategy.optgroup(
                self.render_items(choices, ids), l)

    def render_items(self, choices, ids=null_ids, **kwargs):
        selected = self.selected_decider(self.currentselection())

        if ids is null_ids:
            baseid = kwargs.pop('id', None)
            if baseid is not None:
                ids = ('{0}-{1}'.format(baseid, c) for c in count())

        for ix, v, l in choices:
            if ix is ChoiceMapper.OPTGROUP:
                og_label, og_choices = l, v
                yield self.render_optgroup(og_choices, og_label, ids)
            else:
                id = next(ids)
                widget = Tag.input(type=self.type, name=self.fieldname, id=id,
                                   value=ix, checked=selected(v),
                                   **dict(self.input_attrs, **kwargs))
                yield self.rendering_strategy.item(widget, l, id)


class CheckboxGroup(RadioGroup, MultipleChoiceWidget):
    """
    Use this widget for groups of checkboxes. See the documentation for
    :class:`RadioGroup` for information on how to customize the rendering of
    this widget.
    """
    type = 'checkbox'
    selected_decider = partial(_selectedmany, selected='checked')

    def configure(self, fieldname, raw, value, choices, required):
        """
        TODO: support required attribute on checkbox group
        """
        return super(CheckboxGroup, self).configure(fieldname,
                                                    raw,
                                                    value,
                                                    choices,
                                                    False)


class Textarea(Widget):

    def render(self, **kwargs):
        return Tag.textarea(ustr(self.raw), name=self.fieldname,
                            **dict(self.attrs, **kwargs))
