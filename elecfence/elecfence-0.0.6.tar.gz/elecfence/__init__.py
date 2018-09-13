import json
from decimal import *

import geojson.utils
from geojson import Polygon


class ElecFence(object):
    def __init__(self):
        self.__fence = []

    def create(self, geojson: object):
        """

        :type geojson: object
        :param geojson:
        :return:
        """
        pass

    def inside(self, point: object):
        """

        :type point: object
        :param point:
        :return:
        """
        pass

    def outside(self, point: list):
        """

        :type point: object
        :param point:
        :return:
        """
        pass

    pass


class Point(object):
    def __init__(self, pt=None, swap=None, **kwargs):
        """

        :param pt:
        :param swap:
        :param kwargs:
        """
        self._long = None
        self._lat = None
        """
        Get pt from pt.
        """
        if pt:
            if isinstance(pt, Point):
                self._long, self._lat = pt.array()
            if isinstance(pt, str):
                self._long, self._lat = pt.split(',')
            if isinstance(pt, list):
                self._long, self._lat = pt
            if swap:
                self._long, self._lat = self._lat, self._long
        """
        Get pt from kwargs.
        """
        if self._long is None and self._lat is None:
            self._long = kwargs.get('long')
            self._lat = kwargs.get('lat')

        if self._long is None and self._lat is None:
            raise Exception('Para is error.')
        """
        Convert str to float.
        """
        # if isinstance(self._long, str):
        self._long = Decimal(self._long).quantize(Decimal('0.0000000000'))
        # if isinstance(self._lat, str):
        self._lat = Decimal(self._lat).quantize(Decimal('0.0000000000'))

    def __repr__(self):
        return '<Point:{},{}>'.format(self._long, self._lat)

    def __add__(self, other):
        long, lat = 0, 0
        if isinstance(other, Point):
            long = Point.long
            lat = Point.lat
        if isinstance(other, str):
            long, lat = other.split(',')
        if isinstance(other, list):
            long, lat = other
        if long is None and lat is None:
            raise Exception('Point adder is error.')
        return Point(long=self._long + long, lat=self._lat + lat)

    @property
    def long(self):
        return self._long

    @property
    def lat(self):
        return self._lat

    @property
    def x(self):
        return self._long

    @property
    def y(self):
        return self._lat

    def array(self, swap=None):
        return [self._lat, self._long] if swap else [self._long, self._lat]

    def goejson(self):
        from geojson import Point
        return Point((float(self._long), float(self._lat)))


class Line(object):
    def __init__(self, start: Point, end: Point):
        """

        :type start: Point
        :type end: Point
        """
        self._start = start
        self._end = end
        self._point = []
        x1, y1 = self._start.array()
        x2, y2 = self._end.array()
        self._k = (y2 - y1) / (x2 - x1)
        self._b = y1 - x1 * self._k
        # self._k = self._k.quantize(Decimal('0.00000'))
        # self._b = self._b.quantize(Decimal('0.00000'))

    def __repr__(self):
        return '<Line:y={}*x+{}>'.format(self.k, self.b)

    @property
    def points(self):
        return self._point

    @property
    def k(self):
        return self._k

    @property
    def b(self):
        return self._b

    def calc_x(self, y):
        return (self._b - y) / self._k

    def calc_y(self, x):
        return self._k * x + self._b

    def in_line(self, point):
        x, y = Point(point).array()
        y_calc = self.calc_y(x)
        inline = (y.quantize(Decimal('0.00000')) == y_calc.quantize(Decimal('0.00000')))

        return inline

    def cross(self, line):
        """
        :type line: Line
        """
        for pt in line.points:
            if self.in_line(pt):
                return None
        for pt in self.points:
            if line.in_line(pt):
                return None
        k1, b1 = self._k, self._b
        k2, b2 = line.k, line.b
        x = (b2 - b1) / (k1 - k2)
        y = self.calc_y(x)
        cross = self.in_line([x, y]) and line.in_line([x, y])
        return Point([x, y]) if cross else None


