from json import dumps, loads
from xml.etree.ElementTree import Element, tostring, fromstring
from inspect import isclass
from serialize_gpio.exceptions import UnsupportedMessageFormat


_message_manipulators = None


def _build_message_manipulator_index():

    """Builds a dictionary containing the pairs {'message_format': MessageManipulatorClass} and assigns it to
    '_message_manipulators'."""

    def is_manipulator_class(module_element):
        # Bear in mind that issubclass(cls, cls) returns true, so BasicMessageManipulator will be included
        return isclass(module_element) and issubclass(module_element, BasicMessageManipulator)

    global _message_manipulators
    global_attributes = globals()
    _message_manipulators = {global_attributes[key].message_format: global_attributes[key]
                             for key in global_attributes if is_manipulator_class(global_attributes[key])}


def get_message_manipulator_by_format(requested_message_format):

    """Receives the string representation of a message format, maps it to the corresponding manipulator class
    using '_message_manipulators' and return an instance of that class."""

    if _message_manipulators is None:
        _build_message_manipulator_index()
    try:
        manipulator_class = _message_manipulators[requested_message_format]
        return manipulator_class()
    except KeyError:
        raise UnsupportedMessageFormat(requested_message_format)


class BasicMessageManipulator:

    """Message manipulator that implements message building. It's meant to be directly used locally (when, for example,
    you don't need to transfer messages through a socket) as it does not encode or decode messages, it just keeps the
    messages as dictionaries.
       Other message manipulators should be implemented by subclassing BasicMessageManipulator and overriding
    the encode and decode methods."""

    message_format = 'dict'

    def build_create_device_message(self, target_class, target_device_name, **kwargs):
        message = dict(action='create_device', target_class=target_class, target_device=target_device_name,
                       args=kwargs)
        return self.encode(message)

    def build_execute_device_method_message(self, target_device_name, target_method, **kwargs):
        message = dict(action='execute_method', target_device=target_device_name, target_method=target_method,
                       args=kwargs)
        return self.encode(message)

    def build_close_device_message(self, target_device_name):
        message = dict(action='close_device', target_device=target_device_name)
        return self.encode(message)

    def build_set_literal_property_message(self, target_device_name, target_property, value):
        property_value = dict(property_type='literal', literal_value=value)
        return self._build_set_property_message(target_device_name, target_property, property_value)

    def build_set_function_property_message(self, target_device_name, target_property, *messages):
        property_value = dict(property_type='method', message_list=messages)
        return self._build_set_property_message(target_device_name, target_property, property_value)

    def build_set_property_to_none_message(self, target_device_name, target_property):
        property_value = dict(property_type='none')
        return self._build_set_property_message(target_device_name, target_property, property_value)

    def _build_set_property_message(self, target_device_name, target_property, property_value):
        message = dict(action='set_property', target_device=target_device_name, target_property=target_property,
                       property_value=property_value)
        return self.encode(message)

    def build_get_property_message(self, target_device_name, target_property):
        message = dict(action='get_property', target_device=target_device_name, target_property=target_property)
        return self.encode(message)

    def build_notify_property_value_message(self, target_device_name, target_property, value):
        message = dict(action='notify_property', target_device=target_device_name, target_property=target_property,
                       property_value=value)
        return self.encode(message)

    def build_get_device_state(self, *target_devices):
        message = dict(action='get_state', target_devices=target_devices)
        return self.encode(message)

    def build_notify_device_state_message(self, device_class, device_name, current_value):
        message = dict(action='notify_device_state', target_class=device_class, target_device=device_name,
                       current_value=current_value)
        return self.encode(message)

    def build_get_class_members_message(self, *target_classes):
        message = dict(action='get_class_members', target_classes=target_classes)
        return self.encode(message)

    def build_notify_class_members_message(self, device_class, class_members_dict):
        message = dict(action='notify_class_members', target_class=device_class)
        message.update(class_members_dict)
        return self.encode(message)

    def build_terminate_message(self):
        message = dict(action='terminate')
        return self.encode(message)

    def encode(self, message):
        return message

    def decode(self, message):
        return message


class JsonMessageManipulator(BasicMessageManipulator):

    message_format = 'json'

    def encode(self, message):
        return dumps(message)

    def decode(self, message):
        return loads(message)


class XMLMessageManipulator(BasicMessageManipulator):

    message_format = 'xml'

    def encode(self, message):
        etree_element = Element('message')
        XMLMessageManipulator._append_children(etree_element, message)
        return tostring(etree_element).decode("UTF-8")

    @staticmethod
    def _append_children(etree_element, dictionary):

        """Append all the dictionary elements to etree_element as children."""

        for key, value in dictionary.items():
            child_element = Element(key)
            if isinstance(value, dict):
                # The value is another dict and it's contents are children of child_element, so
                # we append them to it
                XMLMessageManipulator._append_children(child_element, value)
            elif isinstance(value, tuple):
                # The value is a tuple (was received as *args to the message builder) and contains controller messages.
                # When the message is decoded into a dict, these elements don't get decoded; they are put together in
                # a list and the resulting pair of the dict is {'parent.tag': [the_elements_of_the_tuple]}.
                # The attribute is used to flag when this should be done while decoding.
                child_element.set('type', 'list')
                for message in value:
                    child_element.append(fromstring(message))
            else:
                child_element.text = str(value)
            etree_element.append(child_element)

    def decode(self, message):
        etree_element = fromstring(message)
        result_dict = {}
        for element in etree_element:
            element_text = element.text
            if element_text:
                result = XMLMessageManipulator._parse_etree_element_text(element_text)
            elif 'type' in element.attrib and element.attrib['type'] == 'list':
                result = XMLMessageManipulator._decode_list(element)
            else:
                # The element contains itself children that should be decoded
                result = self.decode(tostring(element))
            result_dict[element.tag] = result
        return result_dict

    @staticmethod
    def _decode_list(etree_element):
        return [tostring(child).decode("UTF-8") for child in etree_element]

    @staticmethod
    def _parse_etree_element_text(text):
        try:
            return float(text)
        except ValueError:
            return text
