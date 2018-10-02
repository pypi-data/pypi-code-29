import os
import numpy as np
from phys import units, constants


data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


def correct_solar_modulation(energy, phi, z, a):
    mass = a * constants.nucleon_mass
    energy_is = energy + z * units.eplus * phi
    factor = (energy_is ** 2 - mass ** 2) / (energy ** 2 - mass ** 2)
    return energy_is, factor


def l2norm(*args):
    return np.linalg.norm(args, axis=0)


def make_spectrum(n, name=None):
    s = np.recarray((n,),
                       dtype=np.dtype([('energy',float),
                                       ('energy_min',float),
                                       ('energy_max',float),
                                       ('value', float),
                                       ('error_minus', float),
                                       ('error_plus', float),
                                       ('sys_error_minus', float),
                                       ('sys_error_plus', float)]))
    s.fill(0.0)

    s.name = name
    s.reference = None
    s.verified = False
    s.interaction_model = None
    s.energy_systematic = 0.0
    s.modulation_phi = None
    s.is_fraction = False

    return s

def energy2rigidity(spectrum, charge=None, mass=None):
    if mass is None and not hasattr(a, 'mass'):
        raise Exception('to transform energy to rigidity and viceversa you need to specify the mass')
    if charge is None and not hasattr(a, 'charge'):
        raise Exception('to transform energy to rigidity and viceversa you need to specify the charge')
    if mass is None:
        mass = spectrum.mass
    if charge is None:
        charge = spectrum.charge
    energy = spectrum['energy']
    rigidity = numpy.sqrt(energy**2 - mass**2)/charge
    dEdR = (rigidity*charge**2)/energy
    res = copy.deepcopy(spectrum)
    res['energy'] = rigidity
    res['energy_min'] = numpy.sqrt(res['energy_min']**2 - mass**2)/charge
    res['energy_max'] = numpy.sqrt(res['energy_max']**2 - mass**2)/charge
    res['value'] *= dEdR
    res['error_minus'] *= dEdR
    res['error_plus'] *= dEdR
    res['sys_error_minus'] *= dEdR
    res['sys_error_plus'] *= dEdR
    return res

def rigidity2energy(spectrum, charge=None, mass=None):
    if mass is None and not hasattr(a, 'mass'):
        raise Exception('to transform energy to rigidity and viceversa you need to specify the mass')
    if charge is None and not hasattr(a, 'charge'):
        raise Exception('to transform energy to rigidity and viceversa you need to specify the charge')
    if mass is None:
        mass = spectrum.mass
    if charge is None:
        charge = spectrum.charge
    rigidity = spectrum['energy']
    energy = numpy.sqrt((rigidity*charge)**2 + mass**2)
    dRdE = energy/(rigidity*charge**2)
    res = copy.deepcopy(spectrum)
    res['energy'] = energy
    res['energy_min'] = numpy.sqrt((res['energy_min']*charge)**2 + mass**2)
    res['energy_max'] = numpy.sqrt((res['energy_max']*charge)**2 + mass**2)
    res['value'] *= dRdE
    res['error_minus'] *= dRdE
    res['error_plus'] *= dRdE
    res['sys_error_minus'] *= dRdE
    res['sys_error_plus'] *= dRdE
    return res

def lock_spectrum(s):
    def block_setattr(self, name, value):
        raise AttributeError("u cant touch this")
    s.flags['WRITEABLE'] = False
    s.__setattr__ = block_setattr


def merge_spectra(*spectra, **kwargs):
    independent = kwargs.get("independent", False)
    tol = kwargs.get("tolerance", 0.05)
    pts = []
    for s in spectra:
        for si in s:
            pts.append((np.log10(si.energy), si))
    pts.sort()
    pts2 = []
    i = 0
    while i < len(pts):
        xi, si = pts[i]
        merge = si
        i += 1
        while i < len(pts):
            xj, sj = pts[i]
            if xj - xi < tol:
                merge = np.append(merge, sj)
                i += 1
            else:
                break
        so = si.copy()
        nmerge = merge.shape[0] if merge.shape else 1
        if nmerge > 1:
            for field in ("energy", "energy_min", "energy_max"):
                so[field] = np.prod(merge[field]) ** (1.0 / nmerge)
            if independent:
                w = 1.0 / (0.5 * (merge["error_minus"]**2 + merge["error_plus"]**2))
                wnorm = np.sum(w)
                w = w / wnorm
            else:
                w = 1.0 / nmerge
            so["value"] = np.sum(w * merge["value"])
            for isuf, suf in enumerate(("_minus", "_plus")):
                if independent:
                    so["error"+suf] = wnorm ** -0.5
                    so["sys_error"+suf] = l2norm(
                        (np.min, np.max)[isuf](merge["value"] - so["value"]),
                        np.linalg.norm(w * merge["sys_error"+suf]))
                else:
                    so["error"+suf] = np.sum(w * merge["error"+suf])
                    so["sys_error"+suf] = l2norm(
                        (np.min, np.max)[isuf](merge["value"] - so["value"]),
                        np.sum(w * merge["sys_error"+suf]))
        pts2.append(so)
    s = make_spectrum(len(pts2))
    for i, si in enumerate(pts2):
        s[i] = si
    s.name = "; ".join(np.unique([si.name for si in spectra]))
    s.reference = "; ".join(np.unique([si.reference for si in spectra]))
    s.energy_systematic = np.max([si.energy_systematic for si in spectra])
    s.verified = np.all([si.verified for si in spectra])
    lock_spectrum(s)
    return s


def eval_string(p):
    return eval(p, units.__dict__)


def dict_join(*args):
    result = args[0]
    for a in args[1:]:
        result.update(a)
    return result
