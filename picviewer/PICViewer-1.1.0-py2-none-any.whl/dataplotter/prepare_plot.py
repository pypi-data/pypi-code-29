import numpy as np
from picviewer.dataplotter.makeplot import MakePlot

from picviewer.dataplotter.cic_histogram import particle_energy

class PreparePlot():
    """
        Plot Data class
        
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow

        self.makeplot = MakePlot()
        
    def plotsync(self):


        # Find which panels have field selection.
        # i.e., index = [0,1,3,5,..] --> panels 0, 1, 3, 5 .. have field plots.
        index = [i for i, yesfield in enumerate(self.main.field_select_panel) if yesfield]
        fields = [self.main.field_panel[i] for i in index]
        # i.e., field_keyworsd = [('Bx', 10), ('Ez', 10), ....]
        field_keywords =[(k,self.main.tstep) for k in fields]

        # Find which panels have particle selection.
        index = [i for i, yesfield in enumerate(self.main.field_select_panel) if not yesfield]
        species = [self.main.species_panel[i] for i in index]
        phase = [self.main.phase_panel[i] for i in index]
        particle_keywords0 =[(species[i], phase[i][0], self.main.tstep) for i in range(len(species))]
        particle_keywords1 =[(species[i], phase[i][1], self.main.tstep) for i in range(len(species))]
        particle_keywords2 =[(species[i], 'w', self.main.tstep) for i in range(len(species))]
        # i.e., particle_keywords = [('elec', 'px', 10), ('elec', 'x', 10), .... ]
        particle_keywords = particle_keywords0 + particle_keywords1 + particle_keywords2
        # tip : ---> keywords may be overwrapped in field_keywords or particle_keywords.
        # but the keywrods in the data dictionaries are not overwarpped.

        for keywords in particle_keywords:
            if keywords[1] == 'ene':
                if (keywords[0],'ene', keywords[2]) in self.pdata_container.keys():
                    pass
                else:
                    self.pdata_container[(keywords[0],'ene', keywords[2])] = particle_energy(
                            self.pdata_container[(keywords[0],'px',keywords[2])],
                            self.pdata_container[(keywords[0],'py',keywords[2])],
                            self.pdata_container[(keywords[0],'pz',keywords[2])])


        if self.main.dim == 2:
            # self.axes: return value from each subpanel axis
            # self.cbars: return value from each subpanel colorbar
            self.main.axes, self.main.cbars = self.makeplot.makeplotsync2D(
                    self.main.figure,
                    {k:self.main.fdata_container[k] for k in field_keywords},
                    {k:self.main.pdata_container[k] for k in particle_keywords},
                    self.main.nrow, 
                    self.main.ncolumn,
                    self.main.field_select_panel,
                    self.main.field_panel, 
                    self.main.species_panel,
                    self.main.phase_panel,
                    self.main.tstep,
                    self.main.time,
                    self.main.xaxis,
                    self.main.zaxis,
                    self.main.xminloc_panel,
                    self.main.xmaxloc_panel,
                    self.main.zminloc_panel,
                    self.main.zmaxloc_panel,
                    self.main.aspect_panel)
        else:
            loc_container = self.getLocalparticleLoc()
            self.main.axes, self.main.cbars = self.makeplot.makeplotsync3D(
                    self.main.figure,
                    {k:self.main.fdata_container[k] for k in field_keywords},
                    {k:self.main.pdata_container[k] for k in particle_keywords},
                    loc_container,
                    self.main.nrow, 
                    self.main.ncolumn,
                    self.main.field_select_panel,
                    self.main.field_panel,
                    self.main.species_panel,
                    self.main.phase_panel,
                    self.main.tstep,
                    self.main.time,
                    self.main.sliceplane_panel,
                    self.main.slicevalue_panel,
                    self.main.xaxis,
                    self.main.yaxis,
                    self.main.zaxis,
                    self.main.xminloc_panel,
                    self.main.xmaxloc_panel,
                    self.main.yminloc_panel,
                    self.main.ymaxloc_panel,
                    self.main.zminloc_panel,
                    self.main.zmaxloc_panel,
                    self.main.aspect_panel)
 

        self.main.canvas.draw()


    def plotfield(self):

        # field is the field name in each panel, i.e., 'Bx', 'By', ...
        field = self.main.field_panel[self.main.panelselect-1]
        t = self.main.tstep  # current time step

        x1min, x1max, \
        x2min, x2max, \
        iloc1, iloc2, \
        jloc1, jloc2, \
        kloc1, kloc2 = self.getSpaceRanges()

        if self.main.dim == 2:

            self.main.cbars[(self.main.panelselect-1)] = self.makeplot.plotfield2D(
                self.main.figure, 
                self.main.fdata_container[(field,t)][jloc1:jloc2,iloc1:iloc2],
                self.main.nrow, 
                self.main.ncolumn,
                self.main.field_panel[self.main.panelselect-1],
                self.main.panelselect, 
                self.main.time,
                x1min,
                x1max,
                x2min,
                x2max,
                self.main.aspect_panel[self.main.panelselect-1],
                self.main.cbars[(self.main.panelselect-1)])

        else:   # 3D
            self.main.cbars[(self.main.panelselect-1)]=self.makeplot.plotfield3D(
                self.main.figure,
                self.main.fdata_container[(field,t)][iloc1:iloc2,jloc1:jloc2,kloc1:kloc2],
                self.main.nrow, 
                self.main.ncolumn,
                self.main.field_panel[self.main.panelselect-1],
                self.main.panelselect,
                self.main.time,
                self.main.sliceplane_panel[self.main.panelselect-1],
                x1min,
                x1max,
                x2min,
                x2max,
                self.main.aspect_panel[self.main.panelselect-1],
                self.main.cbars[(self.main.panelselect-1)])

        self.main.canvas.draw()

    def plotparticle(self):

        species = self.main.species_panel[self.main.panelselect-1]
        # variable is a pair element [x,px], [y,px], ...
        phase = self.main.phase_panel[self.main.panelselect-1]
        stride = self.main.strideSlider.value()

        # get space range of the current selected panel
        x1min, x1max, \
        x2min, x2max, \
        dummy, dummy, \
        dummy, dummy, \
        dummy, dummy = self.getSpaceRanges()

        for loc in range(2):
            if phase[loc] == 'ene':
                if (species,'ene', self.main.tstep) in self.main.pdata_container.keys():
                    pass
                else:
                    self.main.pdata_container[(species,'ene',self.main.tstep)] = particle_energy(
                            self.main.pdata_container[(species,'px',self.main.tstep)],
                            self.main.pdata_container[(species,'py',self.main.tstep)],
                            self.main.pdata_container[(species,'pz',self.main.tstep)])

        if self.main.dim == 2:
            self.main.cbars[(self.main.panelselect-1)] = self.makeplot.plotparticle(
                    self.main.figure,
                    self.main.pdata_container[(species,phase[0],self.main.tstep)],
                    self.main.pdata_container[(species,phase[1],self.main.tstep)],
                    self.main.pdata_container[(species,'w',self.main.tstep)],
                    self.main.nrow, 
                    self.main.ncolumn,
                    species,
                    phase,
                    self.main.panelselect, 
                    self.main.time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    self.main.aspect_panel[self.main.panelselect-1],
                    self.main.cbars[(self.main.panelselect-1)])

        else:

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                zvalue = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*(slicevalue/30.)
                width = (self.main.zaxis[-1]-self.main.zaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'z',self.main.tstep)] > zvalue-.5*width) & \
                       (self.main.pdata_container[(species,'z',self.main.tstep)] < zvalue+.5*width))[0]
                
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*(slicevalue/30.)
                width = (self.main.yaxis[-1]-self.main.yaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'y',self.main.tstep)] > yvalue-.5*width) & \
                       (self.main.pdata_container[(species,'y',self.main.tstep)] < yvalue+.5*width))[0]

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                xvalue = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*(slicevalue/30.)
                width = (self.main.xaxis[-1]-self.main.xaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'x',self.main.tstep)] > xvalue-.5*width) & \
                       (self.main.pdata_container[(species,'x',self.main.tstep)] < xvalue+.5*width))[0]

            self.main.cbars[(self.main.panelselect-1)] = self.makeplot.plotparticle(
                    self.main.figure,
                    self.main.pdata_container[(species,phase[0],self.main.tstep)][loc],
                    self.main.pdata_container[(species,phase[1],self.main.tstep)][loc],
                    self.main.pdata_container[(species,'w',self.main.tstep)][loc],
                    self.main.nrow, 
                    self.main.ncolumn,
                    species,
                    phase,
                    self.main.panelselect,
                    self.main.time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    self.main.aspect_panel[self.main.panelselect-1],
                    self.main.cbars[(self.main.panelselect-1)])

        self.main.canvas.draw()



    def getLocalparticleLoc(self):
        """
        Select particle indices located within the particle stride of the 3rd axis
        """
        loc_container = {}

        # Find which panels have particleselection.
        # i.e., index = [0,1,3,5,..] --> panels 0, 1, 3, 5 .. have particle plots.
        index = [i for i, yesfield in enumerate(self.main.field_select_panel) if not yesfield]
        stride = self.main.strideSlider.value()
        for l in index:
            species = self.main.species_panel[l]
            if self.main.sliceplane_panel[l] == 'xy':
                slicevalue = self.main.slicevalue_panel[l]
                zvalue = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*(slicevalue/30.)
                width = (self.main.zaxis[-1]-self.main.zaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'z',self.main.tstep)] > zvalue-.5*width) & \
                       (self.main.pdata_container[(species,'z',self.main.tstep)] < zvalue+.5*width))[0]
                
            if self.main.sliceplane_panel[l] == 'xz':
                slicevalue = self.main.slicevalue_panel[l]
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*(slicevalue/30.)
                width = (self.main.yaxis[-1]-self.main.yaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'y',self.main.tstep)] > yvalue-.5*width) & \
                       (self.main.pdata_container[(species,'y',self.main.tstep)] < yvalue+.5*width))[0]

            if self.main.sliceplane_panel[l] == 'yz':
                slicevalue = self.main.slicevalue_panel[l]
                xvalue = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*(slicevalue/30.)
                width = (self.main.xaxis[-1]-self.main.xaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'x',self.main.tstep)] > xvalue-.5*width) & \
                       (self.main.pdata_container[(species,'x',self.main.tstep)] < xvalue+.5*width))[0]

            loc_container[(l)] = loc

        return loc_container

    def getSpaceRanges(self):
        """
        Get space range values

        """
        if self.main.dim == 2:
            # xminloc, xmaxloc, ... are values in [0,99]
            xminloc = self.main.xminloc_panel[self.main.panelselect-1]
            xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
            zminloc = self.main.zminloc_panel[self.main.panelselect-1]
            zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
            # x1min, x1max, ... are coordinates
            x1min = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100.
            x1max = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100.
            x2min = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
            x2max = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
            # iloc1, iloc2, .. are grids
            jloc1 = int(len(self.main.xaxis)*xminloc/100.)
            jloc2 = int(len(self.main.xaxis)*xmaxloc/100.)
            iloc1 = int(len(self.main.zaxis)*zminloc/100.)
            iloc2 = int(len(self.main.zaxis)*zmaxloc/100.)

            kloc1 = 1
            kloc2 = 1
            
        else:   # 3D
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                xminloc = self.main.xminloc_panel[self.main.panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
                yminloc = self.main.yminloc_panel[self.main.panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[self.main.panelselect-1]
                x1min = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
                x1max = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
                x2min = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*yminloc/100.
                x2max = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*ymaxloc/100.
                iloc1 = int(len(self.main.xaxis)*xminloc/100.)
                iloc2 = int(len(self.main.xaxis)*xmaxloc/100.)
                jloc1 = int(len(self.main.yaxis)*yminloc/100.)
                jloc2 = int(len(self.main.yaxis)*ymaxloc/100.)
                kloc1 = int(1.0*len(self.main.zaxis)*self.main.slicevalue_panel[self.main.panelselect-1]/30)
                kloc2 = kloc1+1
                
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                xminloc = self.main.xminloc_panel[self.main.panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
                zminloc = self.main.zminloc_panel[self.main.panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
                x1min = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100.
                x1max = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100.
                x2min = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
                x2max = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
                iloc1 = int(len(self.main.xaxis)*xminloc/100.)
                iloc2 = int(len(self.main.xaxis)*xmaxloc/100.)
                kloc1 = int(len(self.main.zaxis)*zminloc/100.)
                kloc2 = int(len(self.main.zaxis)*zmaxloc/100.)
                jloc1 = int(1.0*len(self.main.yaxis)*self.main.slicevalue_panel[self.main.panelselect-1]/30.)
                jloc2 = jloc1+1

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                yminloc = self.main.yminloc_panel[self.main.panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[self.main.panelselect-1]
                zminloc = self.main.zminloc_panel[self.main.panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
                x1min = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100.
                x1max = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100.
                x2min = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*yminloc/100.
                x2max = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*ymaxloc/100.
                jloc1 = int(len(self.main.yaxis)*yminloc/100.)
                jloc2 = int(len(self.main.yaxis)*ymaxloc/100.)
                kloc1 = int(len(self.main.zaxis)*zminloc/100.)
                kloc2 = int(len(self.main.zaxis)*zmaxloc/100.)
                iloc1 = int(1.0*len(self.main.xaxis)*self.main.slicevalue_panel[self.main.panelselect-1]/30)
                iloc2 = iloc1+1

        return x1min, x1max, x2min, x2max, iloc1, iloc2, jloc1, jloc2, kloc1, kloc2



  