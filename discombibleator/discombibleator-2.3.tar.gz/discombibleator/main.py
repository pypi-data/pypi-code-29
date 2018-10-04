from .reference_lists import Reference_Lists as ref_list
from .algs import *
from .inputs import *

class Discombibleator(Verse):

    """Class taking an object and converting it into an output string with
    measurements converted into imperial or metric units.

    """

    def __init__(self, object):
        """Method initializing Discombibleator tool.
        Method initializing Biblical_Measurement object.

        Args:
            string (str)
            units (str)
            arr (arr)

        Attributes:
            string (str): String of text to be converted into modern
                measurements.
            arr (arr): empty array to be replaced with string's content as it is
                processed through the class' methods. This keeps the original
                string accessible even after processing has occured.
            units (string): String indicating whether output units will be in
                Imperial or Metric units. Default is Imperial units
            __run__: method running the string through the processing steps as
                new objest self.arr
        """
        self.string = object.string
        self.units = object.units
        self.arr = None

    def run(self):
        """Method running algorithms from algs.py on inputs from inputs.py

        returns:
            string identical to input verse, but with unit names and associated values converted to metric or imperial mesaurements
        """
        self.arr = Tokenize(self.string).__run__()
        self.arr = Concat_Multiword(self.arr).__run__()
        self.arr = Has_Measure_Words(self.arr).__run__()
        self.arr = Lemmatize_Measure_Words(self.arr).__run__()
        self.arr = Find_Convert_Numbers(self.arr, self.units).__run__()
        self.arr = Convert_Measure_Words(self.arr, self.units).__run__()
        return Join_Elements(self.arr).__run__()
