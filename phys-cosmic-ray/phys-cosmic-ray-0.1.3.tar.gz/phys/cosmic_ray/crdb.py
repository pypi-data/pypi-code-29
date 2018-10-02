import numpy as np
import os
import string
from tools import make_spectrum, lock_spectrum, merge_spectra, l2norm, data_dir
from phys import units as u, constants, elements

def _init(**modifiers):
    table = np.loadtxt(data_dir + "/usine_all_database.dat",
                       dtype=[("quantity", "S25"),
                              ("experiment", "S50"),
                              ("x_type", "S10"),
                              ("x", float),
                              ("x_min", float),
                              ("x_max", float),
                              ("value", float),
                              ("error_minus", float),
                              ("error_plus", float),
                              ("sys_error_minus", float),
                              ("sys_error_plus", float),
                              ("ads_url", "S100"),
                              ("phi", float),
                              ("solar_distance", float),
                              ("datetime", "S25"),
                              ("is_upper_limit", bool)])

    # reject upper limits and voyager results
    table =  table[(table["is_upper_limit"] == False)]

    experiments = np.unique(np.sort(table["experiment"]))

    qfilter = {x:x for x in elements.elements.keys()}
    qfilter["H"] = "p"
    qfilter["1H"] = "p"
    qfilter["2h"] = "d"

    crdb = {}
    trans = string.maketrans("()/-+&.", "_______")
    for exp in experiments:
        name = exp.translate(trans).lower().strip("_")
        modifier = modifiers.get(name, None)
        tab = table[table["experiment"] == exp]
        d = {}
        for quantity in np.unique(np.sort(tab["quantity"])):
            if quantity not in qfilter: continue
            tag = qfilter[quantity]
            z, a = elements.elements[tag]
            tabi = tab[tab["quantity"] == quantity]
            x_type = tabi["x_type"][0]
            tabi = tabi[tabi["x_type"] == x_type] # for datasets in EKN and R
            s = make_spectrum(len(tabi), name)
            if x_type == "ETOT":
                for suf in ("", "_min", "_max"):
                    s["energy" + suf] = tabi["x" + suf] * u.GeV
                dedx = 1.0
            elif x_type == "EK":
                for suf in ("", "_min", "_max"):
                    s["energy" + suf] = tabi["x" + suf] * u.GeV + a * constants.nucleon_mass
                dedx = 1.0
            elif x_type == "EKN":
                for suf in ("", "_min", "_max"):
                    s["energy" + suf] = a * (tabi["x" + suf] * u.GeV + constants.nucleon_mass)
                dedx = a
            elif x_type == "R":
                ze = z * u.eplus
                for suf in ("", "_min", "_max"):
                    s["energy" + suf] = l2norm(ze * tabi["x" + suf] * u.GV, a * constants.nucleon_mass)
                dedx = ze ** 2 * tabi["x"] * u.GV / s["energy"]
            else:
                raise ValueError("unknown x_type %s" % x_type)
            flux_unit = 1.0 / dedx / (u.GeV * u.sr * u.s * u.m2)
            for field in ("value", "error_minus", "error_plus",
                          "sys_error_minus", "sys_error_plus"):
                s[field] = np.abs(tabi[field]) * flux_unit
            if modifier is not None:
                sys_mod = modifier.get("value_systematic", None)
                if sys_mod is not None:
                    sys = sys_mod(tag, s.energy, s.value)
                    s.sys_error_minus = l2norm(s.sys_error_minus, sys)
                    s.sys_error_plus = l2norm(s.sys_error_plus, sys)
                s.energy_systematic = modifier.get("energy_systematic", 0.0)
                s.verified = modifier.get("verified", False)
            s.reference = ";".join(np.unique(tabi["ads_url"]))
            s.modulation_phi = tabi["phi"] * u.MV
            lock_spectrum(s)
            d[tag] = s
        crdb[name] = d
    return crdb

def _relative_error(r):
    return lambda prim, energy, value: r * value

def _cream_ii_error(prim, energy, value):
    s = 0.1 * np.ones_like(value)
    s[energy > 3 * u.TeV] = 0.05
    return l2norm(s, 0.15 if prim == "N" else 0.02) * value

crdb = _init(
    cream_i_2004_12_2005_01=dict(
        value_systematic=_relative_error(0.09),
        energy_systematic=0.01,
        verified=True
    ),
    cream_ii_2005_12_2006_01=dict(
        value_systematic=_cream_ii_error,
        energy_systematic=0.05,
        verified=True
    ),
    pamela_2006_07_2008_12=dict(
        verified=True
    ),
    heao3_c2_1979_10_1980_06=dict(
        value_systematic=_relative_error(0.03),
        energy_systematic=0.02,
        verified=True
    ),
    crn_spacelab2_1985_07_1985_08=dict(
        value_systematic=_relative_error(0.1),
        verified=True
    ),
)

from data import cream_iii_2017
crdb["cream_i_iii"] = {
    prim: merge_spectra(crdb["cream_i_2004_12_2005_01"][prim],
                        cream_iii_2017[prim],
                        independent=True)
    for prim in cream_iii_2017
}

globals().update(crdb)
