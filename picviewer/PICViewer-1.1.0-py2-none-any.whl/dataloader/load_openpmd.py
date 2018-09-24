import h5py
import numpy as np

class LoadOpenpmd:

    def loadfield(self, 
                filepath,
                dim, 
                iteration, 
                field):

        fname =  filepath+'/data'+str('%8.8d.h5'%(iteration))
        fi = h5py.File(fname, 'r')
        dset = fi['/data/'+str(iteration)+'/fields/'+field[0]+'/'+field[1]]

        if dim == 3:
            nx, ny, nz = dset.shape
            dxfact = int(np.ceil(1.*nx/256))
            dyfact = int(np.ceil(1.*ny/256))
            dzfact = int(np.ceil(1.*nz/512))

            tempdata = dset[::dxfact,::dyfact,::dzfact]

        else:
            nx, nz = dset.shape
            dxfact = int(np.ceil(1.*nx/2048))
            dzfact = int(np.ceil(1.*nz/2048))

            tempdata = dset[::dxfact,::dzfact]
        
        #nx, nz = tempdata.shape

        tempdata=np.float32(tempdata)

        return tempdata


    def loadparticle(self,
                filepath,
                dim,
                iteration,
                species,
                variable):

        C = 2.99792458e8 # light speed

        fname =  filepath+'/data'+str('%8.8d.h5'%(iteration))
        fi = h5py.File(fname, 'r')
        dset= fi['data/'+str(iteration)+'/particles']
        m = dset[species+'/mass'].attrs['value']

        dset = fi['data/'+str(iteration)+'/particles/' \
                +species+'/weighting']
        numpart = dset.shape[0]
        dpfact = int(np.ceil(1.*numpart/1e7))

        if variable in ['x','y','z']:
            tempdata = fi['data/'+str(iteration)+'/particles/' \
                +species+'/position/'+variable][::dpfact]

            tempdata =np.float32(tempdata)*1.e6

        if variable in ['px','py','pz']:

            tempdata = fi['data/'+str(iteration)+'/particles/' \
                +species+'/momentum/'+variable[1]][::dpfact]

            tempdata =np.float32(tempdata)/(m*C)

        if variable in ['w']:
            tempdata = fi['data/'+str(iteration)+'/particles/' \
                +species+'/weighting'][::dpfact]

            tempdata =np.float32(tempdata)

    
        return tempdata



