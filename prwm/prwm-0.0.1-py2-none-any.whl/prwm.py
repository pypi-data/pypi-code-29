import struct
from enum import Enum

from .common import Endianness, get_struct_endianness, get_prwm_endianness

UINT16_MAX = 2 ** 16 - 1
PRWM_MAX = 16777215

FLOAT32_ENCODING_TYPE = 1 # Look https://github.com/kchapelier/PRWM/blob/master/specifications/prwm.md#encoding-type

class Cardinality(Enum):
    __order__ = 'scalar vector2 vector3 vector4'
    scalar = 0
    vector2 = 1
    vector3 = 2
    vector4 = 3

class PRWM(object):
    version = 1
    is_indexed = True

    def __init__(self):
        self.points = iter(())
        self.cells = iter(())

    def from_vtk_polydata(self, polydata):
        self.points = tuple((
            polydata.GetPoint(i)
            for i in xrange(polydata.GetNumberOfPoints())
        ))
        self.cells = tuple((
            tuple(
                cell.GetPointId(iPoint)
                for iPoint in range(cell.GetNumberOfPoints())
            )[:3]
            for cell in (
                polydata.GetCell(iCell)
                for iCell in xrange(polydata.GetNumberOfCells())
            )
            # FIXME:
            # Trying to filter out curve.
            # Must be filtered under [count:] because cell for curve might has 3 points inside
            if cell.GetNumberOfPoints() == 3
        ))
        # TODO: colors or any attributes?

    def from_data(self, points, cells):
        self.points = points
        self.cells = cells

    def to_bytes(self, endianness=Endianness.littleEndian):
        ''' Return PRWM v1 binary data: https://github.com/kchapelier/PRWM/blob/master/specifications/prwm.md '''
        indices_count = len(self.cells) * 3
        max_index_value = max((
            iPoint
            for cell in self.cells
            for iPoint in cell
        ))
        assert 0 <= max_index_value <= PRWM_MAX
        is_indices_16bit = max_index_value <= UINT16_MAX
        header = _get_header(
            self.version,
            self.is_indexed,
            endianness,
            attributes_count=1,
            attribute_values_count=len(self.points),
            indices_count=indices_count,
            is_indices_16bit=is_indices_16bit
        )
        positions = _get_attribute_block(
            offset=len(header),
            name='position',
            is_integer=False,
            should_be_normalized=False,
            cardinality=Cardinality.vector3,
            encoding_type=FLOAT32_ENCODING_TYPE,
            endianness=endianness,
            values=(
                coord
                for point in self.points
                for coord in point
            )
        )
        return ''.join((
            header,
            positions,
            # FIXME: Should be padded to % 4 == 0
            _get_indices_block(
                endianness=endianness,
                is_16bit=is_indices_16bit,
                values=(
                    iPoint
                    for cell in self.cells
                    for iPoint in cell
                )
            )
        ))

def _pack_to_3bytes(value, endianness):
    res = struct.pack(get_struct_endianness(endianness) + 'I', value)
    if endianness == Endianness.littleEndian:
        return res[:-1]
    assert endianness == Endianness.bigEndian
    return res[1:]

#pylint: disable=too-many-arguments
def _get_header(version, is_indexed, endianness, attributes_count, attribute_values_count, indices_count, is_indices_16bit):
    assert 0 < version <= 255
    assert 0 < attributes_count <= 31
    assert 0 < attribute_values_count <= PRWM_MAX
    assert 0 < indices_count <= PRWM_MAX

    indices_type = 0 if is_indices_16bit else 1

    second_byte = (
        int(is_indexed) << 7 |
        indices_type << 6 |
        get_prwm_endianness(endianness) << 5 |
        attributes_count
    )

    return (
        struct.pack(
            'BB',
            version,
            second_byte
        ) +
        _pack_to_3bytes(attribute_values_count, endianness) +
        _pack_to_3bytes(indices_count, endianness)
    )

def _get_attribute_block(offset, name, is_integer, should_be_normalized, cardinality, encoding_type, endianness, values):
    # should_be_normalized represents 'normalized' of WebGLRenderingContect::vertexAttribPointer:
    #   - If true, signed integers are normalized to [-1, 1].
    #   - If true, unsigned integers are normalized to [0, 1].
    return ''.join([
        name,
        '\0',
        struct.pack(
            'B',
            int(is_integer) << 7 |
            int(should_be_normalized) << 6 |
            cardinality.value << 4 |
            encoding_type
        ),
        '\0' * (4 - ((len(name) + 1) + 1 + offset) % 4),
        ''.join((
            struct.pack(
                # FIXME: the type should be related to encoding_type
                get_struct_endianness(endianness) + 'I' if is_integer else 'f',
                v
            )
            for v in values
        ))
    ])

def _get_indices_block(endianness, values, is_16bit):
    return ''.join((
        struct.pack(get_struct_endianness(endianness) + 'H' if is_16bit else 'I', v)
        for v in values
    ))
