from typing import NamedTuple

class Vec(NamedTuple):
    x: float
    y: float
    z: float

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.z}]'

    def __str__(self):
        return self.__repr__()

class Vec2d(NamedTuple):
    x: float
    y: float

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __str__(self):
        return self.__repr__()

Point = Vec
Point2d = Vec2d

mm = 1
cm = 10

x_axis = x_unit = Vec(1, 0, 0)
y_axis = y_unit = Vec(0, 1, 0)
z_axis = z_unit = Vec(0, 0, 1)
