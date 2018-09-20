import numpy as np
import os
import types
from xml.dom.minidom import parse as minidom_parse, Node
from io import StringIO
from phys import units, constants, elements
from ..tools import (make_spectrum, lock_spectrum, merge_spectra, l2norm,
    correct_solar_modulation, eval_string, dict_join, data_dir)


def parse_xml(filename):
    if not os.path.isabs(filename):
        filename = os.path.join(data_dir, filename)

    try:
        doc = minidom_parse(filename)
    except:
        print "error reading file %s" % filename
        raise

    root_node = doc.firstChild

    if root_node.nodeName not in ("flux", "fraction"):
        raise ValueError("root node must be flux or fraction")

    is_flux = root_node.nodeName == "flux"

    consumed_nodes = set()
    all_child_nodes = set()
    node = root_node.firstChild
    while node:
        if node.nodeType == Node.ELEMENT_NODE:
            all_child_nodes.add(node.nodeName)
        node = node.nextSibling

    def get_node_data(name, converter=None, **kwargs):
        node_list = root_node.getElementsByTagName(name)
        if not node_list:
            if "default" in kwargs:
                return kwargs["default"]
            else:
                raise SystemExit("%s: node \'%s\' must be defined" % (filename, name))
        if len(node_list) > 1:
            raise SystemExit("%s: node \'%s\' is defined multiple times" % (filename, name))
        node = node_list[0]
        consumed_nodes.add(node.nodeName)
        s = node.firstChild.data.strip()
        if converter is not None:
            try:
                return converter(s)
            except:
                print "%s: conversion of string \'%s\' failed" % (filename, s)
                raise
        else:
            return s

    columns = get_node_data('columns',
        converter=lambda s: {n:i for i,n in enumerate(s.split())})

    table = get_node_data('table',
        converter=lambda s: np.genfromtxt(StringIO(s), dtype=float).T)

    table_dict = {x:table[columns[x]] for x in columns}
    func_dict = {x:getattr(np, x) for x in dir(np)}
    func_dict["l2norm"] = l2norm

    scale = get_node_data('scale',
        converter=lambda s: eval(s, dict_join({"table": table}, func_dict)),
        default=1.0)

    if 'scale' in columns:
        scale = scale * table[columns['scale']]

    # normalize errors
    for err in ('error', 'sys_error'):
        if err in columns:
            for suffix in ('_minus', '_plus'):
                assert err + suffix not in columns
                columns[err + suffix] = columns[err]
            del columns[err]
        for suf, suffix in (('_min', '_minus'),
                            ('_max', '_plus')):
            if err + suf in columns:
                assert err + suffix not in columns
                icol = columns[err + suffix] = columns[err + suf]
                table[icol] = np.abs(table[icol] - table[columns["value"]])
                del columns[err + suf]

    spectrum = make_spectrum(table.shape[-1])
    spectrum.name = get_node_data('name', default=None)
    if spectrum.name is None:
        print "Warning: name is missing for %s" % filename
    spectrum.reference = get_node_data('reference', default=None)
    if spectrum.reference is None:
        print "Warning: reference is missing for %s" % filename
    spectrum.verified = get_node_data('verified',
        converter=lambda s: {"true": True, "1": True, "yes": True,
                             "false": False, "0": False, "no": False}[s.lower()],
        default=False)
    if is_flux:
        spectrum.interaction_model = get_node_data('interaction_model',
                                                   default=None)
    else: # for fractions interaction_model is required
        spectrum.interaction_model = get_node_data('interaction_model', default=None)
        spectrum.is_fraction = True

    spectrum.energy_systematic = get_node_data('energy_systematic',
                                               converter=float,
                                               default=0.0)

    energy_unit = get_node_data('energy_unit', converter=eval_string)
    value_unit = get_node_data('value_unit',
                               converter=eval_string) if is_flux else 1.0

    energy_convert = get_node_data('energy_conversion',
                                   converter=lambda s : eval("lambda x:" + s, func_dict),
                                   default=lambda x : x)

    for suffix in ("_min", "_max", ""):
        fin = "x" + suffix
        fout = "energy" + suffix
        if fin in columns:
            spectrum[fout] = energy_convert(table[columns[fin]]) * energy_unit
    # fill missing
    if "x_min" not in columns:
        spectrum["energy_min"] = spectrum["energy_max"] = spectrum["energy"]
    if "x" not in columns:
        spectrum["energy"] = (spectrum["energy_min"] *
                              spectrum["energy_max"]) ** 0.5

    for n in ('value', 'error_minus', 'error_plus',
              'sys_error_minus', 'sys_error_plus'):
        if n in columns:
            spectrum[n] = table[columns[n]] * scale * value_unit

    value_sys_compute = get_node_data('value_systematic', default=None)
    if value_sys_compute is not None:
        for ch in ("minus", "plus"):
            s = spectrum['sys_error_' + ch]
            sys = np.empty(len(spectrum))
            for i in range(len(sys)):
                sys[i] = eval(value_sys_compute,
                              dict_join({k: spectrum[k][i] for k in ("energy", "value")},
                                        func_dict, units.__dict__))
            s[:] = l2norm(s, sys)

    if all_child_nodes != consumed_nodes:
        raise SystemExit("%s: unrecognized nodes %s" % (filename,
                            list(all_child_nodes - consumed_nodes)))

    lock_spectrum(spectrum)

    return spectrum

