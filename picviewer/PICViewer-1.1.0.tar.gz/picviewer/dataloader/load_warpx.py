import numpy as np

import yt
from yt.funcs import mylog
mylog.setLevel(0)

class LoadWarpx:

    def loadfield(self, 
                filepath,
                dim, 
                iteration, 
                field):

        fname =  filepath+'/plt'+str('%5.5d'%(iteration))
        amrlevel = 0
        ds = yt.load(fname)

        if dim == 3:
            nx, ny, nz = ds.domain_dimensions
            dxfact = int(np.ceil(1.*nx/256))
            dyfact = int(np.ceil(1.*ny/256))
            dzfact = int(np.ceil(1.*nz/512))
        else:
            nx, nz = ds.domain_dimensions
            dxfact = int(np.ceil(1.*nx/2048))
            dzfact = int(np.ceil(1.*nz/2048))

        all_data_level = ds.covering_grid(level=amrlevel,
            left_edge=ds.domain_left_edge, dims=ds.domain_dimensions)
        if dim == 3:
            tempdata = all_data_level[field][::dxfact, ::dyfact, ::dzfact].d
        else:
            tempdata = all_data_level[field][::dxfact, ::dzfact, 0].d
            
            tempdata = tempdata.T

        tempdata = np.float32(tempdata)

        return tempdata

    def loadparticle(self,
                filepath,
                dim,
                iteration,
                species,
                variable):

        C = 2.99792458e8 # light speed

        fname =  filepath+'/plt'+str('%5.5d'%(iteration))
        ds = yt.load(fname)
        ad = ds.all_data()

        numpart = ds.particle_type_counts[species]
        dpfact = int(np.ceil(1.*numpart/1e7))

        if variable in ['x','y','z']:    
            tempdata = ad[(species,'particle_position_'+variable)][::dpfact]

            tempdata = np.float32(tempdata)*1e6

        if variable in ['px','py','pz']:    
            tempdata = ad[(species,'particle_momentum_'+variable[1])][::dpfact]

            tempdata =np.float32(tempdata)/C

        if variable in ['w']:
            tempdata = ad[(species,'particle_weight')][::dpfact]

            tempdata =np.float32(tempdata)

        return tempdata
