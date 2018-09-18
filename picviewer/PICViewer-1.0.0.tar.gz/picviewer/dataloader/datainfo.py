
import h5py
import glob
import numpy as np
import re
try:
    import yt
    from yt.funcs import mylog
    mylog.setLevel(0)
except:
    pass

class DataInfo:

    def datainfo(self):
        """
        load simulation parameters

        Returns: param={} dictionary

        param_dic['iterations'] = iterations
        param_dic['file_list'] = file_list
        param_dic['dataformat'] = dataformat
        param_dic['field_list'] = field_list
        param_dic['coord_system'] = coord_system
        param_dic['dim'] = dim
        param_dic['taxis'] = taxis
        param_dic['xaxis'] = xaxis
        param_dic['yaxis'] = yaxis
        param_dic['zaxis'] = zaxis
        param_dic['species_list'] = species_list
        param_dic['phase_list1'] = phase_list1
        param_dic['phase_list2'] = phase_list2
        param_dic['phase_list3'] = phase_list3
        param_dic['mass_list'] = mass_list
        """

        # Determine the data type wheter openpmd hdf5 or WarpX AMRex plot files.
        file_path = '.'
        # warpX data file
        file_list1 = glob.glob(file_path + '/plt?????')

        # openPMD data file
        file_list2 = glob.glob(file_path + '/data????????.h5')

        # tristan-MP data file
        file_list3 = glob.glob(file_path + '/flds.tot.???')

        if len(file_list1) != 0:
            dataformat = 'WarpX'
            file_list = file_list1
        elif len(file_list2) != 0:
            dataformat = 'openPMD'
            file_list = file_list2
        elif len(file_list3) != 0:
            dataformat = 'tristan-MP'
            file_list = file_list3
            
        if dataformat == 'WarpX':
            iterations = [ int(file_name[len(file_name)-5:]) for file_name in file_list ]
            
        elif dataformat == 'openPMD':
            iterations = [ int(file_name[len(file_name)-11:len(file_name)-3]) for file_name in file_list ]
 
        elif dataformat == 'tristan-MP':
            digit = re.findall('\d+',file_list[0])
            if len(digit[0]) == 3:
                iterations = [ int(file_name[len(file_name)-3:len(file_name)]) for file_name in file_list ]
            if len(digit[0]) == 4:
                iterations = [ int(file_name[len(file_name)-4:len(file_name)]) for file_name in file_list ]

        file_list.sort()
        iterations.sort()
        tmax = len(iterations)

        ###########################
        # WarpX data format
        ###########################
        if dataformat == 'WarpX':
            
            ##############################################################
            # find field list
            ##############################################################
            field_list = []
            ds = yt.load(file_list[tmax-1])
            field_list_all = ds.field_list
            nfields_all = len(field_list_all)
            for i in np.arange(nfields_all):
                if field_list_all[i][0] == 'boxlib':
                    field_list.append(field_list_all[i][1])

            ##############################################################
            # find the coordinate system, 'Cartesian or cylindrical
            ##############################################################
            if ds.parameters['geometry.coord_sys'] == '0':
                coord_system = 'cartesian'
            else:
                coord_system = 'cylindrical'
    
            ##############################################################
            # find dimensionality
            ##############################################################
            if ds.domain_dimensions[2] > 1:
                dim = 3
            elif ds.domain_dimensions[1] == 1:
                dim = 1
            else: 
                dim = 2
            
            ##############################################################
            # get spatial axes
            ##############################################################
            if dim == 3:
                xmin=ds.domain_left_edge[0].d*1.e6
                ymin=ds.domain_left_edge[1].d*1.e6
                zmin=ds.domain_left_edge[2].d*1.e6
                xmax=ds.domain_right_edge[0].d*1.e6
                ymax=ds.domain_right_edge[1].d*1.e6
                zmax=ds.domain_right_edge[2].d*1.e6
                nx = ds.domain_dimensions[0]
                ny = ds.domain_dimensions[1]
                nz = ds.domain_dimensions[2]

                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                yaxis=1.*np.arange(ny)*(ymax-ymin)/ny+ymin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin   

            else:
                xmin=ds.domain_left_edge[0].d*1.e6
                zmin=ds.domain_left_edge[1].d*1.e6
                xmax=ds.domain_right_edge[0].d*1.e6
                zmax=ds.domain_right_edge[1].d*1.e6
                nx = ds.domain_dimensions[0]
                nz = ds.domain_dimensions[1]

                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                yaxis=np.array([0])       

            ##############################################################
            # find species list
            ##############################################################
            #ds = yt.load(file_list[0])
            ds.index
            species_list_all=ds.particle_types
            mass_list = []
            species_list = []
            for species in species_list_all:
                if species[0] != 'a':
                    try:
                        q = ds.parameters[species+'.charge']
                        m = ds.parameters[species+'.mass']
                        mass_list.append(m)
                    except KeyError:
                        pass
                    species_list.append(species)
                    
                        
            ##############################################################
            # pahse list
            ##############################################################
            if dim == 2:
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                phase_list1.append(('x','eng'))
                #phase_list1.append(('ene','ang'))

            else:
            
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                #phase_list1.append(('x','ene'))
                #phase_list1.append(('ene','ang'))

                phase_list2 = []
                phase_list2.append(('y','x'))
                phase_list2.append(('px','x'))
                phase_list2.append(('py','x'))
                phase_list2.append(('pz','x'))
                #phase_list2.append(('ene','x'))
                phase_list2.append(('y','px'))
                phase_list2.append(('y','py'))
                phase_list2.append(('y','pz'))
                #phase_list2.append(('y','ene'))
                #phase_list2.append(('ene','ang'))

                phase_list3 = []
                phase_list3.append(('y','z'))
                phase_list3.append(('px','z'))
                phase_list3.append(('py','z'))
                phase_list3.append(('pz','z'))
                #phase_list3.append(('ene','z'))
                phase_list3.append(('y','px'))
                phase_list3.append(('y','py'))
                phase_list3.append(('y','pz'))
                #phase_list3.append(('y','ene'))
                #phase_list3.append(('ene','ang'))

            ##############################################################
            # get times in fs unit
            ##############################################################
            taxis=np.zeros(len(file_list))
            s=0
            for files in file_list:
                ds = yt.load(files)
                time=ds.current_time.d*1.e15
                taxis[s]=time
                s+=1


        ###########################
        # OpenPMD data format
        ###########################
        if dataformat == 'openPMD':

            ##############################################################
            # find field list
            ##############################################################
            field_list = []
            fi = h5py.File(file_list[tmax-1],'r')
            item = fi['data/'+str(iterations[tmax-1])+'/fields']
            fields_group = item.items()
            nfields = len(fields_group)
                
            item = fi['data/'+str(iterations[tmax-1])+'/fields/E']
            coord_group = item.items()
            ncoord = len(coord_group)
            coord_list = []
            for i in np.arange(ncoord):
                coord_list.append(coord_group[i][0])

            for i in np.arange(nfields):
                for j in np.arange(ncoord):
                    if fields_group[i][0] != 'rho':
                        field_list.append(fields_group[i][0]+coord_list[j])
                    else:
                        field_list.append(fields_group[i][0])
                        break

            ##############################################################
            # find the coordinate system, 'Cartesian or cylindrical
            ##############################################################
            item = fi['data/'+str(iterations[tmax-1])+'/fields/'+field_list[0][0]].attrs['geometry']
            if item == 'cartesian':
                coord_system = 'cartesian'
            else:
                coord_system = 'cylindrical'

            ##############################################################
            # find dimensionality
            ##############################################################
            item = fi['data/'+str(iterations[tmax-1])+'/fields/'+field_list[0][0]].attrs['axisLabels']
            dim = len(item)

            ##############################################################
            # get spatial axes
            ##############################################################
            if dim ==3:
                dset=fi['/data/'+str(iterations[tmax-1])+'/fields/E']
                dx,dy,dz=dset.attrs["gridSpacing"]
                xmin,ymin,zmin = dset.attrs['gridGlobalOffset']
                dset=fi['/data/'+str(iterations[tmax-1])+'/fields/E/x']
                nx,ny,nz = dset.shape
                xmax=nx*dx+xmin
                ymax=ny*dy+ymin
                zmax=nz*dz+zmin
                
                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                yaxis=1.*np.arange(ny)*(ymax-ymin)/ny+ymin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                xaxis*=1.e6
                yaxis*=1.e6
                zaxis*=1.e6

            else:
                dset=fi['/data/'+str(iterations[tmax-1])+'/fields/E']
                dx,dz=dset.attrs["gridSpacing"]
                xmin,zmin = dset.attrs['gridGlobalOffset']
                dset=fi['/data/'+str(iterations[tmax-1])+'/fields/E/x']
                nx,nz = dset.shape
                xmax=nx*dx+xmin
                zmax=nz*dz+zmin
                
                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                xaxis*=1.e6
                zaxis*=1.e6
                yaxis=np.array([0])    

            ##############################################################
            # find species list
            ##############################################################
            dset= fi['data/'+str(iterations[tmax-1])+'/particles']
            species_list = dset.keys()
            mass_list = []
            for species in species_list:
                q = dset[species+'/charge'].attrs['value']
                m = dset[species+'/mass'].attrs['value']
                mass_list.append(m)

            ##############################################################
            # pahse list
            ##############################################################
            if dim == 2:
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                #phase_list1.append(('x','eng'))
                #phase_list1.append(('ene','ang'))

            else:
            
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                #phase_list1.append(('x','ene'))
                #phase_list1.append(('ene','ang'))

                phase_list2 = []
                phase_list2.append(('y','x'))
                phase_list2.append(('px','x'))
                phase_list2.append(('py','x'))
                phase_list2.append(('pz','x'))
                #phase_list2.append(('ene','x'))
                phase_list2.append(('y','px'))
                phase_list2.append(('y','py'))
                phase_list2.append(('y','pz'))
                phase_list2.append(('y','ene'))
                #phase_list2.append(('ene','ang'))

                phase_list3 = []
                phase_list3.append(('y','z'))
                phase_list3.append(('px','z'))
                phase_list3.append(('py','z'))
                phase_list3.append(('pz','z'))
                #phase_list3.append(('ene','z'))
                phase_list3.append(('y','px'))
                phase_list3.append(('y','py'))
                phase_list3.append(('y','pz'))
                #phase_list3.append(('y','ene'))
                #phase_list3.append(('ene','ang'))


            ##############################################################
            # get times in fs unit
            ##############################################################
            taxis=np.zeros(len(file_list))
            s=0
            for files in file_list:
                fi = h5py.File(files,'r')
                dset=fi['/data/'+str(iterations[s])]
                time=dset.attrs['time']*1.e15
                taxis[s]=time
                s+=1
                
        ###########################
        # Tristan-MP data format
        ###########################
        if dataformat == 'tristan-MP':

            ##############################################################
            # find field list
            ##############################################################
            field_list = []
            fi = h5py.File(file_list[tmax-1],'r')
            field_list_all = fi.items()
            field_list = []
            for field in field_list_all:
                field_list.append(field[0])
                

            ##############################################################
            # find the coordinate system, 'Cartesian or cylindrical
            ##############################################################
            coord_system = 'cartesian'

            ##############################################################
            # find dimensionality
            ##############################################################
            if 1 in fi[field_list[0]].shape:
                dim = 2
                dummy, ny, nx = fi[field_list[0]].shape
            else:
                dim = 3
                nz, ny, nx = fi[field_list[0]].shape

            ##############################################################
            # get spatial axes
            ##############################################################
            

            param = h5py.File('./param.'+str('%3.3d'%(iterations[tmax-1])), 'r')
            c = param['c'][0]
            c_omp = param['c_omp'][0]
            delgam = param['delgam'][0]
            istep = param['istep'][0]
            interval = param['interval'][0]
            dx = 1./c_omp
            dy = dx
            if dim == 3: dz = dy
            dt = c/c_omp

            xmin = 0; xmax = nx*istep*dx
            ymin = 0; ymax = ny*istep*dy
            if dim == 3 :zmin = 0; zmax = nz*istep*dz
        
            xaxis=1.*np.arange(nx)*(xmax-xmin)/(nx-1)+xmin
            yaxis=1.*np.arange(ny)*(ymax-ymin)/(ny-1)+ymin
            if dim == 3: zaxis=1.*np.arange(nz)*(zmax-zmin)/(nz-1)+zmin


            ##############################################################
            # find species list
            ##############################################################
            species_list = []
            species_list.append('electron')
            species_list.append('ion')
            mass_list = []
            mass_list.append('me')
            mass_list.append('mi')
            
            ##############################################################
            # pahse list
            ##############################################################
            if dim == 2:
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                #phase_list1.append(('x','eng'))
                #phase_list1.append(('ene','ang'))

            else:
            
                phase_list1 = []
                phase_list1.append(('x','z'))
                phase_list1.append(('px','z'))
                phase_list1.append(('py','z'))
                phase_list1.append(('pz','z'))
                #phase_list1.append(('ene','z'))
                phase_list1.append(('x','px'))
                phase_list1.append(('x','py'))
                phase_list1.append(('x','pz'))
                #phase_list1.append(('x','ene'))
                #phase_list1.append(('ene','ang'))

                phase_list2 = []
                phase_list2.append(('y','x'))
                phase_list2.append(('px','x'))
                phase_list2.append(('py','x'))
                phase_list2.append(('pz','x'))
                #phase_list2.append(('ene','x'))
                phase_list2.append(('y','px'))
                phase_list2.append(('y','py'))
                phase_list2.append(('y','pz'))
                phase_list2.append(('y','ene'))
                #phase_list2.append(('ene','ang'))

                phase_list3 = []
                phase_list3.append(('y','z'))
                phase_list3.append(('px','z'))
                phase_list3.append(('py','z'))
                phase_list3.append(('pz','z'))
                #phase_list3.append(('ene','z'))
                phase_list3.append(('y','px'))
                phase_list3.append(('y','py'))
                phase_list3.append(('y','pz'))
                #phase_list3.append(('y','ene'))
                #phase_list3.append(('ene','ang'))


            ##############################################################
            # get times in fs unit
            ##############################################################
            taxis=np.zeros(len(file_list))
            s=0
            for iteration in iterations:
                fname = 'param.'+str('%3.3d'%(iteration))
                fi = h5py.File(fname,'r')
                time=fi['time'][0]
                taxis[s]=time
                s+=1

            xaxis0 = xaxis
            if dim == 3: zaxis0 = zaxis
            yaxis0 = yaxis

            zaxis = xaxis0
            xaxis = yaxis0
            if dim == 3: yaxis = zaxis 

        param_dic = {}

        param_dic['iterations'] = iterations
        param_dic['dataformat'] = dataformat
        param_dic['field_list'] = field_list
        param_dic['coord_system'] = coord_system
        param_dic['dim'] = dim
        param_dic['taxis'] = taxis
        param_dic['xaxis'] = xaxis
        param_dic['yaxis'] = yaxis
        param_dic['zaxis'] = zaxis
        param_dic['species_list'] = species_list
        param_dic['phase_list1'] = phase_list1
        if dim == 3:
            param_dic['phase_list2'] = phase_list2
            param_dic['phase_list3'] = phase_list3
        param_dic['mass_list'] = mass_list

        return param_dic


    def update_domain_axes(self, dataformat, dim, iteration):

        if dataformat == 'WarpX':

            fname =  './plt'+str('%5.5d'%(iteration))
            ds = yt.load(fname)

            if dim == 3:
                xmin=ds.domain_left_edge[0].d*1.e6
                ymin=ds.domain_left_edge[1].d*1.e6
                zmin=ds.domain_left_edge[2].d*1.e6
                xmax=ds.domain_right_edge[0].d*1.e6
                ymax=ds.domain_right_edge[1].d*1.e6
                zmax=ds.domain_right_edge[2].d*1.e6
                nx = ds.domain_dimensions[0]
                ny = ds.domain_dimensions[1]
                nz = ds.domain_dimensions[2]

                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                yaxis=1.*np.arange(ny)*(ymax-ymin)/ny+ymin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin   

            else:
                xmin=ds.domain_left_edge[0].d*1.e6
                zmin=ds.domain_left_edge[1].d*1.e6
                xmax=ds.domain_right_edge[0].d*1.e6
                zmax=ds.domain_right_edge[1].d*1.e6
                nx = ds.domain_dimensions[0]
                nz = ds.domain_dimensions[1]

                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                yaxis=np.array([0])     

        if dataformat == 'openPMD':

            fname =  './data'+str('%8.8d.h5'%(iteration))
            fi = h5py.File(fname,'r')

            if dim ==3:
                dset=fi['/data/'+str(iteration)+'/fields/E']
                dx,dy,dz=dset.attrs["gridSpacing"]
                xmin,ymin,zmin = dset.attrs['gridGlobalOffset']
                dset=fi['/data/'+str(iteration)+'/fields/E/x']
                nx,ny,nz = dset.shape
                xmax=nx*dx+xmin
                ymax=ny*dy+ymin
                zmax=nz*dz+zmin
                
                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                yaxis=1.*np.arange(ny)*(ymax-ymin)/ny+ymin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                xaxis*=1.e6
                yaxis*=1.e6
                zaxis*=1.e6

            else:
                dset=fi['/data/'+str(iteration)+'/fields/E']
                dx,dz=dset.attrs["gridSpacing"]
                xmin,zmin = dset.attrs['gridGlobalOffset']
                dset=fi['/data/'+str(iteration)+'/fields/E/x']
                nx,nz = dset.shape
                xmax=nx*dx+xmin
                zmax=nz*dz+zmin
                
                xaxis=1.*np.arange(nx)*(xmax-xmin)/nx+xmin
                zaxis=1.*np.arange(nz)*(zmax-zmin)/nz+zmin
                xaxis*=1.e6
                zaxis*=1.e6
                yaxis=np.array([0])    

        if dataformat == 'tristan-MP':

            fname = './flds.tot.'+str('%3.3d'%(iteration))
            fi = h5py.File(fname,'r')
            if 1 in fi['ex'].shape:
                dim = 2
                dummy, ny, nx = fi['ex'].shape
            else:
                dim = 3
                nz, ny, nx = fi['ex'].shape

            fname = './param.'+str('%3.3d'%(iteration))
            param = h5py.File(fname,'r')

            c = param['c'][0]
            c_omp = param['c_omp'][0]
            delgam = param['delgam'][0]
            istep = param['istep'][0]
            interval = param['interval'][0]
            dx = 1./c_omp
            dy = dx
            if dim == 3: dz = dy
            dt = c/c_omp
            
            xmin = 0; xmax = nx*istep*dx
            ymin = 0; ymax = ny*istep*dy
            if dim == 3 :zmin = 0; zmax = nz*istep*dz
        
            xaxis=1.*np.arange(nx)*(xmax-xmin)/(nx-1)+xmin
            yaxis=1.*np.arange(ny)*(ymax-ymin)/(ny-1)+ymin
            if dim == 3: zaxis=1.*np.arange(nz)*(zmax-zmin)/(nz-1)+zmin

            xaxis0 = xaxis
            if dim == 3: zaxis0 = zaxis
            yaxis0 = yaxis

            zaxis = xaxis0
            xaxis = yaxis0
            if dim == 3: yaxis = zaxis0


        return xaxis, yaxis, zaxis






