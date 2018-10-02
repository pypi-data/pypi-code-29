#!/usr/bin/env python
import numpy as np
from collections import defaultdict
import argparse
import os

def load_errorbar_plot(filename,
                       logx,
                       logy,
                       xstep,
                       yrelerr):
    d = np.loadtxt(filename, delimiter=',')
    lgx = d[:, 0] if logx else np.log10(d[:, 0])
    lgx = np.round(lgx / (0.5 * xstep)) * (0.5 * xstep)
    x = 10 ** lgx
    y = 10 ** d[:, 1] if logy else d[:, 1]
    yg = defaultdict(lambda: [])
    for xi, yi in zip(x, y):
        yg[xi].append(yi)
    x = np.empty(len(yg))
    y = np.empty(len(yg))
    ye = np.empty((2, len(yg)))
    for i, xi in enumerate(sorted(yg)):
        x[i] = xi
        ygi = yg[xi]
        ygi.sort()
        if len(ygi) == 1:
            y[i] = ygi[0]
            ye[0, i] = ye[1, i] = y[i] * yrelerr
        else:
            y[i] = ygi[1]
            ye[0, i] = ygi[1] - ygi[0]
            ye[1, i] = ygi[2] - ygi[1]
    return x, y, ye

## main
parser = argparse.ArgumentParser()
parser.add_argument("file", help="csv file from WebPlotDigitizer")
parser.add_argument("-o", help="output file")
parser.add_argument("--logx", action="store_true", help="x is log10(E), else x is E")
parser.add_argument("--logy", action="store_true", help="y is log10(value), else y is value")
parser.add_argument("--yrelerr", type=float, default=np.nan,
                    help="relative error to use if no error could be read off the plot")
parser.add_argument("-s", type=float, default=0.1,
                    help="energy steps in log10, defaults to 0.1")
parser.add_argument("--energy-unit", default="TODO",
                    help="energy unit")
parser.add_argument("--value-unit", default="TODO",
                    help="value unit")
parser.add_argument("-p", default=0.0, type=float,
                    help="divide y by x ** p, defaults to 0")
parser.add_argument("--ref", default="TODO",
                    help="Reference")
parser.add_argument("--name", default=None,
                    help="Name to put in the xml")
parser.add_argument("--fraction-of", default=None,
                    help="compute fraction based on this file, which is total")

args = parser.parse_args()

if args.name is None:
    name = os.path.splitext(os.path.basename(args.o))[0]
else:
    name = args.name
energy_unit = args.energy_unit
value_unit = args.value_unit
table = []
x, y, ye = load_errorbar_plot(args.file,
                              logx=args.logx,
                              logy=args.logy,
                              xstep=args.s,
                              yrelerr=args.yrelerr)
y /= x ** args.p
ye /= x ** args.p
if args.fraction_of is not None:
    x_tot, y_tot, ye_tot = load_errorbar_plot(args.fraction_of,
                                              logx=args.logx,
                                              logy=args.logy,
                                              xstep=args.s,
                                              yrelerr=args.yrelerr)
    dtot = dict(zip(x_tot, y_tot))
    for i, xi in enumerate(x):
        y[i] /= dtot[xi]
        for j in (0, 1):
            ye[j][i] /= dtot[xi]

for xi, yi, yeli, yeui in zip(x, y, ye[0], ye[1]):
    line = "%12.4e %12.4e %12.4e %12.4e" % (xi, yi, yeli, yeui)
    table.append(line)
table = "\n".join(table)
ref = args.ref

open(args.o, "w").write("""<flux>
  <name> {name} </name>
  <reference>
    {ref}
  </reference>
  <energy_unit> {energy_unit} </energy_unit>
  <value_unit> {value_unit} </value_unit>
  <columns> energy value error_minus error_plus </columns>
  <table>
{table}
  </table>
</flux>
""".format(**locals()))
