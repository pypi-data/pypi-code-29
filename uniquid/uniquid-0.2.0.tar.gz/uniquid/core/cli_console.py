# Copyright (c) 2018 UniquID

import json
import uniquid.core.constants as constants

# constants
_TAB = '\t'


class CliConsole:
    """Generic object which controls all interactions with the command line and
    the console. Independant of the framework which the tool is built with.
    """

    def __init__(self,
                 in_ok=None,
                 in_error=None,
                 in_output=constants.FORMAT_TEXT,
                 in_exc_ctor=RuntimeError):
        """Create a CliConsole object and store the references to the
           platform specific functions.

           Arguments:
           in_ok -- Framework function to print strings to console.
           in_error -- Framework function to print errors to the console.
           in_output -- Format of output to terminal.
           in_exc_ctor -- Reference to contructor function to create
           exceptions which should be thrown for the framework."""
        self._print_ok = None
        self._print_error = None
        self._raise_exception = None
        self._format = in_output
        self.is_list_mode = False
        self.num_prints = 0
        if in_ok is not None:
            self._print_ok = in_ok
        elif in_ok is not None:
            self._print_warning = in_ok
        if in_error is not None:
            self._print_error = in_error
        elif in_ok is not None:
            self._print_error = in_ok
        self._excp_ctor = in_exc_ctor

    def ok(self, in_string):
        """Print a string using the pre-configured print function."""
        if self._print_ok is None:
            self.exception('Print function not assigned.')
        if (self._format == constants.FORMAT_TEXT):
            self._print_ok(in_string)
        elif (self._format == constants.FORMAT_JSON):
            if (self.is_list_mode and
                    self.num_prints > 0):
                self._print_ok(',')
            self._print_ok('{"message": "' + in_string + '"}')
        else:
            self.exception('Internal error: Unexpected format type')
        self.num_prints = self.num_prints + 1

    def error(self, in_string):
        """Print a string using the pre-configured print function."""
        if self._print_error is None:
            self.exception('Print error function not assigned.')
        if (self._format == constants.FORMAT_TEXT):
            self._print_error('Error: ' + in_string)
        elif (self._format == constants.FORMAT_JSON):
            if (self.is_list_mode and
                    self.num_prints > 0):
                self._print_ok(',')
            self._print_error('{"error": "' + in_string + '"}')
        else:
            self.exception('Internal error: Unexpected format type')
        self.num_prints = self.num_prints + 1

    def exception(self, in_string):
        """Throw an exception which contains the message."""
        raise self._excp_ctor(in_string)

    def begin_list(self):
        """Print prefix lines to all text output for the command.

        Places the object in List mode, which means it expects to print
        multiple data objects to the CLI."""
        if self._print_ok is None:
            self.exception('Print function not assigned.')
        if self._format == constants.FORMAT_JSON:
            self._print_ok('[')
        self.is_list_mode = True

    def end_list(self):
        """Print suffix lines to all text output for the command."""
        if self._print_ok is None:
            self.exception('Print function not assigned.')
        if self._format == constants.FORMAT_JSON:
            self._print_ok(']')
        self.is_list_mode = False
        self.num_prints = 0

    def print_objects(self, in_objs):
        """Print object(s) to the console in the requested format.

        Arguments:
        in_objs -- A Python object. May be a dictionary or a list.
        """
        if self._format == constants.FORMAT_JSON:
            if (self.is_list_mode and
                    self.num_prints > 0):
                self._print_ok(',')
            self._print_ok(json.dumps(in_objs,
                                      sort_keys=False,
                                      indent=4))
        elif self._format == constants.FORMAT_TEXT:
            if isinstance(in_objs, list):
                # print the header from the first object in the list
                if (len(in_objs) > 0 and
                        isinstance(in_objs[0], dict)):
                    key_list = self._get_hier_keys(in_objs[0])
                    self._print_ok(_TAB.join(key_list).upper())
                # print rows for all objects in the list
                for obj in in_objs:
                    self._print_ok(_TAB.join(self._get_hier_values(obj)))
            elif isinstance(in_objs, dict):
                # print the header from the object
                self._print_ok(_TAB.join(self._get_hier_keys(in_objs)).upper())
                # print row with values from object
                self._print_ok(_TAB.join(self._get_hier_values(in_objs)))
            else:
                self.exception('Internal: Unsupported object type: '
                               + str(type(in_objs)))
        else:
            self.exception('Internal: Unsupported text format.')
        self.num_prints = self.num_prints + 1

    def _get_hier_keys(self, in_objs):
        """Get a list of all of the keys in the object hierarchy."""
        retval = list()
        if isinstance(in_objs, list):
            for item in in_objs:
                list_keys = self._get_hier_keys(item)
                retval.extend(list_keys)
        elif isinstance(in_objs, dict):
            for key, value in in_objs.items():
                if (isinstance(value, dict) or
                        isinstance(value, list)):
                    sub_keys = self._get_hier_keys(value)
                    if len(sub_keys) > 0:
                        for sub_key in sub_keys:
                            retval.append(str(key) + '_' + str(sub_key))
                    else:
                        retval.append(str(key))
                else:
                    retval.append(str(key))
        return retval

    def _get_hier_values(self, in_objs):
        """Get a list of all of the values in the object hierarchy."""
        retval = list()
        if isinstance(in_objs, list):
            aglom = list()
            aglom.append('[')
            for item in in_objs:
                list_values = self._get_hier_values(item)
                for value in list_values:
                    aglom.append(str(value))
                if item is not in_objs[-1]:
                    aglom.append(',')
            aglom.append(']')
            retval.append(''.join(aglom))
        elif isinstance(in_objs, dict):
            for item in in_objs.values():
                dict_values = self._get_hier_values(item)
                for item in dict_values:
                    retval.append(str(item))
        else:
            retval.append(str(in_objs))
        return retval
