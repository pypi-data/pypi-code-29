# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

from openbases.logger import bot
from openbases.utils import read_yaml
import os
import re
import sys
  
from .utils import (
    load_deid,
    get_deid,
    load_combined_deid
)
from deid.config.standards import (
    actions,
    sections,
    formats
)

from deid.logger import bot
import os
import re

bot.level = 3

class DeidRecipe:
    '''
       Create and work with a deid recipe to filter and perform operations on
       a dicom header. Usage typically looks like:

       deid = 'dicom.deid'
       recipe = DeidRecipe(deid)
       
       If deid is None, the default provided by the application is used.

       Parameters
       ==========
           deid: the deid recipe (or recipes) files to use. If more than one
                 is provided, should be done in order of preference for load
                 (later in the list overrides earlier loaded).
           base: if True, load a default base (default_base) before custom
           default_base: the default base to load if "base" is True
    '''
    
    def __init__(self, deid=None, base=False, default_base='dicom'):

        # If deid is None, use the default
        if deid is None:
            bot.warning('No specification, loading default base deid.%s' %default_base)
            base = True

        self._init_deid(deid, base=base, default_base=default_base)

    def __str__(self):
        return '[deid]'

    def __repr__(self):
        return '[deid]'

    def load(self, deid):
        '''
           load a deid recipe into the object. If a deid configuration is
           already defined, append to that. 
        '''
        deid = get_deid(deid)
        if deid is not None:
 
            # Update our list of files
            self._files.append(deid)
            self.files = list(set(self.files))

            # Priority here goes to additional deid
            self.deid = load_combined_deid([self.deid, deid])

    def _get_section(self, name):
        '''
           return a section (key) in the loaded deid, if it exists
        '''
        section = None
        if self.deid is not None:
            if name in self.deid:
                section = self.deid[name]
        return section


    def get_format(self):
        '''return the format of the loaded deid, if one exists
        '''
        return self._get_section('format')


    def get_filters(self, name=None):
        '''return all filters for a deid recipe, or a set based on a name
        '''
        filters = self._get_section('filter')
        if name is not None and filters is not None:
            filters = filters[name]        
        return filters


    def ls_filters(self):
        '''list names of filter groups
        '''
        filters = self._get_section('filter')
        return list(filters.keys())

    def get_actions(self, action=None, field=None):
        '''get deid actions to perform on a header, or a subset based on a type

        A header action is a list with the following:
         {'action': 'REMOVE', 'field': 'AssignedLocation'},
 
        Parameters
        ==========
        action: if not None, filter to action specified
        field: if not None, filter to field specified

        '''
        header = self._get_section('header')
        if header is not None:
            if action is not None:
                action = action.upper()
                header = [x for x in header if x['action'].upper() == action]      
            if field is not None:
                field = field.upper()
                header = [x for x in header if x['field'].upper() == field]  

        return header


    def _init_deid(self, deid=None, base=False, default_base='dicom'):
        '''
        initalize the recipe with one or more deids, optionally including 
        the default. This function is called at init time. If you need to add
        or work with already loaded configurations, use add/remove 
    
        Parameters
        ==========
            deid: the deid recipe (or recipes) files to use. If more than one
                  is provided, should be done in order of preference for load
                  (later in the list overrides earlier loaded).
            default_base: load the default base before the user customizations. 
        '''
        if deid is None:
            deid = []

        if not isinstance(deid,list):
            deid = [deid]

        if base is True:
            deid.append(default_base)

        self._files = deid

        if len(deid) == 0:
            bot.info('You can add custom deid files with .load().')
        self.deid = load_combined_deid(deid)


class Journal:
    joss = 'joss'
    rse = 'rse'

class Author:
    '''an Author holds a name, orcid id, and affiliation'''
    def __init__(self, 
                 name, 
                 orcid, 
                 affiliation):
        self.name = name
        self.orcid = orcid
        self.affiliation = affiliation


class Paper:

    def __init__(self, filename, quiet=False):

        self._check_inputs(filename)
        self.metadata = read_yaml(filename, quiet=quiet)

    def __str__(self):
        return "<paper.md: %s>" % self.filename

    def __repr__(self):
        return self.__str__()

    def __contains__(self, value):
        return value in self.metadata

    def _check_inputs(self, filename):
        '''check to make sure that filename exists
           Parameters
           ==========
           filename: the markdown file to parse
        '''
        if not os.path.exists(filename):
            bot.exit('Cannot find %s' % filename)
        self.filename = os.path.abspath(os.path.realpath(filename))


    def get(self, key, quiet=True, sep=',', field=None):
        '''return a key from the yaml, default is silent (no print) if doesn't
           exist. If the yaml item is a list with different subfields, then
           field must also be defined.
        '''
        # If the arg is of format arg:field will return field from list
        key = key.split(':')
        if len(key) > 1:
            field = key[1]

        key=key[0]

        if key in self.metadata:
    
            value = self.metadata[key]

            if isinstance(value, (tuple, list)):

                # If the first entry is a dict
                if isinstance(value[0], dict):
                    values = []

                    for entry in value:
                        if field in entry and field is not None:
                            if entry[field]:
                                values.append(entry[field])
                    value = values

                print(sep.join(value))
            else:
                print(self.metadata[key])
