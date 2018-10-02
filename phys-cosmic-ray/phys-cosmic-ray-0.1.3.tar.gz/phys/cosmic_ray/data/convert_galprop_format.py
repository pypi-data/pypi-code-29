#!/usr/bin/env python
import numpy as np
import argparse
import os


def read_galprop(filename):

    mass_nucleon = 0.93895 # GeV/c2

    def mass_from_charge(z):
        if z == -1: return -1
        if z == 1: return 1
        if z == 18: return 40
        if z == 26: return 56
        return 2 * z

    en = []
    en_unit = None
    fl_unit = None
    fl = []
    fd = []
    fu = []
    mass = []
    skip = True
    for iline, line in enumerate(open(filename)):
        if not line: continue
        if line.startswith("#"): continue
        if line.startswith("="):
            skip = False
            continue
        if skip: continue
        parts = [x.strip() for x in line.split() if not x.isspace()]
        if en_unit is None:
            en_unit = parts[2]
            fl_unit = parts[3]
        assert en_unit == parts[2], parts[2]
        assert fl_unit == parts[3], parts[3]
        assert "flux" == parts[4], parts[4]
        z, a = parts[16].split(".")
        if a == "-1":
            a = mass_from_charge(int(z))
        kinetic_energy = float(parts[5])
        energy = kinetic_energy + a * mass_nucleon

        flux = float(parts[8])
        flux_d = float(parts[9])
        flux_u = float(parts[10])
        if flux_u == 0.0:
            flux_u = flux_d

        en.append(energy)
        fl.append(flux)
        fd.append(flux_d)
        fu.append(flux_u)
        mass.append(a)

    npa = np.array
    return en_unit, fl_unit, npa(en), npa(fl), npa(fd), npa(fu), npa(mass)


## main
parser = argparse.ArgumentParser()
parser.add_argument("file", help="csv file from WebPlotDigitizer")
parser.add_argument("-o", help="output file")
parser.add_argument("--ref", default="TODO",
                    help="Reference")
parser.add_argument("--name", default=None,
                    help="Name to put in the xml")
parser.add_argument("--esys", type=float, default=0.0,
                    help="systematic uncertainty of energy scale")

args = parser.parse_args()

if args.name is None:
    args.name = os.path.splitext(os.path.basename(args.o))[0]

suffix = { 1: "p", 4: "He", 12: "C", 14: "N", 16: "O",
           20: "Ne", 24: "Mg", 28: "Si", 56: "Fe" }

ofilename = args.o
obase, oext = os.path.splitext(args.o)

energy_unit, flux_unit, en_a, fl_a, fd_a, fu_a, a = read_galprop(args.file)
for ai in np.unique(a):

    ref = args.ref
    name = args.name
    if ai != -1:
        ofilename = "{0}_{1}{2}".format(obase, suffix[ai], oext)
        name = args.name + " " + suffix[ai]

    m = a == ai
    en = en_a[m]
    fl = fl_a[m]
    fd = fd_a[m]
    fu = fu_a[m]

    table = []
    for eni, fli, fdi, fui in zip(en, fl, fd, fu):
        line = "%12.4e %12.4e %12.4e %12.4e" % (eni, fli, fdi, fui)
        table.append(line)
    table = "  \n".join(table)
    esys = ""
    if args.esys:
        esys = "<energy_systematic> %.2f </energy_systematic>" % args.esys

    open(ofilename, "w").write("""<flux>
<name> {name} </name>
<reference>
  {ref}
</reference>
<energy_unit> {energy_unit} </energy_unit>
<value_unit> {flux_unit} </value_unit>
{esys}
<columns> energy value error_minus error_plus </columns>
<table>
{table}
</table>
</flux>
""".format(**locals()))
