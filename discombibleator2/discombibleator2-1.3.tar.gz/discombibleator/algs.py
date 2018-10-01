import numpy as np
import pandas as pd
import pkg_resources
from nltk.tokenize import word_tokenize
from .reference_lists import Reference_Lists as ref_lists

path1 = "data/measures.csv"
filepath1 = pkg_resources.resource_filename(__name__, path1)
path2 = "data/measurement_roots.csv"
filepath2 = pkg_resources.resource_filename(__name__, path2)
path3 = "data/multiword_values.csv"
filepath3 = pkg_resources.resource_filename(__name__, path3)

# various reference dictionaries to be accessed later
measures = pd.read_csv(filepath1, header = 0, index_col = 0,
                        squeeze=True).to_dict()

measurement_roots = pd.read_csv(filepath2, header=0,
                                index_col=1, squeeze=True).to_dict()

multiword_values = pd.read_csv(filepath3, header=0,
                                index_col=1, squeeze=True).to_dict()

class Tokenize(object):

    """Class tokenizing object with nltk

    attributes:
        __init__
        run

    returns:
        self.arr (arr): input string tokenized by word

    """

    def __init__(self, object):
        self.string = object
        self.arr = None

    def __run__(self):
        self.arr = word_tokenize(self.string)
        return self.arr

class Concat_Multiword(object):

    """Method finding and concatenating tokenized multi-word measure words.

    attributes:
        __init__
        __run__

    """

    def __init__(self, object):
        """Method initializing Concat_Multiword

        args:
            object (obj)

        attributes:
            arr (arr): array of word-tokenized words and symbols
            has_multiword (bool): checks for presence of potential
                multiword-measure words through list of multiword_signifiers
            signifiers (arr): list of multiword_signifiers present in arr
            ordinal (arr): list of ordinal_times signifiers to check
        """
        self.arr = object
        self.has_multiword = any(np.intersect1d(self.arr, ref_lists().multiword_signifiers))
        self.signifiers = set(self.arr).intersection(ref_lists().multiword_signifiers)
        self.ordinal = ref_lists().ordinal_times

    def __run__(self):
        """Method to concatenate multi-word measure words into one Array
        item. The method searches for signifiers of potential multiword measure
        measurewords present, then confirms and standardizes the word as one
        token.

        returns:
            arr (arr): array of words with multiword tokens joined
        """
        if self.has_multiword == True:
            for i, j in enumerate(self.arr):
                if j in self.signifiers:
                    if self.arr[i-1] in self.ordinal:
                        self.arr[i-2:i+1] = [" ".join(self.arr[i-2:i+1])]
                    elif j in ("journey", "walk") and \
                    self.arr[i-2] in ("day", "days"):
                        if self.arr[i-3] in ("Sabbath", "sabbath"):
                            self.arr[i-3:i+1] = ["sabbath day's journey"]
                        else:
                            self.arr[i-2:i+1] = ["days' journey"]
                    elif j in ("cubit", "cubits"):
                        if self.arr[i-1] == 'long':
                            self.arr[i-1:i+1] = ["long cubits"]
        return self.arr

class Has_Measure_Words(object):

    """Method checking whether a valid measurement can be found in the input.

    attributes:
        __init__
        __run__

    """

    def __init__(self, object):
        """Method initializing Has_Measure_Words

        args:
            arr (arr)

        attributes:
            arr (arr): array to be checked for relevant measure words
            measurement_found (bool): signifier if measure word found,
                initialized to False
            mwords (dict): dictionary of measure words in various forms
        """
        self.arr = object
        self.mwords = (list(measurement_roots.keys()) + list(measurement_roots.values()))

    def __run__(self):
        """Method checking for presence of measurments in Ancient Hebrew units

        returns:
            arr (arr): returns array if Ancient Hebrew measure words found
                in arr
        """
        if set(self.mwords) & set(self.arr):
            return self.arr
        else:
            raise ValueError("Measurement to be converted not found in input text:\n{}".format(self.arr))

class Lemmatize_Measure_Words(object):

    """Method lemmatizing measure words in input.

    attributes:
        __init__
        __run__

    """

    def __init__(self, object):
        self.arr = object

    def __run__(self):
        """Method turning measure words into a standard form for later lookup of
        conversion rates

        returns:
            self.arr (arr): array with measure words standardized to form found
                in measures
        """
        self.arr[:] = [measurement_roots[word] if word in measurement_roots \
            else word for word in self.arr]
        return self.arr

