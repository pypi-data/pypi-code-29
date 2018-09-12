#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys


__all__ = ['Size', 'Piece', 'Region', 'solve', 'LocationNotFoundError']


class Size(object):
    '''The Size class encapsulates the width and height of a component in a single object.'''
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height


class Piece(object):
    '''This class represents input information.'''
    def __init__(self, uid, size):
        self._uid = uid
        self._size = size

    @property
    def uid(self):
        return self._uid

    @property
    def size(self):
        return self._size


class StablePoint(object):
    '''This class represents a BL stable point.'''
    def __init__(self, x=0, y=0, gap_width=0, gap_height=0):
        self._x = x
        self._y = y
        self._gap_width = gap_width
        self._gap_height = gap_height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def gap_width(self):
        return self._gap_width

    @property
    def gap_height(self):
        return self._gap_height


class Region(object):
    '''This class represents a rectangle in an integer coordinate system.'''
    def __init__(self, uid, top, right, bottom, left):
        self._uid = uid
        self._top = top
        self._right = right
        self._bottom = bottom
        self._left = left

    @property
    def uid(self):
        return self._uid

    @property
    def top(self):
        return self._top

    @property
    def right(self):
        return self._right

    @property
    def bottom(self):
        return self._bottom

    @property
    def left(self):
        return self._left

    @property
    def width(self):
        return self._right - self._left

    @property
    def height(self):
        return self._top - self._bottom

    @property
    def area(self):
        return self.width * self.height

    @classmethod
    def from_position_and_size(cls, uid, x, y, width, height):
        return cls(uid=uid, top=y + height, right=x + width, bottom=y, left=x)


class LocationNotFoundError(Exception):
    '''Raised when a location is not found.'''
    pass


def is_colliding(stable_point, current_size, other_regions):
    '''Whether the rectangle on the stable point is in collide with another rectangles.

    Args:
        stable_point (:class:`StablePoint`):
        current_size (:class:`Size`):
        other_regions (list(:class:`Region`)):

    Returns:
        True if colliding, False otherwise.
    '''
    for other_region in other_regions:
        if stable_point.x >= other_region.right:
            continue
        if (stable_point.x + current_size.width) <= other_region.left:
            continue
        if stable_point.y >= other_region.top:
            continue
        if (stable_point.y + current_size.height) <= other_region.bottom:
            continue

        return True

    return False


def find_point_index(
    stable_points,
    current_size,
    other_regions,
    container_width
):
    '''Find a BL point index.'''
    min_x, min_y = sys.maxsize, sys.maxsize
    last_used_id = None

    for i, point in enumerate(stable_points):
        if (current_size.width <= point.gap_width) or (current_size.height <= point.gap_height):
            continue

        if (point.x < 0) or (point.y < 0) or (point.x + current_size.width > container_width):
            continue

        if is_colliding(stable_point=point, current_size=current_size, other_regions=other_regions):
            continue

        # Update the location.
        if (point.y < min_y) or (point.y == min_y and point.x < min_x):
            min_x = point.x
            min_y = point.y
            last_used_id = i

    if last_used_id is None:
        raise LocationNotFoundError

    return last_used_id


def generate_stable_points(current_region, other_regions):
    '''Generate stable points.'''
    stable_points = list()

    # Add a candidate for BL stable point.
    # This newly occurred by the current rectangle and the container.
    stable_points.append(
        StablePoint(x=current_region.right, y=0, gap_width=0, gap_height=current_region.bottom)
    )
    stable_points.append(
        StablePoint(x=0, y=current_region.top, gap_width=current_region.left, gap_height=0)
    )

    # Add a candidate for BL stable point.
    # This newly occurred by the current rectangle and other rectangles.
    for other_region in other_regions:
        # When the current rectangle is to the left side of the other rectangle.
        if (current_region.right <= other_region.left) and (current_region.top > other_region.top):
            x = current_region.right
            y = other_region.top
            w = other_region.left - current_region.right
            if current_region.bottom > other_region.top:
                h = current_region.bottom - other_region.top
            else:
                h = 0
            stable_points.append(StablePoint(x=x, y=y, gap_width=w, gap_height=h))
        # When the current rectangle is to the right side of the other rectangle.
        if (current_region.left >= other_region.right) and (current_region.top < other_region.top):
            x = other_region.right
            y = current_region.top
            w = current_region.left - other_region.right
            if other_region.bottom > current_region.top:
                h = other_region.bottom - current_region.top
            else:
                h = 0
            stable_points.append(StablePoint(x=x, y=y, gap_width=w, gap_height=h))
        # When the current rectangle is to the lower side of the other rectangle.
        if (current_region.top <= other_region.bottom) and (current_region.right > other_region.right):
            x = other_region.right
            y = current_region.top
            if current_region.left > other_region.right:
                w = current_region.left - other_region.right
            else:
                w = 0
            h = other_region.bottom - current_region.top
            stable_points.append(StablePoint(x=x, y=y, gap_width=w, gap_height=h))
        # When the current rectangle is to the upper side of the other rectangle.
        if (current_region.bottom >= other_region.top) and (current_region.right < other_region.right):
            x = current_region.right
            y = other_region.top
            if other_region.left > current_region.right:
                w = other_region.left - current_region.right
            else:
                w = 0
            h = current_region.bottom - other_region.top
            stable_points.append(StablePoint(x=x, y=y, gap_width=w, gap_height=h))

    return stable_points


