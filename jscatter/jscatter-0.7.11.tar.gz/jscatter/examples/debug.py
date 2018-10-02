# -*- coding: utf-8 -*-
#  this file is intended to used in the debugger
# write a script that calls your function to debug it

import jscatter as js
import numpy as np
import sys
# some arrays
w=np.r_[-100:100]
q=np.r_[0.001:5:0.01]
x=np.r_[1:10]

p=js.grace()
p.plot(js.ff.cuboid(q,60,4,6))
p.plot(js.ff.cuboid(q,6,4,60))
p.plot(js.ff.cuboid(q,60,6,4))

p.yaxis(scale='l')
p.xaxis(scale='l')

