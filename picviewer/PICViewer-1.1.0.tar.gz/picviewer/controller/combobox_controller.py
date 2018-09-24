import numpy as np

from picviewer.dataloader.collectdata import CollectData
from picviewer.dataplotter.prepareplot import PreparePlot

class ComboboxController():
    """
        combobox control class
        
    """
    def __init__(self,Mainwindow):

        self.main = Mainwindow

        # colletc data class
        self.collectdata = CollectData(self.main)
        # prepare data class
        self.prepareplot = PreparePlot(self.main)

    def fieldbutton(self):

        self.main.field_select_panel[self.main.panelselect-1] = True

        self.collectdata.loadfield()
        self.prepareplot.plotfield()

    def fieldcombobox(self):

        self.main.fieldButton.setChecked(True)
        self.main.field_select_panel[self.main.panelselect-1] = True
        index=self.main.fieldsComboBox.currentIndex()
        self.main.field_panel[self.main.panelselect-1] = self.main.field_list[index]

        self.collectdata.loadfield()
        self.prepareplot.plotfield()

    def particlebutton(self):
   
        self.main.field_select_panel[self.main.panelselect-1] = False

        self.collectdata.loadparticle()
        self.prepareplot.plotparticle()


    def speciescombobox(self):

        self.main.particleButton.setChecked(True)
        self.main.field_select_panel[self.main.panelselect-1] = False
        index=self.main.speciesComboBox.currentIndex()
        self.main.species_panel[self.main.panelselect-1] = self.main.species_list[index]

        self.collectdata.loadparticle()
        self.prepareplot.plotparticle()

        
    def phasecombobox(self):

        self.main.particleButton.setChecked(True)
        self.main.field_select_panel[self.main.panelselect-1] = False
        index=self.main.phaseComboBox.currentIndex()
        if self.main.dim == 2:
            self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list1[index]
        else:
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xy':
                self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list2[index]
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'xz':
                self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list1[index]
            if self.main.sliceplane_panel[self.main.panelselect-1] == 'yz':
                self.main.phase_panel[self.main.panelselect-1] = self.main.phase_list3[index]

        self.collectdata.loadfield()
        self.prepareplot.plotfield()



