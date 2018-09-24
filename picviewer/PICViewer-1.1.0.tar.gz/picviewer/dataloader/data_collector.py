import numpy as np

from picviewer.dataloader.load_warpx import LoadWarpx
from picviewer.dataloader.load_openpmd import LoadOpenpmd
from picviewer.dataloader.load_tristanmp import LoadTristanmp

class DataCollector():
    """
        load field and paritcle data class

    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow
        
        if self.main.dataformat == 'WarpX':
            self.loaddata = LoadWarpx()
        if self.main.dataformat == 'openPMD':
            self.loaddata = LoadOpenpmd()
        if self.main.dataformat == 'tristanMP':
            self.loaddata = LoadTristanmp()

        
    def loaddatasync(self):

        for l in np.arange(self.main.nrow*self.main.ncolumn):

            # i.e., self.field_select_panel = [True, True, False, ....]
            # When a panel selects field data, it is True
            # but selects particle data, False
            if self.main.field_select_panel[l]:
                field = self.main.field_panel[l]
                self.loadfield(field)
            else:
                species = self.main.species_panel[l]
                phase= self.main.phase_panel[l]

                self.loadparticle(species, phase[0], phase[1])

    
    def loadfield(self, field=None):
        """
        load field data for a selected window panel

        """
        if field is None: 
            field = self.main.field_panel[self.main.panelselect-1]
   
        if (field,self.main.tstep) in self.main.fdata_container.keys():
        # if the field data already exist in fdata_container, skip loading
            pass
        else:
            self.main.fdata_container[(field,self.main.tstep)] = \
                self.loaddata.loadfield(
                    self.main.filepath,
                    self.main.dim,
                    self.main.iterations[self.main.tstep-1],
                    field)

    def loadparticle(self, species=None, phase1=None, phase2=None):
        """
        load particle data for a selected window panel

        """
        if species == None: 
            species = self.main.species_panel[self.main.panelselect-1]

        # phase_panel is a list with a pair, i.e., [['px','x'], ['x','z']], ...
        if phase1 == None or phase2 == None: 
            phase = self.main.phase_panel[self.main.panelselect-1]
        else:
            phase = [phase1, phase2]

        position_variables = ['x','y','z']
        momentum_variables = ['px','py','pz']
        other_variables = ['ene', 'ang']
        # load weight variable
        if (species,'w', self.main.tstep) in self.main.pdata_container.keys():
            pass # if the particle variable is in data container, skip loading
        else:
            self.main.pdata_container[(species,'w',self.main.tstep)] = \
                self.loaddata.loadparticle(
                    self.main.filepath,
                    self.main.dim,
                    self.main.iterations[self.main.tstep-1], 
                    species,
                    'w')

        # loop over the phase tuple elements, i.e., phase = (x,z), (px,z), ...
        for loc in range(2):
            variable = phase[loc]
            # load momentum variables
            if variable in momentum_variables:
                # if the particle variable is in data container, skip loading 
                if (species,variable, self.main.tstep) in self.main.pdata_container.keys():
                    pass
                else:
                    self.main.pdata_container[(species,variable,self.main.tstep)] = \
                        self.loaddata.loadparticle(
                            self.main.filepath,
                            self.main.dim,
                            self.main.iterations[self.main.tstep-1], 
                            species,
                            variable)

            # load position variables
            if variable in position_variables:
                if self.main.dim == 2:
                    if (species,variable, self.main.tstep) in self.main.pdata_container.keys():
                        pass
                    else:
                        self.main.pdata_container[(species,variable,self.main.tstep)] = \
                            self.loaddata.loadparticle(
                            self.main.filepath,
                            self.main.dim,
                            self.main.iterations[self.main.tstep-1], 
                            species,
                            variable)

            # If the variable is energy, angles, then load 'px', 'py', and 'pz'. 
            elif variable in other_variables:
                for var in momentum_variables:
                    if (species,var,self.main.tstep) in self.main.pdata_container.keys():
                        pass
                    else:
                        self.main.pdata_container[(species,var,self.main.tstep)] = \
                            self.loaddata.loadparticle(
                            self.main.filepath,
                            self.main.dim,
                            self.main.iterations[self.main.tstep-1], 
                            species,
                            var)

        # In 3D, load all the position data, x, y, and z for slicing
        if self.main.dim == 3:
            for variable in position_variables:
                if (species,variable, self.main.tstep) in self.main.pdata_container.keys():
                    pass
                else:
                    self.main.pdata_container[(species,variable,self.main.tstep)] = \
                        self.loaddata.loadparticle(
                            self.main.filepath,
                            self.main.dim,
                            self.main.iterations[self.main.tstep-1], 
                            species,
                            variable)

    
