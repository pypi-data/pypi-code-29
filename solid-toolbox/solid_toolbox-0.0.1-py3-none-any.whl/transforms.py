from solid import *
from solid.utils import *

def noop(*args):
    def func(transform):
        return transform
    return func

def rotate_with_fake_origin(degree, axis, temp_origin):
    x, y, z = temp_origin
    def rotater(child):
        return translate((x, y, z))(
            rotate(degree, axis)(
                translate((-x, -y, -z))(
                    child,
                ),
            ),
        )
    return rotater
