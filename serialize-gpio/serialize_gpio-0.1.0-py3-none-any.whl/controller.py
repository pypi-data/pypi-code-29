from functools import partial
from queue import Queue
from serialize_gpio.exceptions import *
from serialize_gpio.messageManipulators import get_message_manipulator_by_format
from serialize_gpio.inspection import *
import gpiozero


def _method_property_function(messages):

    """This function will be assigned, after being partially applied, to device properties that receive callable objects
    like Button.when_pressed. It will take a list of messages and make the controller handle them one by one."""

    controller = GPIOController()
    for message in messages:
        controller.handle_message(message)


def _get_values_from_keys(dictionary, key, *additional_keys):

    """Gets the values in the 'dictionary' parameter associated with the specified keys and returns them. If only one
    key is received, the corresponding element will be returned. If more than one key is received, a list containing
    all the corresponding values will be returned instead."""

    try:
        if len(additional_keys) == 0:
            return dictionary[key]
        else:
            result = [dictionary[key]] + [dictionary[additional_key] for additional_key in additional_keys]
            return result
    except KeyError as exception:
        raise MissingMessageArguments(exception.args[0])


def _get_args_from_message(command_dict):

    """Gets the 'args' parameter from a message and verifies if it's a dict before returning it. If it is not
    a dict, an exception is raised."""

    kwargs = _get_values_from_keys(command_dict, 'args')
    if not isinstance(kwargs, dict):
        raise BadMessageArguments('args', 'Args field should evaluate to dict when parsed')
    return kwargs


def _parse_property_value_from_message(property_dict):

    """Receives the property value and returns what should be assigned to the device property. First it verifies the
    received parameter is a dictionary, and then proceeds to parse the value.
    For method properties, it partially applies '_method_property_function' (passing in the 'message_list'
    attribute of the message as it's parameter) and returns it.
    For literals, it return the 'literal_value' attribute of the message.
    If the type is 'none', returns None
    Otherwise, it will raise an exception."""

    if not isinstance(property_dict, dict):
        raise BadMessageArguments('property_value', 'Property value field should evaluate to dict when parsed')
    property_type = _get_values_from_keys(property_dict, 'property_type')
    if property_type == 'method':
        message_list = _get_values_from_keys(property_dict, 'message_list')
        return partial(_method_property_function, message_list)
    elif property_type == 'literal':
        return _get_values_from_keys(property_dict, 'literal_value')
    elif property_type == 'none':
        return None
    else:
        raise BadMessageArguments(
            'property_type', "Property type '{property_type}' is not supported".format(property_type=property_type))


def _make_action_index():

    """This function will be used as a decorator to build the controller's index of actions. Declares the index,
    a function for adding elements to it and return the function."""

    action_index = {}

    def add_action_handler(func):
        action_index[func.__name__] = func
        return func

    add_action_handler.action_index = action_index
    return add_action_handler


action_handler = _make_action_index()
# The action_handler variable will be the decorator itself


class GPIOController(object):

    """Class for implementing the controller (_GPIOController class) as a singleton object."""

    _instance = None

    def __init__(self, message_format='json'):
        if GPIOController._instance is None:
            GPIOController._instance = _GPIOController(message_format)

    def __getattr__(self, item):
        return getattr(GPIOController._instance, item)

    def __setattr__(self, attr, value):
        setattr(GPIOController._instance, attr, value)


