import datetime
from unittest import TestCase

import doid
from doid.container import K, ListContainer
from doid.filter import Q, BaseFilter


class GenericObject(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "<" + ", ".join(f"{k}={v}" for k, v in self.__dict__.items()) + ">"


DATA = [
    ['Adrian Rodriguez', 'Pattonstad', datetime.date(1939, 6, 19), 'PM'],
    ['Alex Hogan', 'Andersonfurt', datetime.date(1962, 12, 26), 'PM'],
    ['Brendan Mendoza PhD', 'Lake Rhonda', datetime.date(1907, 1, 28), 'PM'],
    ['Carol Roy', 'Pattonstad', datetime.date(1913, 12, 19), 'AM'],
    ['Christopher Medina', 'Lake Rhonda', datetime.date(1998, 7, 6), 'AM'],
    ['Christopher Sweeney', 'Pattonstad', datetime.date(1915, 7, 17), 'PM'],
    ['Cody Zimmerman', 'North Alanberg', datetime.date(1948, 5, 10), 'PM'],
    ['Courtney Nguyen', 'Lake Rhonda', datetime.date(1953, 8, 13), 'AM'],
    ['Crystal Brown', 'Lake Rhonda', datetime.date(1949, 6, 5), 'AM'],
    ['Curtis Woodard', 'West Josephchester', datetime.date(1935, 4, 23), 'AM'],
    ['Daniel Hall', 'Andersonfurt', datetime.date(1924, 7, 26), 'PM'],
    ['Donald Johnson', 'Lake Rhonda', datetime.date(1922, 1, 10), 'AM'],
    ['Dr. Patricia Pierce', 'North Alanberg', datetime.date(2011, 10, 2), 'PM'],
    ['Jeffrey Maynard', 'North Alanberg', datetime.date(1934, 2, 27), 'PM'],
    ['Jennifer Bates', 'Pattonstad', datetime.date(1976, 11, 2), 'PM'],
    ['Jessica Porter', 'Pattonstad', datetime.date(1995, 10, 14), 'PM'],
    ['John Rodriguez', 'Lake Rhonda', datetime.date(1983, 1, 16), 'AM'],
    ['Joseph Smith', 'West Josephchester', datetime.date(1918, 4, 2), 'PM'],
    ['Karen Henry', 'North Alanberg', datetime.date(1967, 1, 1), 'AM'],
    ['Kelsey Howell', 'West Josephchester', datetime.date(1961, 3, 5), 'PM'],
    ['Kevin Bailey DVM', 'Lake Rhonda', datetime.date(1941, 6, 17), 'AM'],
    ['Laura Hernandez', 'Pattonstad', datetime.date(1962, 1, 15), 'PM'],
    ['Lisa Nelson', 'West Josephchester', datetime.date(1913, 10, 24), 'AM'],
    ['Marissa Cline', 'Lake Rhonda', datetime.date(1951, 8, 22), 'AM'],
    ['Mark Dixon', 'Andersonfurt', datetime.date(1983, 6, 20), 'AM'],
    ['Mary Johnson', 'Pattonstad', datetime.date(1946, 10, 21), 'PM'],
    ['Max Bautista', 'Andersonfurt', datetime.date(1933, 6, 14), 'PM'],
    ['Melinda Kelly', 'North Alanberg', datetime.date(1941, 2, 27), 'PM'],
    ['Michael Simpson', 'North Alanberg', datetime.date(1976, 11, 20), 'PM'],
    ['Michael Wilson', 'North Alanberg', datetime.date(1986, 4, 30), 'AM'],
    ['Mr. Austin Rosales', 'North Alanberg', datetime.date(1907, 11, 25), 'AM'],
    ['Mrs. Alexa Cameron', 'North Alanberg', datetime.date(1939, 11, 2), 'PM'],
    ['Ms. Chelsey Richardson', 'North Alanberg', datetime.date(1994, 3, 13), 'PM'],
    ['Paul Miller', 'North Alanberg', datetime.date(1987, 8, 23), 'AM'],
    ['Phillip Wallace', 'Lake Rhonda', datetime.date(1937, 1, 31), 'PM'],
    ['Robert Brown', 'Pattonstad', datetime.date(1969, 9, 1), 'PM'],
    ['Robert Valdez', 'Andersonfurt', datetime.date(2010, 9, 7), 'PM'],
    ['Sandra Williams', 'Andersonfurt', datetime.date(1920, 2, 26), 'PM'],
    ['Sarah Simmons', 'Pattonstad', datetime.date(1980, 9, 6), 'AM'],
    ['Shawn White', 'North Alanberg', datetime.date(1915, 6, 2), 'PM'],
    ['Stephanie Wang', 'West Josephchester', datetime.date(1907, 1, 25), 'PM'],
    ['Stephen Hahn', 'Pattonstad', datetime.date(1914, 12, 10), 'PM'],
    ['Steven Wolfe', 'West Josephchester', datetime.date(2009, 12, 6), 'PM'],
    ['Thomas Griffin', 'Lake Rhonda', datetime.date(1966, 3, 26), 'PM'],
    ['Thomas Kramer', 'Andersonfurt', datetime.date(1948, 3, 25), 'PM'],
    ['Timothy Ray', 'Pattonstad', datetime.date(2007, 7, 27), 'AM'],
    ['Vanessa Rogers', 'Andersonfurt', datetime.date(1932, 1, 24), 'PM'],
    ['Walter Heath', 'Pattonstad', datetime.date(1937, 8, 20), 'PM'],
    ['William Hall', 'North Alanberg', datetime.date(1997, 5, 4), 'AM'],
    ['William Rodriguez', 'North Alanberg', datetime.date(1994, 11, 30), 'PM']
]

class TestInterfaces(TestCase):
    def setUp(self):
        self.data = ListContainer(
            GenericObject(name=name, city=city, born=born, ampm=ampm) for
            name, city, born, ampm in DATA
        )

    def test_attribute_getter_string(self):
        aaron = self.data[0]
        self.assertEqual(K('name')(aaron)[0], aaron.name)
        self.assertEqual(K('city')(aaron)[0], aaron.city)
        self.assertEqual(K('born')(aaron)[0], aaron.born)
        self.assertEqual(K('ampm')(aaron)[0], aaron.ampm)

    def test_attribute_getter_nested(self):
        aaron = self.data[0]
        self.assertEqual(K('born__year')(aaron)[0], aaron.born.year)
        self.assertEqual(K('born__year__denominator')(aaron)[0], aaron.born.year.denominator)
        self.assertEqual(K('born__month')(aaron)[0], aaron.born.month)
        self.assertEqual(K('born__month__denominator')(aaron)[0], aaron.born.month.denominator)
        self.assertEqual(K('born__day')(aaron)[0], aaron.born.day)
        self.assertEqual(K('born__day__denominator')(aaron)[0], aaron.born.day.denominator)

    def test_generic_filter__eq(self):
        result = self.data.filter(ampm='AM')
        self.assertEqual(len(result), len([_ for _ in self.data if _.ampm == 'AM']))

    def test_generic_filter__ne(self):
        result = self.data.filter(ampm__ne='AM')
        self.assertEqual(len(result), len([_ for _ in self.data if _.ampm != 'AM']))

    def test_generic_filter__negated(self):
        am_filter = Q(ampm='AM')
        self.assertIsInstance(am_filter, BaseFilter)
        result = self.data.filter(~am_filter)  # Not am_filter
        self.assertEqual(len(result), len([_ for _ in self.data if _.ampm != 'AM']))

    def test_generic_filter__ge(self):
        milenials = self.data.filter(born__year__ge=2000)
        self.assertEqual(len(milenials), len([_ for _ in self.data if _.born.year >= 2000]))

    def test_generic_filter__between(self):
        x_gen = self.data.filter(born__year__between=[1960, 1980])
        self.assertEqual(len(x_gen), len([_ for _ in self.data if 1960 <= _.born.year <= 1980]))

    def test_generic_filter__chain(self):
        x_gen = self.data.filter(born__year__ge=1960).filter(born__year__le=1980)
        self.assertEqual(len(x_gen), len([_ for _ in self.data if 1960 <= _.born.year <= 1980]))

    def test_generic_filter__and(self):
        x_gen_filter = Q(born__year__ge=1960) & Q(born__year__le=1980)
        self.assertIsInstance(x_gen_filter, BaseFilter)
        x_gen = self.data.filter(x_gen_filter)
        self.assertEqual(len(x_gen), len([_ for _ in self.data if 1960 <= _.born.year <= 1980]))

    def test_generic_filter__or(self):
        random_filter = Q(born__year__ge=1960) | Q(born__month=12)
        self.assertIsInstance(random_filter, BaseFilter)
        result = self.data.filter(random_filter)
        self.assertEqual(
            len(result), len([_ for _ in self.data if _.born.year >= 1960 or _.born.month == 12])
        )

    def test_generic_filter_regex(self):
        c_persons = self.data.filter(name__match='^C')
        self.assertEqual(len(c_persons), len([_ for _ in self.data if _.name.startswith('C')]))

    def test_sort_simple(self):
        inverse = self.data.order_by('name', reverse=True)
        self.assertEqual(inverse, self.data[::-1])

    def test_sort_multiple_keys(self):
        ordered = self.data.order_by('city', 'name')
        self.assertEqual(ordered, sorted(self.data, key=lambda x: [x.city, x.name]))

    def test_sort_stability(self):
        ordered = self.data.order_by('city').order_by('name', reverse=True)
        equivalent = self.data[:]
        equivalent.sort(key=lambda x: x.city)
        equivalent.sort(key=lambda x: x.name, reverse=True)
        self.assertEqual(ordered, equivalent)
