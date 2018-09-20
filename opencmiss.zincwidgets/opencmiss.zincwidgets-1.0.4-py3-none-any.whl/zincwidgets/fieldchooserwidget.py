"""
Zinc Field Chooser Widget

Widget for choosing a field from a region, derived from QComboBox

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

from opencmiss.zinc.field import Field
from opencmiss.zinc.status import OK as ZINC_OK

class FieldChooserWidget(QtGui.QComboBox):

    def __init__(self, parent=None):
        '''
        Call the super class init functions
        '''
        QtGui.QComboBox.__init__(self, parent)
        self._nullObjectName = None
        self._region = None
        self._conditional = None
        self._field = None

    def _fieldmoduleCallback(self, fieldmoduleevent):
        '''
        Callback for change in fields; may need to rebuild field list
        '''
        changeSummary = fieldmoduleevent.getSummaryFieldChangeFlags()
        #print "_fieldmoduleCallback changeSummary =", changeSummary
        if (0 != (changeSummary & (Field.CHANGE_FLAG_IDENTIFIER | Field.CHANGE_FLAG_ADD | Field.CHANGE_FLAG_REMOVE))) or ((self._conditional != None) and (0 != (changeSummary & Field.CHANGE_FLAG_DEFINITION))):
            self._buildFieldList()

    def _buildFieldList(self):
        '''
        Rebuilds the list of items in the ComboBox from the field module
        '''
        self.blockSignals(True)
        self.clear()
        if self._region and self._region.isValid():
            if self._nullObjectName:
                self.addItem(self._nullObjectName)
            fielditer = self._region.getFieldmodule().createFielditerator()
            field = fielditer.next()
            while field.isValid():
                name = field.getName()
                if field.isManaged() and ((self._conditional is None) or self._conditional(field)):
                    self.addItem(name)
                field = fielditer.next()
        self.blockSignals(False)
        self._displayField()

    def _displayField(self):
        '''
        Display the currently chosen field in the ComboBox
        '''
        self.blockSignals(True)
        if self._field:
            fieldName = self._field.getName()
            # following doesn't handle field name matching _nullObjectName
            index = self.findText(fieldName)
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

    def getRegion(self):
        return self._region

    def setRegion(self, region):
        '''
        Sets the region that this widget chooses fields from
        '''
        if region and region.isValid():
            self._region = region
        else:
            self._region = None
        self._field = None
        self._buildFieldList()
        if region:
            self._fieldmodulenotifier = region.getFieldmodule().createFieldmodulenotifier()
            self._fieldmodulenotifier.setCallback(self._fieldmoduleCallback)
        else:
            self._fieldmodulenotifier = None

    def setConditional(self, conditional):
        '''
        Set a callable which takes a field and returns true if field should be included
        Call before setting the current field
        '''
        self._conditional = conditional
        self._buildFieldList()

    def getField(self):
        '''
        Must call this from currentIndexChanged() slot to get/update current field
        '''
        fieldName = str(self.currentText())
        if self._nullObjectName and (fieldName == self._nullObjectName):
            self._field = None
        else:
            self._field = self._region.getFieldmodule().findFieldByName(fieldName)
        return self._field

    def setField(self, field):
        '''
        Set the currently selected field; call after setConditional
        '''
        if not field or not field.isValid():
            self._field = None
        elif not field.isManaged():
            print("Field chooser cannot set unmanaged field")
            self._field = None
        elif self._conditional and not self._conditional(field):
            print("Field chooser cannot set field not satisfying conditional function")
            self._field = None
        else:
            self._field = field
        self._displayField()
