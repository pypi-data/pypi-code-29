import numpy as np
import os
from phys import units, constants, elements
from ..tools import (make_spectrum, lock_spectrum, merge_spectra, l2norm,
    correct_solar_modulation, eval_string, dict_join, data_dir)

from .parse_xml import parse_xml
from .parse_txt import parse_txt

#location = os.path.join(os.path.dirname(__file__), 'data')
location = os.path.dirname(__file__)


"""
_hires_stereo = np.genfromtxt(data_dir + '/hires/HiResStereo.txt').T
_scale = 1e-30
_flux_unit = 1./(units.m**2*units.s*units.sr*units.eV)
hires_stereo_with_errs = make_spectrum(len(_hires_stereo[0]), name='HiRes Stereo')
hires_stereo_with_errs['energy'] = 10**_hires_stereo[0]*units.EeV
hires_stereo_with_errs['value'] = _hires_stereo[2]*_flux_unit*_scale
hires_stereo_with_errs['error_minus'] = hires_stereo_with_errs['value']*(1-_hires_stereo[7]/_hires_stereo[5])
hires_stereo_with_errs['error_plus'] = hires_stereo_with_errs['value']*(_hires_stereo[8]/_hires_stereo[5] - 1)
hires_stereo_with_errs.reference = 'R.U. Abbasi et al. [Hires Collaboration], Phys. Rev. Lett. 100 (2008) 101101.'
hires_stereo_with_errs.energy_systematic = 0.2
"""

"""
auger_sibyll_fraction = {
    "p": parse_txt('auger/xmax-s21-4.dat','p-fraction (Sibyll 2.1)',
        columns={'energy':0, 'value':1, 'error_low':2, 'sys_error_low':3, 'error_high':4, 'sys_error_high':5},
        is_fraction=True),
    "He": parse_txt('auger/xmax-s21-4.dat','He-fraction (Sibyll 2.1)',
        columns={'energy':0, 'value':6, 'error_low':7, 'sys_error_low':8, 'error_high':9, 'sys_error_high':10},
        is_fraction=True),
    "N": parse_txt('auger/xmax-s21-4.dat','N-fraction (Sibyll 2.1)',
        columns={'energy':0, 'value':11, 'error_low':12, 'sys_error_low':13, 'error_high':14, 'sys_error_high':15},
        is_fraction=True),
    "Fe": parse_txt('auger/xmax-s21-4.dat','Fe-fraction (Sibyll 2.1)',
        columns={'energy':0, 'value':16, 'error_low':17, 'sys_error_low':18, 'error_high':19, 'sys_error_high':20},
        is_fraction=True),
}

auger_qgsjet_fraction = {
    "p": parse_txt('auger/xmax-q04-4.dat','p-fraction (QGSJet II 04)',
        columns={'energy':0, 'value':1, 'error_low':2, 'sys_error_low':3, 'error_high':4, 'sys_error_high':5},
        is_fraction=True),
    "He": parse_txt('auger/xmax-q04-4.dat','He-fraction (QGSJet II 04)',
        columns={'energy':0, 'value':6, 'error_low':7, 'sys_error_low':8, 'error_high':9, 'sys_error_high':10},
        is_fraction=True),
    "N": parse_txt('auger/xmax-q04-4.dat','N-fraction (QGSJet II 04)',
        columns={'energy':0, 'value':11, 'error_low':12, 'sys_error_low':13, 'error_high':14, 'sys_error_high':15},
        is_fraction=True),
    "Fe": parse_txt('auger/xmax-q04-4.dat','Fe-fraction (QGSJet II 04)',
        columns={'energy':0, 'value':16, 'error_low':17, 'sys_error_low':18, 'error_high':19, 'sys_error_high':20},
        is_fraction=True),
}

auger_epos_fraction = {
    "p": parse_txt('auger/xmax-eps-4.dat','p-fraction (EPOS LHC)',
        columns={'energy':0, 'value':1, 'error_low':2, 'sys_error_low':3, 'error_high':4, 'sys_error_high':5},
        is_fraction=True),
    "He": parse_txt('auger/xmax-eps-4.dat','He-fraction (EPOS LHC)',
        columns={'energy':0, 'value':6, 'error_low':7, 'sys_error_low':8, 'error_high':9, 'sys_error_high':10},
        is_fraction=True),
    "N": parse_txt('auger/xmax-eps-4.dat','N-fraction (EPOS LHC)',
        columns={'energy':0, 'value':11, 'error_low':12, 'sys_error_low':13, 'error_high':14, 'sys_error_high':15},
        is_fraction=True),
    "Fe": parse_txt('auger/xmax-eps-4.dat','Fe-fraction (EPOS LHC)',
        columns={'energy':0, 'value':16, 'error_low':17, 'sys_error_low':18, 'error_high':19, 'sys_error_high':20},
        is_fraction=True),
}
"""


def import_xml_data():
    import glob
    from collections import defaultdict
    from string import maketrans
    trans = maketrans("- ", "__")
    spectra = defaultdict(lambda: {})
    for xml_file in glob.glob(data_dir + "/*/*.xml"):
        name = os.path.basename(xml_file)
        name = name[:-4]
        elems = []
        items = name.split("_")
        n = len(items)
        for i in range(-1, -len(items), -1):
            item = items[i]
            if item in elements.elements:
                elems.append(item)
                n = i
            else:
                break
        name = "_".join(items[:n]).translate(trans).lower()
        s = parse_xml(xml_file)
        spectra[name][" ".join(reversed(elems))] = s
    for name, val in spectra.items():
        # the following line prevents one from reloading the module. Standard behavior is to rebind the name.
        #if name in globals():
        #    raise ValueError("name %s already exists" % name)
        # simplify access to data sets with only one item
        if len(val) == 1 and val.keys()[0] == "":
            globals()[name] = val[""]
        else:
            globals()[name] = val
import_xml_data()


kascade_grande_icrc2015 = {
    "": kascade_grande_icrc2015_total,
    "p He": kascade_grande_icrc2015_light,
    "O Fe": kascade_grande_icrc2015_heavy
}

hess_2007_mix = {
    "Fe": merge_spectra(hess_2007_sibyll21["Fe"],
                        hess_2007_qgsjet01["Fe"],
                        independent=False)
}

