import matplotlib
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LogNorm
from cic_histogram import histogram_cic_2d

#from matplotlib.figure import Figure

class MakePlot():
    """
        Plot Data class
        
    """
    def plotfield2D(self, 
            figure, 
            fdata, 
            nrow, 
            ncolumn, 
            field, 
            panel_select,
            time, 
            x1min,
            x1max,
            x2min,
            x2max,
            aspect,
            cbar):

        #figure.clear()

        interpolation = 'nearest'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'

        self.plot = figure.add_subplot(nrow,ncolumn,panel_select)

        cbar.remove()

        im =  self.plot.imshow(fdata, interpolation=interpolation, cmap='jet',
            origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect)

        self.plot.axes.set_xlim([x1min,x1max])
        self.plot.axes.set_ylim([x2min,x2max])
        self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
        self.plot.set_xlabel(xtitle, fontsize=fontsize)
        self.plot.set_ylabel(ytitle, fontsize=fontsize)

        ax = figure.gca()
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=cbarwidth, pad=0.)
        cb = figure.colorbar(im, cax=cax)

        if nrow < 4 or ncolumn < 4:
                self.plot.axes.get_figure().tight_layout()

        return cb

    def plotfield3D(self, 
            figure, 
            fdata, 
            nrow, 
            ncolumn, 
            field, 
            panel_select,
            time, 
            sliceplane,
            x1min,
            x1max,
            x2min,
            x2max,
            aspect,
            cbar):

        #figure.clear()

        interpolation = 'nearest'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        if sliceplane == 'xy':
            xtitle = r'x ($\mu$m)'; ytitle = r'y ($\mu$m)'
            fdata = fdata[:,:,0].T
        if sliceplane == 'xz':
            xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'
            fdata = fdata[:,0,:]
        if sliceplane == 'yz':
            xtitle = r'z ($\mu$m)'; ytitle = r'y ($\mu$m)'
            fdata = fdata[0,:,:]

        self.plot = figure.add_subplot(nrow,ncolumn,panel_select)
        
        cbar.remove()

        im =  self.plot.imshow(fdata, interpolation=interpolation, cmap='jet',
            origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect)

        self.plot.axes.set_xlim([x1min,x1max])
        self.plot.axes.set_ylim([x2min,x2max])
        self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
        self.plot.set_xlabel(xtitle, fontsize=fontsize)
        self.plot.set_ylabel(ytitle, fontsize=fontsize)

        ax = figure.gca()
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=cbarwidth, pad=0.)
        cb = figure.colorbar(im, cax=cax)

        #if nrow < 4 or ncolumn < 4:
        #        self.plot.axes.get_figure().tight_layout()

        return cb

    def makeplotsync2D(self, 
                    figure, 
                    fdata_container, 
                    pdata_container,
                    nrow, 
                    ncolumn,
                    field_select_panel,
                    field_panel, 
                    species_panel,
                    phase_panel,
                    tstep, 
                    time, 
                    xaxis,
                    zaxis, 
                    xminloc_panel,
                    xmaxloc_panel,
                    zminloc_panel,
                    zmaxloc_panel,
                    aspect):

        figure.clear()

        interpolation = 'nearest'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax
        axes={}
        cbars={}

        for l in np.arange(nrow*ncolumn):
            
            axes[(l)] = self.plot = figure.add_subplot(nrow,ncolumn,l+1)

            x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc_panel[l]/100.
            x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc_panel[l]/100.
            x2min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc_panel[l]/100.
            x2max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc_panel[l]/100.

            if field_select_panel[l]:
                # field plot
                field=field_panel[l]
            
                xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'
                iloc1 = int(len(zaxis)*zminloc_panel[l]/100.)
                iloc2 = int(len(zaxis)*zmaxloc_panel[l]/100.)
                jloc1 = int(len(xaxis)*xminloc_panel[l]/100.)
                jloc2 = int(len(xaxis)*xmaxloc_panel[l]/100.)

                self.plot.cla()
                im =  self.plot.imshow(fdata_container[(field, tstep)][jloc1:jloc2,iloc1:iloc2], 
                    interpolation=interpolation, cmap='jet',
                    origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect[l])

                self.plot.axes.set_xlim([x1min,x1max])
                self.plot.axes.set_ylim([x2min,x2max])
                self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
                self.plot.set_xlabel(xtitle, fontsize=fontsize)
                self.plot.set_ylabel(ytitle, fontsize=fontsize)

                ax = figure.gca()
                divider = make_axes_locatable(ax)
                cax = divider.append_axes("right", size=cbarwidth, pad=0.)
                cb = figure.colorbar(im, cax=cax)

            else:   # particle plot
                species = species_panel[l]
            
                # pahse is a tuple, i.e., (px,x) --> px is the x2 axis (y-axis), x is the x1 axis (x-axis)
                phase = phase_panel[l]

                title = species+' '+phase[0]+'-'+phase[1]
                nbin = 300
                
                # x1-axis (or x-axis) variables
                if phase[1] in ['px','py','pz']:
                    p1min = np.min(pdata_container[(species, phase[1], tstep)])
                    p1max = np.max(pdata_container[(species, phase[1], tstep)])
                    xtitle = r'%s ($c$)'%(phase[1])
                elif phase[1] in ['ene']:
                    p1min = np.min(pdata_container[(species, phase[1], tstep)])
                    p1max = np.max(pdata_container[(species, phase[1], tstep)])
                    xtitle = r'%s ($\gamma$-1)'%(phase[1])
                elif phase[1] in ['x','y','z']:
                    p1min = x1min
                    p1max = x1max
                    xtitle = r'%s ($\mu$m)'%(phase[1])

                # x2-axis (y-axis) variables
                if phase[0] in ['px','py','pz']:
                    p2min = np.min(pdata_container[(species, phase[0], tstep)])
                    p2max = np.max(pdata_container[(species, phase[0], tstep)])
                    ytitle = r'%s ($c$)'%(phase[0])
                elif phase[0] in ['ene']:
                    p2min = np.min(pdata_container[(species, phase[0], tstep)])
                    p2max = np.max(pdata_container[(species, phase[0], tstep)])
                    ytitle = r'%s ($\gamma$-1)'%(phase[0])
                elif phase[0] in ['x','y','z']:
                    p2min = x2min
                    p2max = x2max
                    ytitle = r'%s ($\mu$m)'%(phase[0])

                histogram = histogram_cic_2d( 
                        pdata_container[(species, phase[1], tstep)],
                        pdata_container[(species, phase[0], tstep)],    
                        pdata_container[(species, 'w', tstep)], 
                        nbin, p1min, p1max, nbin, p2min, p2max)   

                vmax=np.max(histogram)
                vmin = vmax*1.e-4
                #vmax *= contrast/100.
                #vmin *= 100./contrast
                logthresh=-np.log10(vmin)
                
                im = self.plot.imshow( histogram.T, 
                                origin='lower', extent=[ p1min,p1max,p2min,p2max ], 
                                aspect=aspect[l], interpolation=interpolation, cmap='jet',
                                vmin=vmin, vmax=vmax,
                                norm=matplotlib.colors.LogNorm(10**-logthresh))

                self.plot.axes.set_xlim([p1min,p1max])
                self.plot.axes.set_ylim([p2min,p2max])
                self.plot.set_title(title+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
                self.plot.set_xlabel(xtitle, fontsize=fontsize)
                self.plot.set_ylabel(ytitle, fontsize=fontsize)
                ax = figure.gca()
                divider = make_axes_locatable(ax)
                cax = divider.append_axes("right", size=cbarwidth, pad=0.)
                cb = figure.colorbar(im, cax=cax)

            cbars[(l)]= cb

            #if nrow < 4 or ncolumn < 4:
            #        self.plot.axes.get_figure().tight_layout()

        return axes, cbars
        

    def makeplotsync3D(self, 
                    figure, 
                    fdata_container, 
                    pdata_container,
                    loc_container,
                    nrow, 
                    ncolumn,
                    field_select_panel,
                    field_panel, 
                    species_panel,
                    phase_panel,
                    tstep, 
                    time, 
                    sliceplane_panel, 
                    slicevalue_panel,
                    xaxis,
                    yaxis,
                    zaxis, 
                    xminloc_panel,
                    xmaxloc_panel,
                    yminloc_panel,
                    ymaxloc_panel,
                    zminloc_panel,
                    zmaxloc_panel,
                    aspect):

        figure.clear()

        interpolation = 'nearest'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        axes={}
        cbars={}

        for l in np.arange(nrow*ncolumn):
            
            axes[(l)] = self.plot = figure.add_subplot(nrow,ncolumn,l+1)

            sliceplane = sliceplane_panel[l]
            slicevalue = slicevalue_panel[l]
            xminloc = xminloc_panel[l]
            xmaxloc = xmaxloc_panel[l]
            yminloc = yminloc_panel[l]
            ymaxloc = ymaxloc_panel[l]
            zminloc = zminloc_panel[l]
            zmaxloc = zmaxloc_panel[l]

            if sliceplane == 'xy':
                x1min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc/100.
                x1max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc/100.
                x2min = yaxis[0]+(yaxis[-1]-yaxis[0])*yminloc/100.
                x2max = yaxis[0]+(yaxis[-1]-yaxis[0])*ymaxloc/100.

            if sliceplane == 'xz':
                    xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'
                    x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc/100.
                    x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc/100.
                    x2min = xaxis[0]+(xaxis[-1]-xaxis[0])*xminloc/100.
                    x2max = xaxis[0]+(xaxis[-1]-xaxis[0])*xmaxloc/100.

            if sliceplane == 'yz':
                    xtitle = r'z ($\mu$m)'; ytitle = r'y ($\mu$m)'
                    x1min = zaxis[0]+(zaxis[-1]-zaxis[0])*zminloc/100.
                    x1max = zaxis[0]+(zaxis[-1]-zaxis[0])*zmaxloc/100.
                    x2min = yaxis[0]+(yaxis[-1]-yaxis[0])*yminloc/100.
                    x2max = yaxis[0]+(yaxis[-1]-yaxis[0])*ymaxloc/100.

            if field_select_panel[l]:
                # field plot
                field=field_panel[l]

                if sliceplane == 'xy':
                    xtitle = r'x ($\mu$m)'; ytitle = r'y ($\mu$m)'
                    iloc1 = int(len(xaxis)*xminloc/100.)
                    iloc2 = int(len(xaxis)*xmaxloc/100.)
                    jloc1 = int(len(yaxis)*yminloc/100.)
                    jloc2 = int(len(yaxis)*ymaxloc/100.)
                    kloc = int(1.0*len(zaxis)*slicevalue/30.)

                    im =  self.plot.imshow(fdata_container[(field, tstep)][iloc1:iloc2,jloc1:jloc2,kloc].T, 
                    interpolation=interpolation, cmap='jet',
                    origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect[l])

                if sliceplane == 'xz':
                    xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'
                    iloc1 = int(len(zaxis)*zminloc/100.)
                    iloc2 = int(len(zaxis)*zmaxloc/100.)
                    jloc1 = int(len(xaxis)*xminloc/100.)
                    jloc2 = int(len(xaxis)*xmaxloc/100.)
                    kloc = int(1.0*len(yaxis)*slicevalue/30)

                    im =  self.plot.imshow(fdata_container[(field, tstep)][jloc1:jloc2,kloc,iloc1:iloc2], 
                    interpolation=interpolation, cmap='jet',
                    origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect[l])

                if sliceplane == 'yz':
                    xtitle = r'z ($\mu$m)'; ytitle = r'y ($\mu$m)'
                    iloc1 = int(len(zaxis)*zminloc/100.)
                    iloc2 = int(len(zaxis)*zmaxloc/100.)
                    jloc1 = int(len(yaxis)*yminloc/100.)
                    jloc2 = int(len(yaxis)*ymaxloc/100.)
                    kloc = int(1.0*len(xaxis)*slicevalue/30)
                    
                    im =  self.plot.imshow(fdata_container[(field, tstep)][kloc,jloc1:jloc2,iloc1:iloc2],
                    interpolation=interpolation, cmap='jet',
                    origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect[l])

                self.plot.axes.set_xlim([x1min,x1max])
                self.plot.axes.set_ylim([x2min,x2max])
                self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
                self.plot.set_xlabel(xtitle, fontsize=fontsize)
                self.plot.set_ylabel(ytitle, fontsize=fontsize)

                ax = figure.gca()
                divider = make_axes_locatable(ax)
                cax = divider.append_axes("right", size=cbarwidth, pad=0.)
                cb = figure.colorbar(im, cax=cax)

            else:   # particle plot
                species = species_panel[l]
                phase = phase_panel[l]

                title = species+' '+phase[0]+'-'+phase[1]
                nbin = 300

                loc = loc_container[l]

                if phase[1] in ['px','py','pz']:
                    p1min = np.min(pdata_container[(species, phase[1], tstep)][loc])
                    p1max = np.max(pdata_container[(species, phase[1], tstep)][loc])
                    xtitle = r'%s ($c$)'%(phase[1])
                elif phase[1] in ['ene']:
                    p1min = np.min(pdata_container[(species, phase[1], tstep)][loc])
                    p1max = np.max(pdata_container[(species, phase[1], tstep)][loc])
                    xtitle = r'%s ($\gamma$-1)'%(phase[1])
                elif phase[1] in ['x','y','z']:
                    p1min = x1min
                    p1max = x1max
                    xtitle = r'%s ($\mu$m)'%(phase[1])

                if phase[0] in ['px','py','pz']:
                    p2min = np.min(pdata_container[(species, phase[0], tstep)][loc])
                    p2max = np.max(pdata_container[(species, phase[0], tstep)][loc])
                    ytitle = r'%s ($c$)'%(phase[0])
                elif phase[0] in ['ene']:
                    p2min = np.min(pdata_container[(species, phase[0], tstep)][loc])
                    p2max = np.max(pdata_container[(species, phase[0], tstep)][loc])
                    ytitle = r'%s ($\gamma$-1)'%(phase[0])
                elif phase[0] in ['x','y','z']:
                    p2min = x2min
                    p2max = x2max
                    ytitle = r'%s ($\mu$m)'%(phase[0])

                histogram = histogram_cic_2d( 
                        pdata_container[(species, phase[1], tstep)][loc],
                        pdata_container[(species, phase[0], tstep)][loc],    
                        pdata_container[(species, 'w', tstep)][loc], nbin, p1min, p1max, nbin, p2min, p2max)   

                vmax=np.max(histogram)
                vmin = vmax*1.e-4
                #vmax *= contrast/100.
                #vmin *= 100./contrast
                logthresh=-np.log10(vmin)
                
                im = self.plot.imshow( histogram.T, 
                                origin='lower', extent=[ p1min,p1max,p2min,p2max ], 
                                aspect=aspect[l], interpolation=interpolation, cmap='jet',
                                vmin=vmin, vmax=vmax,
                                norm=matplotlib.colors.LogNorm(10**-logthresh))

                self.plot.axes.set_xlim([p1min,p1max])
                self.plot.axes.set_ylim([p2min,p2max])
                self.plot.set_title(title+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
                self.plot.set_xlabel(xtitle, fontsize=fontsize)
                self.plot.set_ylabel(ytitle, fontsize=fontsize)
                ax = figure.gca()
                divider = make_axes_locatable(ax)
                cax = divider.append_axes("right", size=cbarwidth, pad=0.)
                cb = figure.colorbar(im, cax=cax)

            cbars[(l)]= cb

            #if nrow < 3 or ncolumn < 3:
            #    self.plot.axes.get_figure().tight_layout()

        return axes, cbars


    def plotparticle(self,
            figure,
            pdata2,
            pdata1,
            wdata,
            nrow,
            ncolumn,
            species,
            variable,
            panel_select,
            time,
            x1min,
            x1max,
            x2min,
            x2max,
            aspect,
            cbar):

        interpolation = 'nearest'

        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        title = species+' '+variable[0]+'-'+variable[1]

        xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'
        nbin = 300
        self.plot = figure.add_subplot(nrow,ncolumn,panel_select)
        self.plot.cla()

        cbar.remove()

        if variable[1] in ['px','py','pz']:
            p1min = np.min(pdata1)
            p1max = np.max(pdata1)
            xtitle = r'%s ($c$)'%(variable[1])
        elif variable[1] in ['ene']:
            p1min = np.min(pdata1)
            p1max = np.max(pdata1)
            xtitle = r'%s ($\gamma$-1)'%(variable[1])
        elif variable[1] in ['x','y','z']:
            p1min = x1min
            p1max = x1max
            xtitle = r'%s ($\mu$m)'%(variable[1])
        if variable[0] in ['px','py','pz']:
            p2min = np.min(pdata2)
            p2max = np.max(pdata2)
            ytitle = r'%s ($c$)'%(variable[0])
        elif variable[0] in ['ene']:
            p2min = np.min(pdata2)
            p2max = np.max(pdata2)
            ytitle = r'%s ($\gamma$-1)'%(variable[0])
        elif variable[0] in ['x','y','z']:
            p2min = x2min
            p2max = x2max
            ytitle = r'%s ($\mu$m)'%(variable[0])

        histogram = histogram_cic_2d( pdata1, pdata2, wdata, nbin, p1min, p1max, nbin, p2min, p2max)   
        vmax=np.max(histogram)
        vmin = vmax*1.e-4
        #vmax *= contrast/100.
        #vmin *= 100./contrast
        logthresh=-np.log10(vmin)
        
        im = self.plot.imshow( histogram.T, 
                        origin='lower', extent=[ p1min,p1max,p2min,p2max ], 
                        aspect=aspect, interpolation=interpolation, cmap='jet',
                        vmin=vmin, vmax=vmax,
                        norm=matplotlib.colors.LogNorm(10**-logthresh))

        self.plot.axes.set_xlim([p1min,p1max])
        self.plot.axes.set_ylim([p2min,p2max])
        self.plot.set_title(title+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
        self.plot.set_xlabel(xtitle, fontsize=fontsize)
        self.plot.set_ylabel(ytitle, fontsize=fontsize)
        ax = figure.gca()
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=cbarwidth, pad=0.)
        cb = figure.colorbar(im, cax=cax)


        if nrow < 4 or ncolumn < 4:
                self.plot.axes.get_figure().tight_layout()

        return cb



    def locallineplot2D(self, 
                figure, 
                nrow, 
                ncolumn, 
                field,
                panel_select,
                time,
                laxis, 
                ldata):
                
        interpolation = 'spline16'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        xtitle = r'l ($\mu$m)'; ytitle = field
        
        self.plot = figure.add_subplot(nrow,ncolumn,panel_select)
        self.plot.cla()

        self.plot.plot(laxis, ldata)

        self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
        self.plot.set_xlabel(xtitle, fontsize=fontsize)
        self.plot.set_ylabel(ytitle, fontsize=fontsize)

        if nrow < 4 or ncolumn < 4:
                self.plot.axes.get_figure().tight_layout()


    def localcontourplot2D(self, 
                figure, 
                fdata, 
                nrow, 
                ncolumn, 
                field,
                panel_select,
                time,
                x1min,
                x1max,
                x2min,
                x2max,
                aspect):

        interpolation = 'nearest'
        
        fontmax = 11; fontmin = 5.
        barmax = 0.12; barmin = 0.05
        matplotlib.rc('xtick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        matplotlib.rc('ytick', labelsize=int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax))
        fontsize = int((fontmin-fontmax)/(30-1)*(nrow*ncolumn-1)+fontmax)
        cbarwidth = (barmin-barmax)/(30-1)*(nrow*ncolumn-1)+barmax

        xtitle = r'z ($\mu$m)'; ytitle = r'x ($\mu$m)'

        self.plot = figure.add_subplot(nrow,ncolumn,panel_select)
        self.plot.cla()

        im =  self.plot.imshow(fdata, interpolation=interpolation, cmap='jet',
            origin='lower', extent=[x1min,x1max,x2min,x2max], aspect=aspect)

        self.plot.axes.set_xlim([x1min,x1max])
        self.plot.axes.set_ylim([x2min,x2max])
        self.plot.set_title(field+'  (%6.1f fs)'%(time), x=0.3, fontsize=fontsize)
        self.plot.set_xlabel(xtitle, fontsize=fontsize)
        self.plot.set_ylabel(ytitle, fontsize=fontsize)

        ax = figure.gca()
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=cbarwidth, pad=0.)
        cb = figure.colorbar(im, cax=cax)

        if nrow < 4 or ncolumn < 4:
                self.plot.axes.get_figure().tight_layout()
