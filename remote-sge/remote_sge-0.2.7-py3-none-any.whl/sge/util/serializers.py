from collections import OrderedDict
from datetime import datetime

def element_text(element):
    try:
        return element.text
    except AttributeError:
        pass

class XmlEnvironmentDeserializer(object):
    @staticmethod
    def deserialize(xml_node):
        res = OrderedDict()
        if xml_node != None:
            for var_el in xml_node.getchildren():
                var_name = var_el.find('VA_variable').text
                if var_name[0:14] != '__SGE_PREFIX__':
                    res[var_name] = element_text(var_el.find('VA_value'))
        return res

class XmlJobArgumentsDeserializer(object):
    @staticmethod
    def deserialize(xml_element):
        res = []
        if xml_element != None:
            for arg_el in xml_element.getchildren():
                res.append(arg_el.find('ST_name').text)
        return res

class XmlIntDeserializer(object):
    @staticmethod
    def deserialize(xml_element):
        text = element_text(xml_element)
        if text:
            return int(text)

class StringSerializer(object):
    """
    Abstract class representing how to convert between int,
    boolean or dict types, and their string representations
    that are accepted by qsub_.

    .. _qsub: http://gridscheduler.sourceforge.net/htmlman/htmlman1/qsub.html
    """
    @staticmethod
    def serialize(value):
        return value
    @staticmethod
    def deserialize(value):
        return value
    @staticmethod
    def doctext():
        return "Doesn't modify the string value being serialized."

class DictionaryConverter(StringSerializer):
    @staticmethod
    def serialize(dictionary):
        # result = []
        # for item in dictionary.items():
        #     result.append("%s=%s" % item)
        return ','.join(["%s=%s" % item for item in dictionary.items()])
    @staticmethod
    def deserialize(value):
        return dict(item.split("=") for item in value.split(","))

    @staticmethod
    def doctext():
        return ("Accepts a :class:`dict` and serializes it as " + 
                "var1=val1,var2=val2,...")

class DateTimeConverter(StringSerializer):
    """
    Converts a python :class:`~datetime.datetime` into a string in the format
    YYYYMMDDhhmm.SS, as described in the sge datatype_ specification.

    .. _datatype: http://gridscheduler.sourceforge.net/htmlman/htmlman1/sge_types.html
    """
    FORMAT = r"%Y%m%d%H%M.%S"
    @staticmethod
    def serialize(datetime):
        return datetime.strftime(DateTimeConverter.FORMAT)
    @staticmethod
    def deserialize(string):
        return datetime.strptime(string, DateTimeConverter.FORMAT)
    @staticmethod
    def doctext():
        return ("Accepts a :class:`~datetime.datetime` and serializes it as " + 
                DateTimeConverter.FORMAT)

class BoolConverter(StringSerializer):
    """Helper class to convert to/from bool attributes."""
    TRUE = r'yes'
    FALSE = r'no'

    @staticmethod
    def serialize(value):
        if value:
            return BoolConverter.TRUE
        else:
            return BoolConverter.FALSE

    @staticmethod
    def deserialize(value):
        return value == BoolConverter.TRUE

    @staticmethod
    def doctext():
        return "Accepts: True or False.  Writes appropriate value to qsub."


class IntConverter(StringSerializer):

    """Helper class to convert to/from int attributes."""
    @staticmethod
    def serialize(value):
        # print(value)
        return str(value)

    @staticmethod
    def deserialize(value):
        return int(value)

    @staticmethod
    def doctext():
        return "Accepts int value and translates to a string."
