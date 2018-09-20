"""
Zinc Scene Editor Widget

Allows a Zinc Scene object to be edited in Qt / Python.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

from opencmiss.zincwidgets.sceneeditorwidget_ui import Ui_SceneEditorWidget
from opencmiss.zinc.field import Field
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.status import OK as ZINC_OK

class SceneEditorWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        '''
        Call the super class init functions
        '''
        QtGui.QWidget.__init__(self, parent)
        self._scene = None
        # Using composition to include the visual element of the GUI.
        self.ui = Ui_SceneEditorWidget()
        self.ui.setupUi(self)

    def getScene(self):
        '''
        Get the scene currently in the editor
        '''
        return self._scene

    def setScene(self, scene):
        '''
        Set the current scene in the editor
        '''
        if not (scene and scene.isValid()):
            self._scene = None
        else:
            self._scene = scene
        self.ui.graphics_editor.setScene(scene)
        if self._scene:
            self.ui.graphics_editor.setGraphics(self._scene.getFirstGraphics())
        self._buildGraphicsList()

    def _getDefaultCoordinateField(self):
        '''
        Get the first coordinate field from the current scene
        '''
        if self._scene:
            fielditer = self._scene.getRegion().getFieldmodule().createFielditerator()
            field = fielditer.next()
            while field.isValid():
                if field.isTypeCoordinate() and (field.getValueType() == Field.VALUE_TYPE_REAL) and \
                  (field.getNumberOfComponents() <= 3) and field.castFiniteElement().isValid():
                    return field
                field = fielditer.next()
        return None

    def _getGraphicsDisplayName(self, graphics):
        '''
        Build a display name from the graphics type and domain
        '''
        type = graphics.getType()
        fieldDomainType = graphics.getFieldDomainType()
        if type == Graphics.TYPE_POINTS:
           if fieldDomainType == Field.DOMAIN_TYPE_POINT:
               return "point"
           if fieldDomainType == Field.DOMAIN_TYPE_NODES:
               return "node points"
           if fieldDomainType == Field.DOMAIN_TYPE_DATAPOINTS:
               return "data points"
           return "element points"
        elif type == Graphics.TYPE_LINES:
            return "lines"
        elif type == Graphics.TYPE_SURFACES:
            return "surfaces"
        elif type == Graphics.TYPE_CONTOURS:
            return "contours"
        elif type == Graphics.TYPE_STREAMLINES:
            return "streamlines"

    def _buildGraphicsList(self):
        '''
        Fill the graphics list view with the list of graphics for current region/scene
        '''
        self._graphicsItems = QtGui.QStandardItemModel(self.ui.graphics_listview)
        selectedIndex = None
        if self._scene:
            selectedGraphics = self.ui.graphics_editor.getGraphics()
            graphics = self._scene.getFirstGraphics()
            while graphics and graphics.isValid():
                name = self._getGraphicsDisplayName(graphics)
                item = QtGui.QStandardItem(name)
                item.setData(graphics)
                item.setCheckable(True)
                item.setEditable(False)
                visible = graphics.getVisibilityFlag()
                item.setCheckState(QtCore.Qt.Checked if visible else QtCore.Qt.Unchecked)
                self._graphicsItems.appendRow(item)
                if graphics == selectedGraphics:
                    selectedIndex = self._graphicsItems.indexFromItem(item)
                graphics = self._scene.getNextGraphics(graphics)
        self.ui.graphics_listview.setModel(self._graphicsItems)
        #self.ui.graphics_listview.setMovement(QtGui.QListView.Snap)
        #self.ui.graphics_listview.setDragDropMode(QtGui.QListView.InternalMove)
        #self.ui.graphics_listview.setDragDropOverwriteMode(False)
        #self.ui.graphics_listview.setDropIndicatorShown(True)
        if selectedIndex:
            self.ui.graphics_listview.setCurrentIndex(selectedIndex)
        self.ui.graphics_listview.show()

    def graphicsListItemClicked(self, modelIndex):
        '''
        Either changes visibility flag or selects current graphics
        '''
        model = modelIndex.model()
        item = model.item(modelIndex.row())
        graphics = item.data()
        visibilityFlag = item.checkState() == QtCore.Qt.Checked
        graphics.setVisibilityFlag(visibilityFlag)
        selectedModelIndex = self.ui.graphics_listview.currentIndex()
        selectedItem = model.item(selectedModelIndex.row())
        selectedGraphics = selectedItem.data()
        if graphics == selectedGraphics:
            self.ui.graphics_editor.setGraphics(selectedGraphics)

    def addGraphicsEntered(self, name):
        '''
        Add a new chosen graphics type
        '''
        if not self._scene:
            return
        graphicsType = Graphics.TYPE_INVALID
        fieldDomainType = Field.DOMAIN_TYPE_INVALID
        if name == "point":
            graphicsType = Graphics.TYPE_POINTS
            fieldDomainType = Field.DOMAIN_TYPE_POINT
        elif name == "node points":
            graphicsType = Graphics.TYPE_POINTS
            fieldDomainType = Field.DOMAIN_TYPE_NODES
        elif name == "data points":
            graphicsType = Graphics.TYPE_POINTS
            fieldDomainType = Field.DOMAIN_TYPE_DATAPOINTS
        elif name == "element points":
            graphicsType = Graphics.TYPE_POINTS
            fieldDomainType = Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION
        elif name == "lines":
            graphicsType = Graphics.TYPE_LINES
        elif name == "surfaces":
            graphicsType = Graphics.TYPE_SURFACES
        elif name == "contours":
            graphicsType = Graphics.TYPE_CONTOURS
        elif name == "streamlines":
            graphicsType = Graphics.TYPE_STREAMLINES
        else:
            pass
        if graphicsType != Graphics.TYPE_INVALID:
            self._scene.beginChange()
            graphics = self._scene.createGraphics(graphicsType)
            if fieldDomainType != Field.DOMAIN_TYPE_INVALID:
                graphics.setFieldDomainType(fieldDomainType)
            if fieldDomainType != Field.DOMAIN_TYPE_POINT:
                coordinateField = self._getDefaultCoordinateField()
                if coordinateField is not None:
                    graphics.setCoordinateField(coordinateField)
            self._scene.endChange()
            self.ui.graphics_editor.setGraphics(graphics)
            self._buildGraphicsList()
        self.ui.add_graphics_combobox.setCurrentIndex(0)

    def deleteGraphicsClicked(self):
        '''
        Add a new chosen graphics type
        '''
        if not self._scene:
            return
        graphics = self.ui.graphics_editor.getGraphics()
        if graphics:
            nextGraphics = self._scene.getNextGraphics(graphics)
            if not (nextGraphics and nextGraphics.isValid()):
                nextGraphics = self._scene.getPreviousGraphics(graphics)
            if not (nextGraphics and nextGraphics.isValid()):
                nextGraphics = self._scene.getFirstGraphics()
            self.ui.graphics_editor.setGraphics(nextGraphics)
            self._scene.removeGraphics(graphics)
            self._buildGraphicsList()