class HalfLine(Line):
    def __init__(self, start: Point, end: Point = None):
        if end is None:
            end = Point('0,0')
        super().__init__(start, end)
        self._direction = (end.x - start.x) / abs(end.x - start.x)
        self._point.append(start.array())

    def in_line(self, pt):
        x0, y0 = Point(pt).array()
        y_calc = self.calc_y(x0)
        inline = (y0.quantize(Decimal('0.00000')) == y_calc.quantize(Decimal('0.00000')))

        if inline:
            inline = True
            pass

        x1, y1 = self._point[0]

        if self._direction > 0:
            inline = inline and (x0 > x1)
        else:
            inline = inline and (x0 < x1)
        return inline


class LineSegment(Line):
    def __init__(self, start: Point, end: Point):
        super().__init__(start, end)
        self._point.append(start.array())
        self._point.append(end.array())

    def in_line(self, pt):
        x, y = Point(pt).array()
        y_calc = self.calc_y(x)
        inline = (y.quantize(Decimal('0.00000')) == y_calc.quantize(Decimal('0.00000')))

        x1, y1 = self._point[0]
        x2, y2 = self._point[-1]

        if x1 and x2 and x1 > x2:
            x2, x1 = x1, x2

        inline = inline and (x >= x1) and (x <= x2)

        return inline


class Area(object):
    def __init__(self, area):
        self._area = list()
        # self._points = list()
        # self._lines = list()
        areas = None
        if isinstance(area, Polygon):
            areas = area['coordinates']
        if isinstance(area, str):
            area_json = json.loads(area)
            areas = area_json['coordinates']
        if isinstance(area, list):
            areas = area
        if areas is None:
            raise Exception('type error')
        self._gener_line(areas)

    def _gener_line(self, areas):
        for area in areas:
            _points = [Point(pt) for pt in area]
            _lines = list()
            first_pt = None
            last_pt = None
            for pt in _points:
                if not first_pt:
                    first_pt = pt
                if last_pt:
                    line_temp = LineSegment(last_pt, pt)
                    _lines.append(line_temp)
                last_pt = pt
            line_temp = LineSegment(last_pt, first_pt)
            _lines.append(line_temp)
            self._area.append({
                'points': _points,
                'lines': _lines
            })

    def in_area(self, pt: Point):
        _inside_count = 0
        for pt_end in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            line_temp = HalfLine(pt, pt + pt_end)
            _cross_count = 0
            for area in self._area:
                for _line in area['lines']:
                    _cross_point = _line.cross(line_temp)
                    if _cross_point is not None:
                        _cross_count += 1
                    # print(lc)
            if _cross_count % 2 == 0:
                pass
            else:
                _inside_count += 1
        if _inside_count == 0:
            return 0
        elif _inside_count == 4:
            return 1
        else:
            return 2
        pass

    def to_geojson(self):
        from geojson import Polygon
        point = [[(float(x._long), float(x._lat)) for x in area['points']] for area in self._area]
        return Polygon(point)


if __name__ == '__main__':
    pol_json_random = geojson.utils.generate_random('Polygon')
    pol = geojson.dumps(pol_json_random)
    print(pol)
    pol_json = geojson.loads(pol)

    pts = [
        Point('10.21,20.1'),
        Point('21.17,31.8'),
        Point('15.26,42.3'),
        Point('-12.6,31.1'),
        Point('-23.4,10.2'),
        Point('-11.7,-15.3'),
        Point('1.25,-19.65'),
        Point('5.65,-3.72'),
        Point('7.65,11.85'),
    ]
    pts1 = [
        '10.21,20.1',
        '21.17,31.8',
        '15.26,42.3',
        '-12.6,31.1',
        '-23.4,10.2',
        '-11.7,-15.3',
        '1.25,-19.65',
        '5.65,-3.72',
        '7.65,11.85',
    ]
    pt = [(float(x._long), float(x._lat)) for x in pts]
    a1 = Area(Polygon(pt))
    a = Area(pts1)
    # print(area.goejson())
    p = Point('7.651,11.85')
    # print(p.goejson())
    p_in = a.in_area(p)
    p1_in = a1.in_area(p)
    if p_in == -1:
        print('point outside')
    elif p_in == 1:
        print('point inside')
    else:
        print('point online')
    if p1_in == -1:
        print('point 1 outside')
    elif p1_in == 1:
        print('point 1 inside')
    else:
        print('point 1 online')
    pass
