#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018 Sebastian Georg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
hight2obj

Converts a heightmap to a 3d mesh.

Usage:

hight2obj SOURCE DESTINATION SCALE

Parameters:

* SOURCE: Filename of the source hightmap. This must be a 8 bpp greyscale
          bitmap-type image. PNG is tested an recommended.
* DESTINATION: Filename of the destination file into which the 3d data is
               written.
* SCALE: Scale factor for the z-coordinate. This value is the maximum height
         of the resulting mesh relative to the short side side of the SOURCE
         image.
"""

from PIL import Image
import sys



def create_vertices(image, scale):
    """Returns a list of vertices for a given heightmap."""
    norm = min(image.size) - 1 # normalize coordinates to shortest image length
    vertices = []
    for y in range(image.height):
        for x in range(image.width):
            vertex = (x / norm, y / norm, image.getpixel((x, y)) / 255 * scale)
            vertices.append(vertex)
    return vertices

def create_faces(width, height):
    """Returns a regular mesh of a given size. triangles are defined by vertex
    indices."""
    faces = []
    for y in range(height - 1):
        for x in range(width - 1):
            offset = y * width + 1 # vertex index in obj-format starts at 1
            # relative vertex positions: [u]pper, [l]ower / [l]eft, [r]ight
            ul, ur, ll, lr = (offset + x, offset + x + 1,
                              offset + width + x, offset + width + x + 1)
            # two triangles per square: upper left and lower right
            faces.append((ul, ur, ll))
            faces.append((ll, ur, lr))
    return faces

def main():
    im = Image.open(sys.argv[1])
    outpath = sys.argv[2]
    scale = float(sys.argv[3])
    print('Image: size={}x{}, mode={}'.format(*im.size, im.mode))
    print('Polygon count: {}'.format(2 * (im.width -1) * (im.height - 1)))
    vertices = create_vertices(im, scale)
    faces = create_faces(*im.size)
    with open(outpath, 'w') as outfile:
        outfile.write('# Created by height2obj.py\n')
        for v in vertices:
            outfile.write('v {} {} {}\n'.format(*v))
        for f in faces:
            outfile.write('f {} {} {}\n'.format(*f))
            
if __name__ == '__main__':
    main()
