import numpy as np

from picviewer.dataloader.collectdata import CollectData
from picviewer.dataplotter.prepareplot import PreparePlot

class SliceController():
    """
        combobox control class
        
    """

    def __init__(self,Mainwindow):

        self.main = Mainwindow

        # colletc data class
        self.collectdata = CollectData(self.main)
        # prepare data class
        self.prepareplot = PreparePlot(self.main)

    def slicebutton(self):

        if self.main.dim == 3:    # only works for 3D
            
            if self.main.xyButton.isChecked():
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.main.slicevalueSlider.setValue(slicevalue)
                    self.main.slicevalue_panel[self.main.panelselect-1] = slicevalue
                else:
                    self.main.sliceplane_panel[self.main.panelselect-1] = 'xy'
                    slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                    self.main.slicevalueSlider.setValue(slicevalue)
                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.main.phaseComboBox.currentIndex()
                    self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list2[index]
                    self.main.phaseComboBox.clear() 
                    for i in np.arange(len(self.main.phase_list2)):
                        self.main.phaseComboBox.addItem(self.main.phase_list2[i][0]+'-'+self.main.phase_list2[i][1], i)
                    self.main.phaseComboBox.setCurrentIndex(index)
                
                zvalue = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("z=%.2f" %zvalue))
                stride = self.main.strideSlider.value()
                self.main.strideLabel.setText(u'\u0394'+ "z=%.2f" %(stride/30.))

                
            if self.main.xzButton.isChecked():
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.main.slicevalueSlider.setValue(slicevalue)
                    self.main.slicevalue_panel[self.main.panelselect-1] = slicevalue
                else:
                    self.main.sliceplane_panel[self.main.panelselect-1] = 'xz'
                    slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                    self.main.slicevalueSlider.setValue(slicevalue)

                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.main.phaseComboBox.currentIndex()
                    self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list1[index]
                    self.main.phaseComboBox.clear() 
                    for i in np.arange(len(self.main.phase_list1)):
                        self.main.phaseComboBox.addItem(self.main.phase_list1[i][0]+'-'+self.main.phase_list1[i][1], i)
                    self.main.phaseComboBox.setCurrentIndex(index)
                    
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("y=%.2f" %yvalue))
                stride = self.main.strideSlider.value()
                self.main.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))
   
            if self.main.yzButton.isChecked():        
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                    # if select the same button, return the slice value to the median
                    slicevalue = 15
                    self.main.slicevalueSlider.setValue(slicevalue)
                    self.main.slicevalue_panel[self.main.panelselect-1] = slicevalue
                else:
                    self.main.sliceplane_panel[self.main.panelselect-1] = 'yz'
                    slicevalue = self.main.slicevalue_panel[self.main.panelselect-1]
                    self.main.slicevalueSlider.setValue(slicevalue)

                    # change the space range labels
                    self.ChangeRangeSliderLabels()

                    # change the phase combo-box menus
                    index=self.main.phaseComboBox.currentIndex()
                    self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list3[index]
                    self.main.phaseComboBox.clear() 
                    for i in np.arange(len(self.main.phase_list3)):
                        self.main.phaseComboBox.addItem(self.main.phase_list3[i][0]+'-'+self.main.phase_list3[i][1], i)
                    self.main.phaseComboBox.setCurrentIndex(index)

                xvalue = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("x=%.2f" %xvalue))
                stride = self.main.strideSlider.value()
                self.main.strideLabel.setText(u'\u0394'+ "x=%.2f" %(stride/30.))
                
        else:
            self.main.xzButton.setChecked(True)

        if self.main.dim == 3:

            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()

    def sliceslider(self):
        """
        Slider for the 3rd axis

        """
        if self.main.dim == 3:
            slicevalue = self.main.slicevalueSlider.value()
            self.main.slicevalue_panel[self.main.panelselect-1] = slicevalue
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                zvalue = self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("z=%.2f" %zvalue))
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                yvalue = self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("y=%.2f" %yvalue))
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                xvalue = self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*slicevalue/30.
                self.main.slicevalueLabel.setText(str("x=%.2f" %xvalue))

            if self.main.field_select_panel[self.main.panelselect-1]:
                self.collectdata.loadfield()
                self.prepareplot.plotfield()
            else:
                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()
                
        else:
            self.main.slicevalueSlider.setValue(15)

    def strideslider(self):
        """
        Stride in the 3rd axis for particle selection

        """
        if self.main.dim == 3:
            if self.main.particleButton.isChecked():
                stride = self.main.strideSlider.value()
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                    self.main.strideLabel.setText(u'\u0394'+ "z=%.2f" %(stride/30.))
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                    self.main.strideLabel.setText(u'\u0394'+ "y=%.2f" %(stride/30.))
                if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                    self.main.strideLabel.setText(u'\u0394'+ "x=%.2f" %(stride/30.))

                self.collectdata.loadparticle()
                self.prepareplot.plotparticle()
        else:
            self.main.strideSlider.setValue(15)



    def ChangeRangeSliderLabels(self):
        """
        Change the space range labels

        """
        if self.main.dim == 3:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                self.main.x1min.setText("xmin")
                self.main.x1max.setText("xmax")
                self.main.x2min.setText("ymin")
                self.main.x2max.setText("ymax")
                xminloc = self.main.xminloc_panel[self.main.panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
                yminloc = self.main.yminloc_panel[self.main.panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[self.main.panelselect-1]
                self.main.x1minSlider.setValue(xminloc)
                self.main.x1maxSlider.setValue(xmaxloc)
                self.main.x2minSlider.setValue(yminloc)
                self.main.x2maxSlider.setValue(ymaxloc)
                xmin=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
                xmax=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
                ymin=self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*yminloc/100.
                ymax=self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*ymaxloc/100.
                self.main.x1minLabel.setText(str("%.1f" %xmin))
                self.main.x1maxLabel.setText(str("%.1f" %xmax))
                self.main.x2minLabel.setText(str("%.1f" %ymin))
                self.main.x2maxLabel.setText(str("%.1f" %ymax))
                

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                self.main.x1min.setText("zmin")
                self.main.x1max.setText("zmax")
                self.main.x2min.setText("xmin")
                self.main.x2max.setText("xmax")
                xminloc = self.main.xminloc_panel[self.main.panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
                zminloc = self.main.zminloc_panel[self.main.panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
                self.main.x1minSlider.setValue(zminloc)
                self.main.x1maxSlider.setValue(zmaxloc)
                self.main.x2minSlider.setValue(xminloc)
                self.main.x2maxSlider.setValue(xmaxloc)
                xmin=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
                xmax=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
                zmin=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100. 
                zmax=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100. 
                self.main.x1minLabel.setText(str("%.1f" %zmin))
                self.main.x1maxLabel.setText(str("%.1f" %zmax))
                self.main.x2minLabel.setText(str("%.1f" %xmin))
                self.main.x2maxLabel.setText(str("%.1f" %xmax))

            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                self.main.x1min.setText("zmin")
                self.main.x1max.setText("zmax")
                self.main.x2min.setText("ymin")
                self.main.x2max.setText("ymax")
                yminloc = self.main.yminloc_panel[self.main.panelselect-1]
                ymaxloc = self.main.ymaxloc_panel[self.main.panelselect-1]
                zminloc = self.main.zminloc_panel[self.main.panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
                self.main.x1minSlider.setValue(zminloc)
                self.main.x1maxSlider.setValue(zmaxloc)
                self.main.x2minSlider.setValue(yminloc)
                self.main.x2maxSlider.setValue(ymaxloc)
                ymin=self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*yminloc/100. 
                ymax=self.main.yaxis[0]+(self.main.yaxis[-1]-self.main.yaxis[0])*ymaxloc/100.
                zmin=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100. 
                zmax=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100. 
                self.main.x1minLabel.setText(str("%.1f" %zmin))
                self.main.x1maxLabel.setText(str("%.1f" %zmax))
                self.main.x2minLabel.setText(str("%.1f" %ymin))
                self.main.x2maxLabel.setText(str("%.1f" %ymax))

        else:
                xminloc = self.main.xminloc_panel[self.main.panelselect-1]
                xmaxloc = self.main.xmaxloc_panel[self.main.panelselect-1]
                zminloc = self.main.zminloc_panel[self.main.panelselect-1]
                zmaxloc = self.main.zmaxloc_panel[self.main.panelselect-1]
                self.main.x1minSlider.setValue(zminloc)
                self.main.x1maxSlider.setValue(zmaxloc)
                self.main.x2minSlider.setValue(xminloc)
                self.main.x2maxSlider.setValue(xmaxloc)
                xmin=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xminloc/100.
                xmax=self.main.xaxis[0]+(self.main.xaxis[-1]-self.main.xaxis[0])*xmaxloc/100.
                zmin=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zminloc/100. 
                zmax=self.main.zaxis[0]+(self.main.zaxis[-1]-self.main.zaxis[0])*zmaxloc/100. 
                self.main.x1minLabel.setText(str("%.1f" %zmin))
                self.main.x1maxLabel.setText(str("%.1f" %zmax))
                self.main.x2minLabel.setText(str("%.1f" %xmin))
                self.main.x2maxLabel.setText(str("%.1f" %xmax))