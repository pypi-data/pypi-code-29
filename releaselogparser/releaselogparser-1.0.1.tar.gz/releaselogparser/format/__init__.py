"""
Release History Format implementations

To implement a new format, drop into this directory a python source defining
a subclass of ReleaseHistory with the new implementation. The name for the
new format must be defined in the 'format' subclass attribute. This attribute
can be either a string or a list of strings. Use the latter form to define
aliases.

The name of the file normally used to keep release history in this format
must be stored in the 'filename' attribute.

For example

  class NewHistoryFormat(ReleaseHistory):
      format = 'newformat'
      filename = 'HISTORY.txt'
      ...

See the ReleaseHistory documentation for details.
"""