def run(pieces, container_width):
    '''Run all iterations.

    Args:
        pieces (list(:class:`Piece`)):
        container_width (int):

    Returns:
        list(:class:`Region`)
    '''
    regions = list()
    stable_points = list()
    stable_points.append(StablePoint())

    for piece in pieces:
        current_size = piece.size
        index = find_point_index(
            stable_points=stable_points,
            current_size=current_size,
            other_regions=regions,
            container_width=container_width
        )
        point = stable_points.pop(index)

        new_region = Region.from_position_and_size(
            uid=piece.uid,
            x=point.x,
            y=point.y,
            width=current_size.width,
            height=current_size.height
        )
        new_stable_points = generate_stable_points(
            current_region=new_region,
            other_regions=regions
        )
        stable_points.extend(new_stable_points)
        regions.append(new_region)

    return regions


def next_power_of_2(x):
    return 2.0 ** math.ceil(math.log2(x))


def calc_minimum_container_size(regions):
    '''Calculate a minimum container size from rectangles.'''
    max_width, max_height = 0, 0
    for region in regions:
        if region.right > max_width:
            max_width = region.right
        if region.top > max_height:
            max_height = region.top

    return Size(max_width, max_height)


def calc_container_size(container_width, regions, enable_auto_size, force_pow2):
    '''Calculate a container size.'''
    size = calc_minimum_container_size(regions)
    if enable_auto_size:
        width, height = size.width, size.height
    else:
        width, height = container_width, size.height

    if force_pow2:
        width = int(next_power_of_2(width))
        height = int(next_power_of_2(height))

    return Size(width, height)


def calc_filling_rate(container_size, regions):
    '''Calculate a filling rate.'''
    area = sum(region.area for region in regions)
    return area / container_size.area


def solver1(pieces, container_width, options):
    '''Inputs are sorted in descending order of height before execution.'''
    pieces.sort(key=lambda piece: -piece.size.height)
    regions = run(pieces, container_width)
    container_size = calc_container_size(
        container_width=container_width,
        regions=regions,
        enable_auto_size=options['enable_auto_size'],
        force_pow2=options['force_pow2']
    )
    filling_rate = calc_filling_rate(container_size, regions)

    return filling_rate, container_size, regions


def solver2(pieces, container_width, options):
    '''Inputs are sorted in descending order of area before execution.'''
    pieces.sort(key=lambda piece: -piece.size.area)
    regions = run(pieces, container_width)
    container_size = calc_container_size(
        container_width=container_width,
        regions=regions,
        enable_auto_size=options['enable_auto_size'],
        force_pow2=options['force_pow2']
    )
    filling_rate = calc_filling_rate(container_size, regions)

    return filling_rate, container_size, regions


def solver3(pieces, container_width, options):
    '''Inputs are sorted in descending order of height and width before execution.'''
    pieces.sort(key=lambda piece: (-piece.size.height, -piece.size.width))
    regions = run(pieces, container_width)
    container_size = calc_container_size(
        container_width=container_width,
        regions=regions,
        enable_auto_size=options['enable_auto_size'],
        force_pow2=options['force_pow2']
    )
    filling_rate = calc_filling_rate(container_size, regions)

    return filling_rate, container_size, regions


def solve(
    pieces,
    container_width,
    options=None
):
    '''Obtain the highest filling rate result.

    Args:
        pieces (list(:class:`Piece`)):
        container_width (int):
        options (dict):

    Returns:
        tuple(container_width, container_height, list(:class:`Region`))
    '''
    default_options = {
        # If true, the size will be adjusted automatically.
        'enable_auto_size': True,
        # If true, the power-of-two rule is forced.
        'force_pow2': False
    }
    if options is None:
        options = default_options
    else:
        options = {key: options[key] if key in options else default_options[key] for key in default_options.keys()}

    if options['enable_auto_size']:
        max_width = max(pieces, key=lambda piece: piece.size.width).size.width
        if container_width < max_width:
            container_width = max_width

    if options['force_pow2']:
        container_width = int(next_power_of_2(container_width))

    best_filling_rate = -1.0
    result = (0, 0, None)
    for solver in (solver1, solver2, solver3):
        filling_rate, container_size, regions = solver(
            pieces=pieces,
            container_width=container_width,
            options=options
        )
        if filling_rate > best_filling_rate:
            best_filling_rate = filling_rate
            result = (container_size.width, container_size.height, regions)

    return result