class Find_Convert_Numbers(object):

    """Class locating and converting relevant numbers.

    attributes:
        __init__
        Represents_Int
        Number_Multiplier
        Number_Converter
        Range_Sensitizer
        Measure_Word_Converter
        Match_Num_MW
        __run__

    """

    def __init__(self, object, units ="imperial"):
        """Method initializing Find_Convert_Numbers

        args:
            object (obj)
            units (str)

        attributes:
            arr (arr): array to be processed
            units (str): string indication whether measurement are to be given
                in metric or imperial units. Default in imperial
        """
        self.arr = object
        self.units = units

    def represents_num(self, s):
        """Method checking whether an input is a string representation of an integer.

        args:
            s (string): string item to be checked

        returns:
            (bool): whether the input is a string representation of an integer
        """
        try:
            int(s)
            return True
        except ValueError:
            return False

    def number_multiplier(self, n, measure_word):
        """Method converting number from units in Ancient Hebrew measurements to
        units in modern measurements.

        args:
            n (int): number to be converted
            measure_word (str): Ancient Hebrew units in which n was measured

        returns:
            (str): string of the float of n converted into Imperial or Metric
                units
        """
        if self.units == "metric":
            n = round((float(n) * float(measures['metric_multiplier'][measure_word])), 2)
        else:
            n = round((float(n) * float(measures['imperial_multiplier'][measure_word])), 2)
        return str(n)

    def number_converter(self, item, arr, j):
        """Method handling both integers and the words "the" and "an" before
        measure words, converting them to imperial or metric units

        args:
            item (str): string of int to be converted into int
            arr (arr): array in which item and j are located
            j (str): measure word in array

        returns:
            arr (arr): array with numbers replaced with converted numbers
        """
        item_locator = arr.index(item)
        if self.represents_num(item):
            arr[item_locator] = self.number_multiplier(item, j)
        elif item in ("a", "an", "the", "A", "An", "The"):
            if(arr.index(j) - item_locator) in range(3):
                arr[item_locator] = self.number_multiplier(1, j)
        return arr

    def nums_to_modern(self):
        """Method converting numbers and associated units to modern measurements
        within a range of 3 places in array

        returns:
            self.arr (arr): array with original numbers converted to modern units
        """
        for i, j in enumerate(self.arr):
            if j in measurement_roots.values():
                if i <= 3:
                    for unit in self.arr[:i]:
                        self.arr = self.number_converter(unit, self.arr, j)
                else:
                    for unit in self.arr[i-3:i]:
                        self.arr = self.number_converter(unit, self.arr, j)
        return self.arr

    def __run__(self):
        """Method running consecutive methods within Find_Convert_Numbers class

        returns:
            arr (arr): array with measurement values converted into modern
                units
        """
        self.nums_to_modern()
        return self.arr

class Convert_Measure_Words(object):

    """Class converting measure words from Ancient Hebrew units to modern units

    args:
        object (obj)
        units (str)

    attributes:
        __init__
        __run__

    """

    def __init__(self, object, units):
        self.arr = object
        self.units = units

    def __run__(self):
        """Method replacing Ancient Hebrew measure words with their imperial or
        metric counterparts, in line with unit specification
        """
        for i, j in enumerate(self.arr):
            if j in measurement_roots.values():
                self.arr[i] = measures[self.units][j]
        return self.arr

class Join_Elements(object):

    """Class detokenizing array of words into final sentence.

    attributes:
        __init__
        represents_float
        __run__

    """

    def __init__(self, object):
        self.arr = object
        self.output = None

    def represents_float(self, s):
        """Method checking whether an input is a string representation of a
        float.

        args:
            s (string): string item to be checked

        returns:
            (bool): whether the input is a string representation of an float
        """
        try:
            float(s)
            return True
        except ValueError:
            return False



    def __run__(self):
        """Method running Join_Elements class. If no elements that could have
        been converted are found, method raises an error.

        returns:
            output (str): string of input verse with Ancient Hebrew measurements
            converted into modern measurements.
        """
        #has_numbers ensures Value Error will be raised unless method finds
        #indication of converted measures
        has_numbers = False
        for unit in self.arr:
            if self.represents_float(unit): #indicative of converted numbers
                has_numbers = True
            elif ("PM" or "AM" or "noon") in unit: #indicative of converted times
                has_numbers = True
            self.output = "".join([" "+i if not i.startswith("'") and \
            i not in ref_lists().punctuation else i for i in self.arr]).strip()
        if has_numbers == False:
            raise ValueError("digits of numbers to be converted not found in"
            "input text:\n{}".format(self.arr))
        return self.output
