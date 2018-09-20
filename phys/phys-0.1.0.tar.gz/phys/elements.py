import numpy as np
import os

_table = np.loadtxt(
    os.path.join(os.path.dirname(__file__), "pdg_2017_elements.dat"),
    dtype=[("Z", int), ("A", float)],
    skiprows=1
)

_table = np.unique(_table)

elements = {}
charge2symbol = {}
for i, s in enumerate(('p','d','He','Li','Be','B',
    'C','N','O','F','Ne','Na','Mg',
    'Al','Si','P','S','Cl','Ar','K',
    'Ca','Sc','Ti','V','Cr','Mn',
    'Fe','Co','Ni')):
    elements[s] = _table[i]
    if s != "d":
        charge2symbol[_table[i][0]] = s

del _table
