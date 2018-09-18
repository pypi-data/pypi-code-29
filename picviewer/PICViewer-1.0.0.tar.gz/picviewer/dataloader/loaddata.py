
import h5py
import numpy as np

try:
    import yt
    from yt.funcs import mylog
    mylog.setLevel(0)
except:
    pass

class LoadData:

    #def __init__(self):

    def loadfield(self, 
                dataformat, 
                dim, 
                iteration, 
                field):

        if dataformat == 'openPMD':
            
            fname =  './data'+str('%8.8d.h5'%(iteration))
            fi = h5py.File(fname, 'r')
            dset = fi['/data/'+str(iteration)+'/fields/'+field[0]+'/'+field[1]]
            tempdata = dset[()]
            #nx, nz = tempdata.shape

            tempdata=np.float32(tempdata)

            return tempdata


        if dataformat == 'WarpX':

            fname =  './plt'+str('%5.5d'%(iteration))
            amrlevel = 0
            ds = yt.load(fname)
            all_data_level = ds.covering_grid(level=amrlevel,
                left_edge=ds.domain_left_edge, dims=ds.domain_dimensions)
            if dim == 3:
                tempdata = all_data_level[field][()].d
            else:
                tempdata = all_data_level[field][:, :, 0].d
                
                tempdata = tempdata.T

            tempdata = np.float32(tempdata)

            return tempdata

        if dataformat == 'tristan-MP':
            
            fname = './flds.tot.'+str('%3.3d'%(iteration))
            fi = h5py.File(fname, 'r')
            if field[1] == 'x':
                dset = fi[field[0]+'y']
            elif field[1] == 'y':
                dset = fi[field[0]+'z']
            elif field[1] == 'z':
                dset = fi[field[0]+'x']
            elif field[2] == 'x':
                dset = fi[field[0:2]+'y'+field[3:]]
            elif field[2] == 'y':
                dset = fi[field[0:2]+'z'+field[3:]]
            elif field[2] == 'z':
                dset = fi[field[0:2]+'x'+field[3:]]
            else:
                dset = fi[field]
            
            tempdata = dset[()]

            tempdata=np.float32(tempdata)
            #tempdata = tempdata.T
            tempdata = tempdata[0,:,:]

            return tempdata


    def loadparticle(self,
                dataformat,
                dim,
                iteration,
                species,
                variable):

            C = 2.99792458e8 # light speed

            if dataformat == 'openPMD':

                fname =  './data'+str('%8.8d.h5'%(iteration))
                fi = h5py.File(fname, 'r')
                dset= fi['data/'+str(iteration)+'/particles']
                m = dset[species+'/mass'].attrs['value']

                if variable in ['x','y','z']:
                    tempdata = fi['data/'+str(iteration)+'/particles/' \
                        +species+'/position/'+variable][()]*1.e6

                if variable in ['px','py','pz']:

                    tempdata = fi['data/'+str(iteration)+'/particles/' \
                        +species+'/momentum/'+variable[1]][()]/(m*C)


            if dataformat == 'WarpX':

                fname =  './plt'+str('%5.5d'%(iteration))
                ds = yt.load(fname)
                ad = ds.all_data()

                if variable in ['x','y','z']:    
                    tempdata = ad[(species,'particle_position_'+variable)].to_ndarray()
                    tempdata = np.float32(tempdata)*1e6

                if variable in ['px','py','pz']:    
                    tempdata = ad[(species,'particle_momentum_'+variable[1])].to_ndarray()
                    tempdata =np.float32(tempdata)/C


            if dataformat == 'tristan-MP':

                param = h5py.File('./param.'+str('%3.3d'%(iteration)), 'r')
                c_omp = param['c_omp'][0]

                fname = './prtl.tot.'+str('%3.3d'%(iteration))
                fi = h5py.File(fname, 'r')

                if variable == 'z':
                    tempdata = fi['x'+species[0]][()]
                if variable == 'x':
                    tempdata = fi['y'+species[0]][()]
                if dim == 3:
                    if variable == 'y':
                        tempdata = fi['z'+species[0]][()]
                
                if variable == 'pz':
                    tempdata = fi['u'+species[0]][()]
                if variable == 'px':
                    tempdata = fi['v'+species[0]][()]

                if variable == 'py':
                    tempdata = fi['w'+species[0]][()]

                tempdata =np.float32(tempdata)/c_omp

            return tempdata


