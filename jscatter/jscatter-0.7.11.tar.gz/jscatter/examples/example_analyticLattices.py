"""
**A hexagonal lattice of cylinders with disorder**

We observe the suppression of higher order peaks with increasing disorder
"""

import jscatter as js
import numpy as np
q = np.r_[0.001:1:1500j]
unitcelllength = 50
N = 5
rms=1
domainsize=unitcelllength*N
hexgrid = js.sf.hexLattice(unitcelllength, N)
p = js.grace()
p.multi(2,1)
cyl=js.formel.pDA(js.ff.cylinder,sig=0.01,parname='radius', q=q, L=50, radius=15, SLD=1e-4)
cyl.Y= js.formel.smooth(cyl, 20)
for i,rms in enumerate([1,3,10,30],2):
    hex= js.sf.latticeStructureFactor(q, lattice=hexgrid, rmsd=rms, domainsize=domainsize)
    p[1].plot(hex, li=[1, 2, i], sy=0)
    p[0].plot(hex.X,hex.Y*cyl.Y, li=[1, 3, i], sy=0 , le='hex cylinders rms= '+str(rms))
p[0].plot(cyl, li=[3, 2, 1], sy=0, le='cylinder formfactor')
p[1].yaxis(scale='n', label='I(Q)',max=10,min=0)
p[0].yaxis(scale='l', label='I(Q)')#,max=10000,min=0.01)
p[0].xaxis(scale='n', label='',min=0)
p[1].xaxis(scale='n', label='Q / A\S-1',min=0)
p[0].legend(x=0.6, y=60, charsize=0.8)
p[0].title('hex lattice of cylinders')
p[0].subtitle('increasing disorder rmsd')


"""
**A membrane stack **

"""


import jscatter as js
import numpy as np
q = np.r_[0.1:7:500j]
unitcelllength = 60
N = 15
rms=1
domainsize=unitcelllength*N
# define grid (size is not used)
lamgrid = js.sf.lamLattice(unitcelllength,1)
p = js.grace()
p.multi(2,1)
# single layer membrane
membrane=js.ff.multilayer(q,6,1)
for i,rms in enumerate([1,2,4,6],2):
    sf= js.sf.latticeStructureFactor(q, lattice=lamgrid, rmsd=rms, domainsize=domainsize)
    p[1].plot(sf, li=[1, 2, i], sy=0)
    p[0].plot(sf.X,sf.Y*membrane.Y+0.008, li=[1, 3, i], sy=0 , le='stacked membrane rms= '+str(rms))
p[0].plot(membrane.X,membrane.Y+0.008, li=[3, 2, 1], sy=0, le='membrane formfactor')
p[1].yaxis(scale='n', label='I(Q)',max=10,min=0)
p[0].yaxis(scale='l', label='I(Q)')#,max=10000,min=0.01)
p[0].xaxis(scale='l', label='',min=0)
p[1].xaxis(scale='l', label='Q / A\S-1',min=0)
p[0].legend(x=2, y=1, charsize=0.8)
p[0].title('hex lattice of cylinders')
p[0].subtitle('increasing disorder rmsd')







