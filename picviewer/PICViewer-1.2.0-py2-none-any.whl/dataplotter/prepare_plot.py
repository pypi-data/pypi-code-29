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

        field_keywords = []
        particle_keywords = []

        for l in range(self.main.nrow*self.main.ncolumn):

            tstep = self.main.tstep_panel[l]
            if self.main.field_select_panel[l]:
                field = self.main.field_panel[l]
                field_keywords.append((field,tstep))

            else:
                sepcies = self.main.species_panel[l]
                # phase is a tuple variable, i.e.,  ('px','x'), ('x','z'), ('ene','z'),...
                phase = self.main.phase_panel[l]
                particle_keywords.append((sepcies,phase[0],tstep))
                particle_keywords.append((sepcies,phase[1],tstep))
                # add weight 'w' to the keywords
                particle_keywords.append((sepcies,'w',tstep))

        # i.e., particle_keywords = [('elec', 'px', 10), ('elec', 'x', 5), .... ]
        #  ---> keywords may be overwrapped in field_keywords or particle_keywords.
        # but the keywrods in the data dictionaries are not overwarpped.
      
        for keywords in particle_keywords:
            if keywords[1] == 'ene':
                if (keywords[0],'ene', keywords[2]) in self.main.pdata_container.keys():
                    pass
                else:
                    self.main.pdata_container[(keywords[0],'ene', keywords[2])] = particle_energy(
                            self.main.pdata_container[(keywords[0],'px',keywords[2])],
                            self.main.pdata_container[(keywords[0],'py',keywords[2])],
                            self.main.pdata_container[(keywords[0],'pz',keywords[2])])

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
                    self.main.tstep_panel,
                    self.main.taxis,
                    self.main.xaxis_dic,
                    self.main.zaxis_dic,
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
                    self.main.tstep_panel,
                    self.main.taxis,
                    self.main.sliceplane_panel,
                    self.main.slicevalue_panel,
                    self.main.xaxis_dic,
                    self.main.yaxis_dic,
                    self.main.zaxis_dic,
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

        panelselect = self.main.panelselect
        field = self.main.field_panel[panelselect-1]
        tstep = self.main.tstep_panel[panelselect-1]  # current time step
        nrow = self.main.nrow
        ncolumn = self.main.ncolumn       
        time = self.main.taxis[tstep-1]
        aspect = self.main.aspect_panel[panelselect-1]
        cbar = self.main.cbars[(panelselect-1)]

        x1min, x1max, \
        x2min, x2max, \
        iloc1, iloc2, \
        jloc1, jloc2, \
        kloc1, kloc2 = self.getSpaceRanges()

        if self.main.dim == 2:

            self.main.cbars[(panelselect-1)] = self.makeplot.plotfield2D(
                self.main.figure, 
                self.main.fdata_container[(field,tstep)][jloc1:jloc2,iloc1:iloc2],
                nrow, 
                ncolumn,
                field,
                panelselect, 
                time,
                x1min,
                x1max,
                x2min,
                x2max,
                aspect,
                cbar)

        else:   # 3D
            sliceplane = self.main.sliceplane_panel[panelselect-1]

            self.main.cbars[(panelselect-1)]=self.makeplot.plotfield3D(
                self.main.figure,
                self.main.fdata_container[(field,tstep)][iloc1:iloc2,jloc1:jloc2,kloc1:kloc2],
                nrow, 
                ncolumn,
                field,
                panelselect, 
                time,
                sliceplane,
                x1min,
                x1max,
                x2min,
                x2max,
                aspect,
                cbar)

        self.main.canvas.draw()

    def plotparticle(self):

        panelselect = self.main.panelselect
        tstep = self.main.tstep_panel[panelselect-1]
        xaxis = self.main.xaxis_dic[tstep-1]
        yaxis = self.main.yaxis_dic[tstep-1]
        zaxis = self.main.zaxis_dic[tstep-1]

        nrow = self.main.nrow
        ncolumn = self.main.ncolumn
        species = self.main.species_panel[panelselect-1]
        phase = self.main.phase_panel[panelselect-1]
        time = self.main.taxis[tstep-1]
        aspect = self.main.aspect_panel[panelselect-1]
        cbar = self.main.cbars[(panelselect-1)]
        
        # get space range of the current selected panel
        x1min, x1max, \
        x2min, x2max, \
        dummy, dummy, \
        dummy, dummy, \
        dummy, dummy = self.getSpaceRanges()

        # make an energy container from px, py, and pz
        for phase_ind in range(2):
            if phase[phase_ind] == 'ene':
                if (species,'ene', tstep) in self.main.pdata_container.keys():
                    pass
                else:
                    self.main.pdata_container[(species,'ene',tstep)] = particle_energy(
                            self.main.pdata_container[(species,'px',tstep)],
                            self.main.pdata_container[(species,'py',tstep)],
                            self.main.pdata_container[(species,'pz',tstep)])

        if self.main.dim == 2:
            self.main.cbars[(panelselect-1)] = self.makeplot.plotparticle(
                    self.main.figure,
                    self.main.pdata_container[(species,phase[0],tstep)],
                    self.main.pdata_container[(species,phase[1],tstep)],
                    self.main.pdata_container[(species,'w',tstep)],
                    nrow, 
                    ncolumn,
                    species,
                    phase,
                    panelselect, 
                    time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    aspect,
                    cbar)

        else:
            sliceplane = self.main.sliceplane_panel[panelselect-1]
            slicevalue = self.main.slicevalue_panel[panelselect-1]
            stride = self.main.strideSlider.value()

            if sliceplane == 'xy':
                zvalue = zaxis[0]+(zaxis[-1]-zaxis[0])*(slicevalue/30.)
                width = (zaxis[-1]-zaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'z',tstep)] > zvalue-.5*width) & \
                       (self.main.pdata_container[(species,'z',tstep)] < zvalue+.5*width))[0]
                
            if sliceplane == 'xz':
                yvalue = yaxis[0]+(yaxis[-1]-yaxis[0])*(slicevalue/30.)
                width = (yaxis[-1]-yaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'y',tstep)] > yvalue-.5*width) & \
                       (self.main.pdata_container[(species,'y',tstep)] < yvalue+.5*width))[0]

            if sliceplane == 'yz':
                xvalue = xaxis[0]+(xaxis[-1]-xaxis[0])*(slicevalue/30.)
                width = (xaxis[-1]-xaxis[0])*(stride/30.)
                loc = np.where((self.main.pdata_container[(species,'x',tstep)] > xvalue-.5*width) & \
                       (self.main.pdata_container[(species,'x',tstep)] < xvalue+.5*width))[0]

            self.main.cbars[(self.main.panelselect-1)] = self.makeplot.plotparticle(
                    self.main.figure,
                    self.main.pdata_container[(species,phase[0],tstep)][loc],
                    self.main.pdata_container[(species,phase[1],tstep)][loc],
                    self.main.pdata_container[(species,'w',tstep)][loc],
                    nrow, 
                    ncolumn,
                    species,
                    phase,
                    panelselect,
                    time,
                    x1min,
                    x1max,
                    x2min,
                    x2max,
                    aspect,
                    cbar)

        self.main.canvas.draw()

    def getLocalparticleLoc(self):
        """
        Select particle indices located within the particle stride of the 3rd axis
        """
        loc_container = {}

        stride = self.main.strideSlider.value()

        for l in range(self.main.nrow*self.main.ncolumn):

            if not self.main.field_select_panel[l]:

                tstep = self.main.tstep_panel[l]
                species = self.main.species_panel[l]
                xaxis = self.main.xaxis_dic[tstep-1]
                yaxis = self.main.yaxis_dic[tstep-1]
                zaxis = self.main.zaxis_dic[tstep-1]
                slicevalue = self.main.slicevalue_panel[l]
                
                if self.main.sliceplane_panel[l] == 'xy':
                    zvalue = zaxis[0]+(zaxis[-1]-zaxis[0])*(slicevalue/30.)
                    width = (zaxis[-1]-zaxis[0])*(stride/30.)
                    loc = np.where((self.main.pdata_container[(species,'z',tstep)] > zvalue-.5*width) & \
                        (self.main.pdata_container[(species,'z',tstep)] < zvalue+.5*width))[0]

                if self.main.sliceplane_panel[l] == 'xz':
                    yvalue = yaxis[0]+(yaxis[-1]-yaxis[0])*(slicevalue/30.)
                    width = (yaxis[-1]-yaxis[0])*(stride/30.)
                    loc = np.where((self.main.pdata_container[(species,'y',tstep)] > yvalue-.5*width) & \
                        (self.main.pdata_container[(species,'y',tstep)] < yvalue+.5*width))[0]

                if self.main.sliceplane_panel[l] == 'yz':
                    xvalue = xaxis[0]+(xaxis[-1]-xaxis[0])*(slicevalue/30.)
                    width = (xaxis[-1]-xaxis[0])*(stride/30.)
                    loc = np.where((self.main.pdata_container[(species,'x',tstep)] > xvalue-.5*width) & \
                        (self.main.pdata_container[(species,'x',tstep)] < xvalue+.5*width))[0]

                loc_container[l] = loc

        return loc_container

    def getSpaceRanges(self):
        """
        Get space range values

        """
        panelselect = self.main.panelselect
        tstep = self.main.tstep_panel[panelselect-1]
        xaxis = self.main.xaxis_dic[tstep-1]
        yaxis = self.main.yaxis_dic[tstep-1]
        zaxis = self.main.zaxis_dic[tstep-1]

        if self.main.dim == 2:
            # xminloc, xmaxloc, ... are values in [0,99]
            xminloc = self.main.xminloc_panel[panelselect-1]
            xmaxloc = self.main.xmaxloc_panel[panelselect-1]
            zminloc = self.main.zminloc_panel[panelselect-1]
            zmaxloc = self.main.zmaxloc_panel[panelselect-1]
            # x1min, x1max, ... are coordinates
            x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc/100.
            x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc/100.
            x2min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc/100.
            x2max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc/100.
            # iloc1, iloc2, .. are grids
            jloc1 = int(len(xaxis)*xminloc/100.)
            jloc2 = int(len(xaxis)*xmaxloc/100.)
            iloc1 = int(len(zaxis)*zminloc/100.)
            iloc2 = int(len(zaxis)*zmaxloc/100.)

            kloc1 = 1
            kloc2 = 1
            
        else:   # 3D
            if self.main.sliceplane_panel[panelselect-1] == 'xy':
                xminloc = self.main.xminloc_panel[panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[panelselect-1]
                yminloc = self.main.yminloc_panel[panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[panelselect-1]
                x1min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc/100.
                x1max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc/100.
                x2min = yaxis[0]+(yaxis[-1]-yaxis[0])*yminloc/100.
                x2max = yaxis[0]+(yaxis[-1]-yaxis[0])*ymaxloc/100.
                iloc1 = int(len(xaxis)*xminloc/100.)
                iloc2 = int(len(xaxis)*xmaxloc/100.)
                jloc1 = int(len(yaxis)*yminloc/100.)
                jloc2 = int(len(yaxis)*ymaxloc/100.)
                kloc1 = int(1.0*len(zaxis)*self.main.slicevalue_panel[panelselect-1]/30)
                kloc2 = kloc1+1
                
            if self.main.sliceplane_panel[panelselect-1] == 'xz':
                xminloc = self.main.xminloc_panel[panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[panelselect-1]
                zminloc = self.main.zminloc_panel[panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[panelselect-1]
                x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc/100.
                x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc/100.
                x2min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc/100.
                x2max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc/100.
                iloc1 = int(len(xaxis)*xminloc/100.)
                iloc2 = int(len(xaxis)*xmaxloc/100.)
                kloc1 = int(len(zaxis)*zminloc/100.)
                kloc2 = int(len(zaxis)*zmaxloc/100.)
                jloc1 = int(1.0*len(yaxis)*self.main.slicevalue_panel[panelselect-1]/30.)
                jloc2 = jloc1+1

            if self.main.sliceplane_panel[panelselect-1] == 'yz':
                yminloc = self.main.yminloc_panel[panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[panelselect-1]
                zminloc = self.main.zminloc_panel[panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[panelselect-1]
                x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc/100.
                x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc/100.
                x2min = yaxis[0]+(yaxis[-1]-yaxis[0])*yminloc/100.
                x2max = yaxis[0]+(yaxis[-1]-yaxis[0])*ymaxloc/100.
                jloc1 = int(len(yaxis)*yminloc/100.)
                jloc2 = int(len(yaxis)*ymaxloc/100.)
                kloc1 = int(len(zaxis)*zminloc/100.)
                kloc2 = int(len(zaxis)*zmaxloc/100.)
                iloc1 = int(1.0*len(xaxis)*self.main.slicevalue_panel[panelselect-1]/30)
                iloc2 = iloc1+1

        return x1min, x1max, x2min, x2max, iloc1, iloc2, jloc1, jloc2, kloc1, kloc2



  