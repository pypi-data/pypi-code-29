"""
Zinc Glyph Chooser Widget

Widget for chooses a glyph from a glyph module, derived from QComboBox

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.status import OK as ZINC_OK

class GlyphChooserWidget(QtGui.QComboBox):

    def __init__(self, parent=None):
        '''
        Call the super class init functions
        '''
        QtGui.QComboBox.__init__(self, parent)
        self._nullObjectName = None
        self._glyphmodule = None
        self._glyph = None

    def _buildGlyphList(self):
        '''
        Rebuilds the list of items in the ComboBox from the glyph module
        '''
        self.blockSignals(True)
        self.clear()
        if self._glyphmodule:
            if self._nullObjectName:
                self.addItem(self._nullObjectName)
            glyphiter = self._glyphmodule.createGlyphiterator()
            glyph = glyphiter.next()
            while glyph.isValid():
                name = glyph.getName()
                self.addItem(name)
                glyph = glyphiter.next()
        self.blockSignals(False)
        self._displayGlyph()

    def _displayGlyph(self):
        '''
        Display the currently chosen glyph in the ComboBox
        '''
        self.blockSignals(True)
        if self._glyph:
            glyphName = self._glyph.getName()
            # following doesn't handle glyph name matching _nullObjectName
            index = self.findText(glyphName)
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

    def setGlyphmodule(self, glyphmodule):
        '''
        Sets the region that this widget chooses glyphs from
        '''
        self._glyphmodule = glyphmodule
        self._buildGlyphList()

    def getGlyph(self):
        '''
        Must call this from currentIndexChanged() slot to get/update current glyph
        '''
        glyphName = str(self.currentText())
        if self._nullObjectName and (glyphName == self._nullObjectName):
            self._glyph = None
        else:
            self._glyph = self._glyphmodule.findGlyphByName(glyphName)
        return self._glyph

    def setGlyph(self, glyph):
        '''
        Set the currently selected glyph
        '''
        if not glyph or not glyph.isValid():
            self._glyph = None
        else:
            self._glyph = glyph
        self._displayGlyph()
