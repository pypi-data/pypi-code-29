#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:04:08 2018

@author: Antony Holmes
"""
def parse_arg(x):
    """
    Parse a string argument and attempt to turn numbers into actual
    number types.
    
    Parameters
    ----------
    x : str
        A string arg.
    
    Returns
    -------
    str, float, or int
        x type converted.
    """
    
    if x.replace('.', '').isdigit():
        if x.isdigit():
            x = int(x)
        else:
            x = float(x)
                
    return x


def parse_params(request, *args, **kwargs):
    """
    Parse ids out of the request object and convert to ints and add
    as a named list to the id_map.
    
    Parameters
    ----------
    request : request
        URL request
    *args
        List of strings of id names to parse
    **kwargs
        If a map parameter named 'id_map' is passed through kwargs,
        it will have the ids loaded into it. In this way existing
        maps can be used/reused with this method rather than creating
        a new map each time.
        
    Returns
    -------
    dict
        dictionary of named ids where each entry is a list of numerical
        ids. This is to allow for multiple parameters with the same
        name.
    """
    
    if 'id_map' in kwargs:
        id_map = kwargs['id_map']
    else:
        id_map = {}
    
    for p in args:
        if isinstance(p, dict):
            # If p is a dict then assume the value is the default value
            # and the name is the key. Furthermore assume dict only
            # contains one entry
            names = p.keys()
        elif isinstance(p, tuple):
            # If p is a dict then assume the value is the default value
            # and the name is the key. Furthermore assume dict only
            # contains one entry
            names = [p[0]]
        elif isinstance(p, str):
            names = [p]
        else:
            # arg seems invalid so skip it
            names = []
        
        for name in names:
            if name in request.GET:
                # if the sample id is present, pass it along
                values = [parse_arg(x) for x in request.GET.getlist(name)]
                
                if len(values) > 0:
                    # Only add non empty lists to dict
                    id_map[name] = values
            else:
                # If arg does not exist, supply a default
                if isinstance(p, dict):
                    # values of args are returned as a list even if there
                    # is only one arg
                    id_map[name] = [p[name]]
                elif isinstance(p, tuple):
                    id_map[name] = [p[1]]
                else:
                    pass
            
    return id_map
