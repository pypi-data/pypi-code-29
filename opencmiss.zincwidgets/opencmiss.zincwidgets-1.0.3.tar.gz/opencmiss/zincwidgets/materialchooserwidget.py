"""
Zinc Material Chooser Widget

Widget for chooses a material from a material module, derived from QComboBox

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

from opencmiss.zinc.material import Material
from opencmiss.zinc.status import OK as ZINC_OK

class MaterialChooserWidget(QtGui.QComboBox):

    def __init__(self, parent=None):
        '''
        Call the super class init functions
        '''
        QtGui.QComboBox.__init__(self, parent)
        self._nullObjectName = None
        self._materialmodule = None
        self._material = None

    def _buildMaterialList(self):
        '''
        Rebuilds the list of items in the ComboBox from the material module
        '''
        self.blockSignals(True)
        self.clear()
        if self._materialmodule:
            if self._nullObjectName:
                self.addItem(self._nullObjectName)
            materialiter = self._materialmodule.createMaterialiterator()
            material = materialiter.next()
            while material.isValid():
                name = material.getName()
                self.addItem(name)
                material = materialiter.next()
        self.blockSignals(False)
        self._displayMaterial()

    def _displayMaterial(self):
        '''
        Display the currently chosen material in the ComboBox
        '''
        self.blockSignals(True)
        if self._material:
            materialName = self._material.getName()
            # following doesn't handle material name matching _nullObjectName
            index = self.findText(materialName)
        else:
            index = 0
        self.setCurrentIndex(index)
        self.blockSignals(False)

    def setNullObjectName(self, nullObjectName):
        '''
        Enable a null object option with the supplied name e.g. '-' or '<select>'
        Default is None
        '''
        self._nullObjectName  = nullObjectName

    def setMaterialmodule(self, materialmodule):
        '''
        Sets the region that this widget chooses materials from
        '''
        self._materialmodule = materialmodule
        self._buildMaterialList()

    def getMaterial(self):
        '''
        Must call this from currentIndexChanged() slot to get/update current material
        '''
        materialName = str(self.currentText())
        if self._nullObjectName and (materialName == self._nullObjectName):
            self._material = None
        else:
            self._material = self._materialmodule.findMaterialByName(materialName)
        return self._material

    def setMaterial(self, material):
        '''
        Set the currently selected material
        '''
        if not material or not material.isValid():
            self._material = None
        else:
            self._material = material
        self._displayMaterial()
