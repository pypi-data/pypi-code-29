import numpy as np
import os
import types
from phys import units, constants, elements
from ..tools import (make_spectrum, lock_spectrum, merge_spectra, l2norm,
    correct_solar_modulation, eval_string, dict_join, data_dir)


def parse_txt(filename, name, columns={}, dtype=float, condition= None,
              eval_cols=['energy_unit', 'flux_unit', 'value_unit'],
              converters=None, reference=None, energy_systematic=0.0,
              energy_unit=None, value_unit=None, energy_scale=None,
              scale=1., skip_header=None, skip_footer=None,
              is_fraction=False):
    if not os.path.isabs(filename):
        filename = os.path.join(data_dir, filename)

    kwargs = {}
    if not skip_header is None:
        kwargs['skip_header'] = skip_header
    if not skip_footer is None:
        kwargs['skip_footer'] = skip_footer

    if dtype and type(dtype) == np.dtype and dtype.names:
        default_columns = dict([(n,n) for n in dtype.names])
        default_columns.update(columns)
        columns = default_columns
    elif not columns:
        columns = {'energy':0, 'flux':1, 'error_minus':2, 'error_plus':3, 'scale':4}
    for err in ('error', 'sys_error'):
        if err in columns:
            for suffix in ('_minus', '_plus'):
                assert err + suffix not in columns
                columns[err + suffix] = columns[err]
            del columns[err]

    converters = {}
    for n in eval_cols:
        if n in columns.keys() and n in dtype.names:
            if dtype.names:
                i = [i for i,col in enumerate(dtype.names) if col==n][0]
            elif type(columns[n]) == int:
                i = columns[n]
            else:
                raise Exception("Found '%s' in the column names, but I can't determine the column number (dtype: %s, columns: %s)"%(n, dtype, columns))
            converters[i] = eval_string

    table = np.genfromtxt(filename, converters=converters, dtype=dtype, **kwargs).T
    spectrum = make_spectrum(table.T.shape[0], name=name)

    if scale:
        if type(scale) == str:
            scale = eval(scale)
        if type(scale) == types.LambdaType:
            scale = scale(table)
    if 'scale' in columns:
        scale = scale*table[columns['scale']]

    spectrum.reference = reference
    spectrum.energy_systematic = energy_systematic
    spectrum.is_fraction = is_fraction

    if energy_unit: energy_unit = eval_string(energy_unit)
    elif 'energy_unit' in columns: energy_unit = table[columns['energy_unit']]
    else: energy_unit = 1.

    if value_unit: value_unit = eval_string(value_unit)
    elif 'value_unit' in columns: value_unit = table[columns['value_unit']]
    else: value_unit = 1.

    if energy_scale and energy_scale == 'log':
        spectrum['energy'] = 10**table[columns['energy']]*energy_unit
    else:
        spectrum['energy'] = table[columns['energy']]*energy_unit

    for n in ('value', 'error_minus', 'error_plus',
              'sys_error_minus', 'sys_error_plus'):
        if n in columns:
            spectrum[n] = table[columns[n]]*scale*value_unit
    for err in ('error', 'sys_error'):
        for target_suffix, source_suffix in zip(('_minus', '_plus'), ('_low', '_high')):
            if (err + source_suffix) in columns:
                spectrum[err + target_suffix] = np.abs(table[columns[err + source_suffix]] - spectrum['value'])
    if not condition is None:
        spectrum.data = spectrum.data[condition(table)]

    lock_spectrum(spectrum)
    return spectrum

