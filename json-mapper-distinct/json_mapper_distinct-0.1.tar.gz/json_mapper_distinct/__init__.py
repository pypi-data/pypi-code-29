# A module to map JSON objects

import json
from collections import namedtuple

MapDict = namedtuple('MapDict', ['ElementData'])
MapDictElement = namedtuple('MapDictElement', ['ElementKey', 'ElementData'])
MapList = namedtuple('MapList', ['ElementData'])


class JsonMap(object):
    """
    Vectorless mapping of JSON input
    """
    def __init__(self, source_json, is_file=True):
        """
        :param source_json: If is_file is true, the filename to load. Otherwise the string of JSON
        :param is_file: Whether the value in source_json is a file location or a string passed in
        """
        self.parsed_json = None
        self.raw_map = None
        self.parsed_map = None

        if is_file:
            with open(source_json, 'r') as json_file:
                self.parsed_json = json.load(json_file)
        else:
            self.parsed_json = json.loads(source_json)

        self.raw_map = self.map_json(self.parsed_json)
        self.parsed_map = self.parse_map_element(self.raw_map)

    def map_json(self, input_obj):
        return_obj = None

        if isinstance(input_obj, list):
            working_set = set()

            for i in input_obj:
                working_set.add(self.map_json(i))

            return_obj = MapList(ElementData=tuple(working_set))

        if isinstance(input_obj, dict):
            working_set = set()

            for i, v in input_obj.items():
                de = MapDictElement(ElementKey=i, ElementData=self.map_json(v))
                working_set.add(de)

            return_obj = MapDict(ElementData=tuple(working_set))

        if not isinstance(input_obj, (list, dict)):
            return type(input_obj).__name__

        return return_obj

    def parse_map_element(self, input_obj):
        """
        Parse the raw map. Convert things back to lists and dicts - only distinct
        :return: A unique parsed structure mapping things out
        """
        return_obj = None

        if isinstance(input_obj, MapList):
            working_list = []
            for i in input_obj.ElementData:
                working_obj = self.parse_map_element(i)
                working_list.append(working_obj)

            return_obj = working_list

        if isinstance(input_obj, MapDict):
            working_dict = {}
            for i in input_obj.ElementData:
                if i.ElementKey not in working_dict:
                    working_dict[i.ElementKey] = []
                working_key = working_dict[i.ElementKey]

                working_obj = self.parse_map_element(i.ElementData)
                working_key.append(working_obj)

            for i, v in working_dict.items():  # Get rid of a list if we don't need it
                if len(v) == 1:
                    working_dict[i] = v[0]

            return_obj = working_dict

        if not isinstance(input_obj, (MapList, MapDict)):
            return_obj = input_obj

        return return_obj

    def print_map(self):
        print(json.dumps(self.parsed_map, indent=4))