class _GPIOController(object):

    """Class implementing the actual logic of the GPIOController.

    It's fields are:
        - '_device_classes_index': a dictionary containing all the available classes. It's elements are
            {'class_name', class_object}
        - '_devices': a dictionary containing the currently active devices. It's elements are
            {'device_name': device_object}
        - '_message_manipulator': an instance of a class defined in messageManipulators.py. It's used for
            encoding and decoding messages.
        - '_action_index': a dictionary that maps message actions to the corresponding method that handles them
        - 'response_queue' : a queue element where the controller will put any messages it wishes to send as
            responses. We take this approach because we might need to put messages on it from a different thread
            if a function property from a device needs to send a message when executed.
        - 'message_format': a property representing the current message format being used.'"""

    def __init__(self, message_format):
        self._device_classes_index = build_device_classes_index()
        self._devices = {}
        self._message_manipulator = get_message_manipulator_by_format(message_format)
        self._action_index = action_handler.action_index
        self.response_queue = Queue()

    @property
    def message_format(self):
        return self._message_manipulator.message_format

    @message_format.setter
    def message_format(self, value):
        self._message_manipulator = get_message_manipulator_by_format(value)

    def handle_message(self, message):

        """Handle a message"""

        decoded_message = self._message_manipulator.decode(message)
        action = _get_values_from_keys(decoded_message, 'action')
        handler = self._get_action_handler(action)
        response_message = handler(self, decoded_message)
        return response_message

    @action_handler
    def create_device(self, message):
        target_class_key, target_device_key = _get_values_from_keys(message, 'target_class', 'target_device')
        kwargs = _get_args_from_message(message)
        if target_device_key in self._devices:
            raise DeviceAlreadyExists(target_device_key)
        try:
            self._devices[target_device_key] = self._device_classes_index[target_class_key](**kwargs)
        except KeyError:
            raise InvalidDeviceClass(target_class_key, target_device_key)
        except (ValueError, TypeError):
            raise BadConstructorArguments(target_device_key, target_class_key)

    @action_handler
    def execute_method(self, message):
        target_device_key, target_method_key = _get_values_from_keys(message, 'target_device', 'target_method')
        kwargs = _get_args_from_message(message)
        try:
            resulting_method = self._get_device_method(target_device_key, target_method_key)
            resulting_method(**kwargs)
        except (ValueError, TypeError):
            raise BadMethodArguments(target_device_key, target_method_key)

    @action_handler
    def set_property(self, message):
        target_device_key, target_property_key, property_value_dict = \
            _get_values_from_keys(message, 'target_device', 'target_property', 'property_value')
        target_device = self._get_device_from_key(target_device_key)
        property_value = _parse_property_value_from_message(property_value_dict)
        if hasattr(target_device, target_property_key):
            # setattr() will create the attribute for the device if it doesn't exist,
            # so we check if the device has it and raise the corresponding exception
            # if it does not.
            setattr(target_device, target_property_key, property_value)
        else:
            raise DevicePropertyDoesNotExist(target_device_key, target_property_key)

    @action_handler
    def get_property(self, message):
        target_device_key, target_property_key = \
            _get_values_from_keys(message, 'target_device', 'target_property')
        try:
            device = self._get_device_from_key(target_device_key)
            property_value = getattr(device, target_property_key)
            if callable(property_value):
                # If the property is a function, we just inform it is
                property_value = 'Function property'
            notification_message = self._message_manipulator.build_notify_property_value_message(
                target_device_key, target_property_key, property_value
            )
            self.response_queue.put(notification_message)
        except AttributeError:
            raise DevicePropertyDoesNotExist(target_device_key, target_property_key)

    @action_handler
    def get_state(self, message):
        target_devices = _get_values_from_keys(message, 'target_devices')
        if not isinstance(target_devices, list):
            raise BadMessageArguments('target_devices', 'Target devices field should evaluate to list when parsed.')
        if len(target_devices) == 0:
            # if no devices were given, check the state of all devices
            target_devices_dict = self._devices
        else:
            target_devices_dict = {device_key: _get_values_from_keys(self._devices, device_key)
                                   for device_key in target_devices}
        for target_device_name, target_device_object in target_devices_dict.items():
            state_notification_message = self._message_manipulator.build_notify_device_state_message(
                target_device_object.__class__.__name__, target_device_name, target_device_object.value
            )
            self.response_queue.put(state_notification_message)

    @action_handler
    def get_class_members(self, message):
        target_classes = _get_values_from_keys(message, 'target_classes')
        if not isinstance(target_classes, list):
            raise BadMessageArguments('target_classes', 'Target classes field should evaluate to list when parsed.')
        if len(target_classes) == 0:
            target_classes_dict = self._device_classes_index
        else:
            target_classes_dict = {class_name: _get_values_from_keys(self._device_classes_index, class_name)
                                   for class_name in target_classes}
        for target_class_name, target_class_object in target_classes_dict.items():
            members_notification_message = self._message_manipulator.build_notify_class_members_message(
                target_class_name, inspect_class(target_class_object)
            )
            self.response_queue.put(members_notification_message)

    @action_handler
    def close_device(self, message):
        target_device_key = _get_values_from_keys(message, 'target_device')
        target_device = self._get_device_from_key(target_device_key)
        target_device.close()
        self._remove_device(target_device_key)

    @action_handler
    def terminate(self, message):
        # The message is passed as an argument to keep the actions polymorphic
        devices = [(k, v) for k, v in self._devices.items()]
        for key, device in devices:
            device.close()
            self._remove_device(key)

    def _get_action_handler(self, requested_action):

        """Gets the corresponding method for handling a message according to it's action."""

        try:
            handler = self._action_index[requested_action]
            return handler
        except KeyError:
            raise BadMessageArguments('action',
                                      "Requested action '{action}' is not supported".format(action=requested_action))

    def _get_device_from_key(self, device_key):
        try:
            return self._devices[device_key]
        except KeyError:
            raise DeviceDoesNotExist(device_key)

    def _get_device_method(self, target_device_key, target_method_key):
        try:
            device = self._get_device_from_key(target_device_key)
            return getattr(device, target_method_key)
        except AttributeError:
            raise DeviceMethodDoesNotExist(target_device_key, target_method_key)

    def _remove_device(self, device_key):
        del self._devices[device_key]
