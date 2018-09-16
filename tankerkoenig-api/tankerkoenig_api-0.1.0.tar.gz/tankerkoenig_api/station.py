"""
Model module containing basic models for a gas station.

Contains classes necessary to represent a gas station
from Tankerkoening API

Author  Iulius Gutberlet
"""


class Station:
    """The station itself."""

    def __init__(self):
        """Instantiate a station object."""
        self.address = Address()
        self.prices = Prices()
        self.opening_times = OpeningTimes()

    pass


class Address:
    """The address of information."""

    def __init__(self):
        """Instantiate an address object."""
        self.coords = Coords()

    pass


class Coords:
    """The GPS coordinates."""

    pass


class Prices:
    """The prices class containing the gas types as keys e5, e10, diesel."""

    pass


class OpeningTimes:
    """The opening hours information."""

    def __init__(self):
        """Instantiate an openingtimes object."""
        self.whole_day = False
        self.exceptions = []
        self.regular_times = []


class OpeningTime:
    """Concrete representation of a opening time entry."""

    pass
