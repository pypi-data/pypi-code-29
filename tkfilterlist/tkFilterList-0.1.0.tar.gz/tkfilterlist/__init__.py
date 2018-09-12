#!/usr/bin/env python

"""A self-filtering Listbox with text entry for Tkinter.

tkFilterList is a combination of the Tkinter Listbox and Entry widgets
that updates to display matching items as you type.

You can customize the item display and filtering behavior by setting
its display_rule and filter_rule options, respectively, to your own
custom functions:

  display_rule(item)
    Returns the display text for the specified item.

  filter_rule(item, text)
    Returns True if the text argument matches the specified item,
    False otherwise.

This allows tkFilterList to process lists containing complex datatypes,
including other lists, tuples, and even entire classes.

If you do not define a custom display_rule, tkFilterList will assume
your source values are strings and behave like a standard Listbox.

If you do not define a custom filter_rule, tkFilterList will display
items starting with the entered text (case-insensitive).
"""

from .widget import FilterList

# The only thing we need to publicly export is the widget itself
__all__ = ["FilterList"]
