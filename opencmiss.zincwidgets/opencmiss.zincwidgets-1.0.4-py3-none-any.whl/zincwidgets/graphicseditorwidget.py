"""
Zinc Graphics Editor Widget

Allows the members of a Zinc Graphics object to be edited in Qt on Python.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

from numbers import Number

from opencmiss.zincwidgets.graphicseditorwidget_ui import Ui_GraphicsEditorWidget
from opencmiss.zinc.field import Field
from opencmiss.zinc.element import Element
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics, GraphicsStreamlines, Graphicslineattributes
from opencmiss.zinc.material import Material
from opencmiss.zinc.spectrum import Spectrum
from opencmiss.zinc.status import OK as ZINC_OK

def FieldIsRealValued(field):
    '''
    Conditional function returning true if the field has real values
    '''
    return field.getValueType() == Field.VALUE_TYPE_REAL

def FieldIsScalar(field):
    '''
    Conditional function returning true if the field is real with 1 component
    '''
    return (field.getValueType() == Field.VALUE_TYPE_REAL) and \
           (field.getNumberOfComponents() == 1)

def FieldIsCoordinateCapable(field):
    '''
    Conditional function returning true if the field can be used as a coordinate
    field, i.e. is real valued with up to 3 component
    '''
    return (field.getValueType() == Field.VALUE_TYPE_REAL) and \
           (field.getNumberOfComponents() <= 3)

def FieldIsOrientationScaleCapable(field):
    '''
    Conditional function returning true if the field can be used to orient or scale
    glyphs. Generally, this means it has 1,2,3,4,6 or 9 components, where:
    1 = scalar (no vector, isotropic scaling).
    2 = 1 2-D vector (2nd axis is normal in plane, 3rd is out of 2-D plane);
    3 = 1 3-D vector (orthogonal 2nd and 3rd axes are arbitrarily chosen);
    4 = 2 2-D vectors (3rd axis taken as out of 2-D plane);
    6 = 2 3-D vectors (3rd axis found from cross product);
    9 = 3 3-D vectors = complete definition of 3 axes.
    '''
    return (field.getValueType() == Field.VALUE_TYPE_REAL) and \
           (field.getNumberOfComponents() in [1,2,3,4,6,9])

def FieldIsStreamVectorCapable(field):
    '''
    Conditional function returning true if the field can be used as a
    streamline stream vector field.
    For a 3-D domain with a 3-D coordinate field, can have 3, 6 or 9 components;
    extra components set the lateral axes for extruded profiles.
    For a 2-D domain the stream vector may have 2 components.
    '''
    return (field.getValueType() == Field.VALUE_TYPE_REAL) and \
           (field.getNumberOfComponents() in [2,3,6,9])


class GraphicsEditorWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        '''
        Call the super class init functions
        '''
        QtGui.QWidget.__init__(self, parent)
        self._graphics = None
        # Using composition to include the visual element of the GUI.
        self.ui = Ui_GraphicsEditorWidget()
        self.ui.setupUi(self)
        # base graphics attributes
        self.ui.data_field_chooser.setNullObjectName('-')
        self.ui.coordinate_field_chooser.setNullObjectName('-')
        self.ui.coordinate_field_chooser.setConditional(FieldIsCoordinateCapable)
        # contours
        self.ui.isoscalar_field_chooser.setNullObjectName('- choose -')
        self.ui.isoscalar_field_chooser.setConditional(FieldIsScalar)
        # streamlines
        self.ui.stream_vector_field_chooser.setNullObjectName('- choose -')
        self.ui.stream_vector_field_chooser.setConditional(FieldIsStreamVectorCapable)
        # line attributes
        self.ui.line_orientation_scale_field_chooser.setNullObjectName('-')
        self.ui.line_orientation_scale_field_chooser.setConditional( FieldIsScalar)
        # point attributes
        self.ui.glyph_chooser.setNullObjectName('-')
        self.ui.point_orientation_scale_field_chooser.setNullObjectName('-')
        self.ui.point_orientation_scale_field_chooser.setConditional( FieldIsOrientationScaleCapable)
        self.ui.label_field_chooser.setNullObjectName('-')
        self.ui.label_field_chooser.setConditional(FieldIsRealValued)

    def _updateWidgets(self):
        # base graphics attributes
        coordinateField = None
        material = None
        dataField = None
        isExterior = False
        isWireframe = False
        pointattributes = None
        lineattributes = None
        samplingattributes = None
        contours = None
        streamlines = None
        isDomain0D = True
        if self._graphics:
            coordinateField = self._graphics.getCoordinateField()
            material = self._graphics.getMaterial()
            dataField = self._graphics.getDataField()
            isExterior = self._graphics.isExterior()
            isWireframe = self._graphics.getRenderPolygonMode() == Graphics.RENDER_POLYGON_MODE_WIREFRAME
            contours = self._graphics.castContours()
            streamlines = self._graphics.castStreamlines()
            pointattributes = self._graphics.getGraphicspointattributes()
            lineattributes = self._graphics.getGraphicslineattributes()
            samplingattributes = self._graphics.getGraphicssamplingattributes()
            isDomain0D = self._graphics.getFieldDomainType() in \
                [Field.DOMAIN_TYPE_POINT, Field.DOMAIN_TYPE_NODES, Field.DOMAIN_TYPE_DATAPOINTS]
        self.ui.coordinate_field_chooser.setField(coordinateField)
        self.ui.material_chooser.setMaterial(material)
        self.ui.data_field_chooser.setField(dataField)
        self.ui.exterior_checkbox.setCheckState(QtCore.Qt.Checked if isExterior else QtCore.Qt.Unchecked)
        self._faceDisplay()
        self.ui.wireframe_checkbox.setCheckState(QtCore.Qt.Checked if isWireframe else QtCore.Qt.Unchecked)
        # contours
        isoscalarField = None
        if contours and contours.isValid():
            isoscalarField = contours.getIsoscalarField()
            self.ui.contours_groupbox.show()
        else:
            self.ui.contours_groupbox.hide()
        self.ui.isoscalar_field_chooser.setField(isoscalarField)
        self._isovaluesDisplay()
        # streamlines
        streamVectorField = None
        if streamlines and streamlines.isValid():
            streamVectorField = streamlines.getStreamVectorField()
            self.ui.streamlines_groupbox.show()
        else:
            self.ui.streamlines_groupbox.hide()
        self.ui.stream_vector_field_chooser.setField(streamVectorField)
        self._streamlinesTrackLengthDisplay()
        self._streamlinesTrackDirectionDisplay()
        self._streamlinesColourDataTypeDisplay()
        # line attributes
        lineOrientationScaleField = None
        if lineattributes and lineattributes.isValid():
            lineOrientationScaleField = lineattributes.getOrientationScaleField()
            self.ui.lines_groupbox.show()
        else:
            self.ui.lines_groupbox.hide()
        self._lineShapeDisplay()
        self._lineBaseSizeDisplay()
        self.ui.line_orientation_scale_field_chooser.setField(lineOrientationScaleField)
        self._lineScaleFactorsDisplay()
        isStreamline = (streamlines is not None) and streamlines.isValid()
        if not isStreamline:
            isStreamline = False
        model = self.ui.line_shape_combobox.model()
        model.item(1, 0).setEnabled(isStreamline)
        model.item(3, 0).setEnabled(isStreamline)
        self.ui.line_orientation_scale_field_label.setEnabled(not isStreamline)
        self.ui.line_orientation_scale_field_chooser.setEnabled(not isStreamline)
        self.ui.line_scale_factors_label.setEnabled(not isStreamline)
        self.ui.line_scale_factors_lineedit.setEnabled(not isStreamline)
        # point attributes
        glyph = None
        pointOrientationScaleField = None
        labelField = None
        if pointattributes and pointattributes.isValid():
            glyph = pointattributes.getGlyph()
            pointOrientationScaleField = pointattributes.getOrientationScaleField()
            labelField = pointattributes.getLabelField()
            self.ui.points_groupbox.show()
        else:
            self.ui.points_groupbox.hide()
        self.ui.glyph_chooser.setGlyph(glyph)
        self._pointBaseSizeDisplay()
        self.ui.point_orientation_scale_field_chooser.setField(pointOrientationScaleField)
        self._pointScaleFactorsDisplay()
        self.ui.label_field_chooser.setField(labelField)
        # sampling attributes
        if samplingattributes and samplingattributes.isValid() and not isDomain0D:
            self.ui.sampling_groupbox.show()
        else:
            self.ui.sampling_groupbox.hide()
        self._samplingModeDisplay()
        self._samplingDivisionsDisplay()

    def setScene(self, scene):
        '''
        Set when scene changes to initialised widgets dependent on scene
        '''
        self.ui.material_chooser.setMaterialmodule(scene.getMaterialmodule())
        self.ui.glyph_chooser.setGlyphmodule(scene.getGlyphmodule())
        region = scene.getRegion()
        self.ui.coordinate_field_chooser.setRegion(region)
        self.ui.data_field_chooser.setRegion(region)
        self.ui.isoscalar_field_chooser.setRegion(region)
        self.ui.stream_vector_field_chooser.setRegion(region)
        self.ui.point_orientation_scale_field_chooser.setRegion(region)
        self.ui.label_field_chooser.setRegion(region)
        self.ui.line_orientation_scale_field_chooser.setRegion(region)

    def getGraphics(self):
        '''
        Get the graphics currently in the editor
        '''
        return self._graphics

    def setGraphics(self, graphics):
        '''
        Set the graphics to be edited
        '''
        if not (graphics and graphics.isValid()):
            self._graphics = None
        else:
            self._graphics = graphics
        self._updateWidgets()
 
    def _displayReal(self, widget, value):
        '''
        Display real value in a widget
        '''
        newText = '{:.5g}'.format(value)
        widget.setText(newText)
 
    def _displayScale(self, widget, values, numberFormat = '{:.5g}'):
        '''
        Display vector values in a widget, separated by '*'
        '''
        newText = "*".join(numberFormat.format(value) for value in values)
        widget.setText(newText)

    def _parseScale(self, widget):
        '''
        Return real vector from comma separated text in line edit widget
        '''
        text = widget.text()
        values = [float(value) for value in text.split('*')]
        return values

    def _parseScaleInteger(self, widget):
        '''
        Return integer vector from comma separated text in line edit widget
        '''
        text = widget.text()
        values = [int(value) for value in text.split('*')]
        return values

    def _displayVector(self, widget, values, numberFormat = '{:.5g}'):
        '''
        Display real vector values in a widget. Also handle scalar
        '''
        if isinstance(values, Number):
            newText = str('{:.5g}'.format(values))
        else:
            newText = ", ".join(numberFormat.format(value) for value in values)
        widget.setText(newText)

    def _parseVector(self, widget):
        '''
        Return real vector from comma separated text in line edit widget
        '''
        text = widget.text()
        values = [float(value) for value in text.split(',')]
        return values

    def coordinateFieldChanged(self, index):
        '''
        An item was selected at index in coordinate field chooser widget
        '''
        if self._graphics:
            coordinateField = self.ui.coordinate_field_chooser.getField()
            if coordinateField:
                self._graphics.setCoordinateField(coordinateField)
            else:
                self._graphics.setCoordinateField(Field())

    def dataFieldChanged(self, index):
        '''
        An item was selected at index in data field chooser widget
        '''
        if self._graphics:
            dataField = self.ui.data_field_chooser.getField()
            if dataField:
                scene = self._graphics.getScene()
                scene.beginChange()
                spectrum = self._graphics.getSpectrum()
                if not spectrum.isValid():
                    spectrummodule = scene.getSpectrummodule()
                    spectrum = spectrummodule.getDefaultSpectrum()
                    self._graphics.setSpectrum(spectrum)
                self._graphics.setDataField(dataField)
                scene.endChange()
            else:
                self._graphics.setDataField(Field())

    def exteriorClicked(self, isChecked):
        '''
        The exterior radiobutton was clicked
        '''
        if self._graphics:
            self._graphics.setExterior(isChecked)

    def _faceDisplay(self):
        '''
        Show the current state of the face combo box
        '''
        faceType = Element.FACE_TYPE_ALL
        if self._graphics:
            faceType = self._graphics.getElementFaceType()
        self.ui.face_combobox.blockSignals(True)
        self.ui.face_combobox.setCurrentIndex(faceType - Element.FACE_TYPE_ALL)
        self.ui.face_combobox.blockSignals(False)

    def faceChanged(self, index):
        '''
        Element face combo box changed
        '''
        if self._graphics:
            self._graphics.setElementFaceType(index + Element.FACE_TYPE_ALL)

    def wireframeClicked(self, isChecked):
        '''
        The wireframe surface render radiobutton was clicked
        '''
        if self._graphics:
            self._graphics.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_WIREFRAME if isChecked else Graphics.RENDER_POLYGON_MODE_SHADED)

    def glyphChanged(self, index):
        '''
        An item was selected at index in glyph chooser widget
        '''
        if self._graphics:
            pointattributes = self._graphics.getGraphicspointattributes()
            if (pointattributes.isValid()):
                glyph = self.ui.glyph_chooser.getGlyph()
                if glyph:
                    pointattributes.setGlyph(glyph)
                else:
                    pointattributes.setGlyph(Glyph())

    def materialChanged(self, index):
        '''
        An item was selected at index in material chooser widget
        '''
        if self._graphics:
            material = self.ui.material_chooser.getMaterial()
            self._graphics.setMaterial(material)
       
    def isoscalarFieldChanged(self, index):
        if self._graphics:
            contours = self._graphics.castContours()
            if contours.isValid():
                isoscalarField = self.ui.isoscalar_field_chooser.getField()
                if not isoscalarField:
                    isoscalarField = Field()
                contours.setIsoscalarField(isoscalarField)

    def _isovaluesDisplay(self):
        '''
        Display the current iso values list
        '''
        if self._graphics:
            contours = self._graphics.castContours()
            if contours.isValid():
                count, isovalues = contours.getListIsovalues(1)
                if count > 1:
                    count, isovalues = contours.getListIsovalues(count)
                if count > 0:
                    self._displayVector(self.ui.isovalues_lineedit, isovalues)
                    return
        self.ui.isovalues_lineedit.setText('')

    def isovaluesEntered(self):
        '''
        Set iso values list from text in widget
        '''
        try:
            isovalues = self._parseVector(self.ui.isovalues_lineedit)
            contours = self._graphics.castContours()
            if contours.isValid():
                if contours.setListIsovalues(isovalues) != ZINC_OK:
                    raise
        except:
            print("Invalid isovalues")
        self._isovaluesDisplay()
      
    def streamVectorFieldChanged(self, index):
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                streamVectorField = self.ui.stream_vector_field_chooser.getField()
                if not streamVectorField:
                    streamVectorField = Field()
                streamlines.setStreamVectorField(streamVectorField)

    def _streamlinesTrackLengthDisplay(self):
        '''
        Display the current streamlines length
        '''
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                trackLength = streamlines.getTrackLength()
                self._displayReal(self.ui.streamlines_track_length_lineedit, trackLength)
                return
        self.ui.streamlines_track_length_lineedit.setText('')

    def streamlinesTrackLengthEntered(self):
        '''
        Set iso values list from text in widget
        '''
        streamlinesLengthText = self.ui.streamlines_track_length_lineedit.text()
        try:
            trackLength = float(streamlinesLengthText)
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                if streamlines.setTrackLength(trackLength) != ZINC_OK:
                    raise
        except:
            print("Invalid streamlines track length", streamlinesLengthText)
        self._streamlinesTrackLengthDisplay()

    def _streamlinesTrackDirectionDisplay(self):
        '''
        Show the current state of the streamlines track direction combo box
        '''
        streamlinesTrackDirection = GraphicsStreamlines.TRACK_DIRECTION_FORWARD
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                streamlinesTrackDirection = streamlines.getTrackDirection()
        self.ui.streamlines_track_direction_combobox.blockSignals(True)
        self.ui.streamlines_track_direction_combobox.setCurrentIndex(streamlinesTrackDirection - GraphicsStreamlines.TRACK_DIRECTION_FORWARD)
        self.ui.streamlines_track_direction_combobox.blockSignals(False)

    def streamlinesTrackDirectionChanged(self, index):
        '''
        Element streamlines track direction combo box changed
        '''
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                streamlines.setTrackDirection(index + GraphicsStreamlines.TRACK_DIRECTION_FORWARD)

    def _streamlinesColourDataTypeDisplay(self):
        '''
        Show the current state of the streamlines colour data type combo box
        '''
        streamlinesColourDataType = GraphicsStreamlines.COLOUR_DATA_TYPE_FIELD
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                streamlinesColourDataType = streamlines.getColourDataType()
        self.ui.streamlines_colour_data_type_combobox.blockSignals(True)
        self.ui.streamlines_colour_data_type_combobox.setCurrentIndex(streamlinesColourDataType - GraphicsStreamlines.COLOUR_DATA_TYPE_FIELD)
        self.ui.streamlines_colour_data_type_combobox.blockSignals(False)

    def streamlinesColourDataTypeChanged(self, index):
        '''
        Element streamlines colour data type combo box changed
        '''
        if self._graphics:
            streamlines = self._graphics.castStreamlines()
            if streamlines.isValid():
                scene = self._graphics.getScene()
                scene.beginChange()
                spectrum = self._graphics.getSpectrum()
                if not spectrum.isValid():
                    spectrummodule = scene.getSpectrummodule()
                    spectrum = spectrummodule.getDefaultSpectrum()
                    self._graphics.setSpectrum(spectrum)
                streamlines.setColourDataType(index + GraphicsStreamlines.COLOUR_DATA_TYPE_FIELD)
                scene.endChange()

    def _lineShapeDisplay(self):
        '''
        Show the current state of the lineShape combo box
        '''
        lineShapeType = Graphicslineattributes.SHAPE_TYPE_LINE
        if self._graphics:
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.isValid():
                lineShapeType = lineattributes.getShapeType()
        self.ui.line_shape_combobox.blockSignals(True)
        self.ui.line_shape_combobox.setCurrentIndex(lineShapeType - Graphicslineattributes.SHAPE_TYPE_LINE)
        self.ui.line_shape_combobox.blockSignals(False)

    def lineShapeChanged(self, index):
        '''
        Element lineShape combo box changed
        '''
        if self._graphics:
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.isValid():
                lineattributes.setShapeType(index + Graphicslineattributes.SHAPE_TYPE_LINE)

    def _lineBaseSizeDisplay(self):
        '''
        Display the current line base size
        '''
        if self._graphics:
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.isValid():
                result, baseSize = lineattributes.getBaseSize(2)
                self._displayScale(self.ui.line_base_size_lineedit, baseSize)
                return
        self.ui.line_base_size_lineedit.setText('0')

    def lineBaseSizeEntered(self):
        '''
        Set line base size from text in widget
        '''
        try:
            baseSize = self._parseScale(self.ui.line_base_size_lineedit)
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.setBaseSize(baseSize) != ZINC_OK:
                raise
        except:
            print("Invalid line base size")
        self._lineBaseSizeDisplay()

    def lineOrientationScaleFieldChanged(self, index):
        if self._graphics:
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.isValid():
                orientationScaleField = self.ui.line_orientation_scale_field_chooser.getField()
                if not orientationScaleField:
                    orientationScaleField = Field()
                lineattributes.setOrientationScaleField(orientationScaleField)

    def _lineScaleFactorsDisplay(self):
        '''
        Display the current line scale factors
        '''
        if self._graphics:
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.isValid():
                result, scaleFactors = lineattributes.getScaleFactors(2)
                self._displayScale(self.ui.line_scale_factors_lineedit, scaleFactors)
                return
        self.ui.line_scale_factors_lineedit.setText('0')

    def lineScaleFactorsEntered(self):
        '''
        Set line scale factors from text in widget
        '''
        try:
            scaleFactors = self._parseScale(self.ui.line_scale_factors_lineedit)
            lineattributes = self._graphics.getGraphicslineattributes()
            if lineattributes.setScaleFactors(scaleFactors) != ZINC_OK:
                raise
        except:
            print("Invalid line scale factors")
        self._lineScaleFactorsDisplay()

    def _pointBaseSizeDisplay(self):
        '''
        Display the current point base size
        '''
        if self._graphics:
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.isValid():
                result, baseSize = pointattributes.getBaseSize(3)
                self._displayScale(self.ui.point_base_size_lineedit, baseSize)
                return
        self.ui.point_base_size_lineedit.setText('0')

    def pointBaseSizeEntered(self):
        '''
        Set point base size from text in widget
        '''
        try:
            baseSize = self._parseScale(self.ui.point_base_size_lineedit)
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.setBaseSize(baseSize) != ZINC_OK:
                raise
        except:
            print("Invalid point base size")
        self._pointBaseSizeDisplay()

    def pointOrientationScaleFieldChanged(self, index):
        if self._graphics:
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.isValid():
                orientationScaleField = self.ui.point_orientation_scale_field_chooser.getField()
                if not orientationScaleField:
                    orientationScaleField = Field()
                pointattributes.setOrientationScaleField(orientationScaleField)

    def _pointScaleFactorsDisplay(self):
        '''
        Display the current point scale factors
        '''
        if self._graphics:
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.isValid():
                result, scaleFactors = pointattributes.getScaleFactors(3)
                self._displayScale(self.ui.point_scale_factors_lineedit, scaleFactors)
                return
        self.ui.point_scale_factors_lineedit.setText('0')

    def pointScaleFactorsEntered(self):
        '''
        Set point scale factors from text in widget
        '''
        try:
            scaleFactors = self._parseScale(self.ui.point_scale_factors_lineedit)
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.setScaleFactors(scaleFactors) != ZINC_OK:
                raise
        except:
            print("Invalid point scale factors")
        self._pointScaleFactorsDisplay()
       
    def labelFieldChanged(self, index):
        if self._graphics:
            pointattributes = self._graphics.getGraphicspointattributes()
            if pointattributes.isValid():
                labelField = self.ui.label_field_chooser.getField()
                if not labelField:
                    labelField = Field()
                pointattributes.setLabelField(labelField)

    def _samplingModeDisplay(self):
        '''
        Show the current state of the sampling mode combo box
        '''
        samplingMode = Element.POINT_SAMPLING_MODE_CELL_CENTRES
        if self._graphics:
            samplingattributes = self._graphics.getGraphicssamplingattributes()
            if samplingattributes.isValid():
                samplingMode = samplingattributes.getElementPointSamplingMode()
        self.ui.sampling_mode_combobox.blockSignals(True)
        self.ui.sampling_mode_combobox.setCurrentIndex(samplingMode - Element.POINT_SAMPLING_MODE_CELL_CENTRES)
        self.ui.sampling_mode_combobox.blockSignals(False)

    def samplingModeChanged(self, index):
        '''
        Sampling mode combo box changed
        '''
        if self._graphics:
            samplingattributes = self._graphics.getGraphicssamplingattributes()
            if samplingattributes.isValid():
                samplingattributes.setElementPointSamplingMode(index + Element.POINT_SAMPLING_MODE_CELL_CENTRES)

    def _samplingDivisionsDisplay(self):
        '''
        Display the current sampling divisions
        '''
        if self._graphics:
            tessellation = self._graphics.getTessellation()
            result, samplingDivisions = tessellation.getMinimumDivisions(3)
            self._displayScale(self.ui.sampling_divisions_lineedit, samplingDivisions, '{:d}')
            return
        self.ui.sampling_divisions_lineedit.setText('')

    def samplingDivisionsEntered(self):
        '''
        Set sampling base size from text in widget
        '''
        try:
            samplingDivisions = self._parseScaleInteger(self.ui.sampling_divisions_lineedit)
            tessellation = self._graphics.getTessellation()
            result, oldSamplingDivisions = tessellation.getMinimumDivisions(3)
            # only set if different from current values
            divisions = 0
            for i in range(3):
                if i < len(samplingDivisions):
                    divisions = samplingDivisions[i]
                if divisions != oldSamplingDivisions[i]:
                    scene = self._graphics.getScene()
                    tessellationmodule = scene.getTessellationmodule()
                    if all((i == 1) for i in samplingDivisions):
                        tessellation = tessellationmodule.getDefaultPointsTessellation()
                    else:
                        tessellation = tessellationmodule.createTessellation()
                        if ZINC_OK != tessellation.setMinimumDivisions(samplingDivisions):
                            raise
                    self._graphics.setTessellation(tessellation)
                    break
        except:
            print("Invalid sampling divisions")
        self._samplingDivisionsDisplay()
