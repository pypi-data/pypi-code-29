class GPIOControllerException(Exception):

    """Base class for all exceptions of the package"""

    def __init__(self, msg=None):
        if msg is None:
            msg = "A GPIOControllerException was raised"
        super(GPIOControllerException, self).__init__(msg)


class DeviceError(GPIOControllerException):

    """Base class for all the exceptions regarding devices"""

    def __init__(self, device_key, msg=None):
        if msg is None:
            msg = "A DeviceError was raised regarding device '{device_key}'".format(device_key=device_key)
        super(DeviceError, self).__init__(msg)
        self.device_key = device_key


class UnsupportedMessageFormat(GPIOControllerException):

    def __init__(self, message_format):
        msg = "Message format '{message_format} is not supported'".format(message_format=message_format)
        super(UnsupportedMessageFormat, self).__init__(msg)
        self.message_format = message_format


class MissingMessageArguments(GPIOControllerException):

    def __init__(self, missing_key):
        msg = "Missing message parameter '{missing_key}'".format(missing_key=missing_key)
        super(MissingMessageArguments, self).__init__(msg)
        self.missing_key = missing_key


class BadMessageArguments(GPIOControllerException):

    def __init__(self, bad_key, msg=None):
        if msg is None:
            msg = "Incorrect message argument with key {bad_key}".format(bad_key=bad_key)
        super(BadMessageArguments, self).__init__(msg)
        self.bad_key = bad_key


class DeviceAlreadyExists(DeviceError):

    def __init__(self, device_key):
        msg = "Device '{device_key}' already exists".format(device_key=device_key)
        super(DeviceAlreadyExists, self).__init__(device_key, msg)


class DeviceDoesNotExist(DeviceError):
    
    def __init__(self, device_key):
        msg = "Device '{device_key}' does not exist".format(device_key=device_key)
        super(DeviceDoesNotExist, self).__init__(device_key, msg)


class InvalidDeviceClass(DeviceError):

    """Raised when attempting to create a device from a class which is not in the class index"""

    def __init__(self, requested_device_class, device_key):
        msg = "'{requested_device_class}' is not a valid device class".format(
            requested_device_class=requested_device_class)
        super(InvalidDeviceClass, self).__init__(device_key, msg)
        self.requested_device_class = requested_device_class


class DeviceAttributeError(DeviceError):

    """Base class for errors regarding device attributes"""

    def __init__(self, device_key, requested_attribute, msg):
        super(DeviceAttributeError, self).__init__(device_key, msg)
        self.requested_attribute = requested_attribute


class BadMethodArguments(DeviceAttributeError):

    def __init__(self, device_key, requested_method, msg=None):
        if msg is None:
            msg = "Incorrect arguments for method '{requested_method}' on device '{device_key}'".format(
                requested_method=requested_method, device_key=device_key)
        super(BadMethodArguments, self).__init__(device_key, requested_method, msg)


class BadConstructorArguments(BadMethodArguments):

    def __init__(self, device_key, requested_class):
        msg = "Incorrect arguments for method '__init__' from class '{requested_class}' when" \
              "trying to instantiate '{device_key}'".format(requested_class=requested_class, device_key=device_key)
        super(BadConstructorArguments, self).__init__(device_key, requested_class, msg)


class DeviceMethodDoesNotExist(DeviceAttributeError):

    def __init__(self, device_key, requested_method):
        msg = "'{device_key}' does not support method '{requested_method}'".format(
            device_key=device_key, requested_method=requested_method)
        super(DeviceMethodDoesNotExist, self).__init__(device_key, requested_method, msg)


class DevicePropertyDoesNotExist(DeviceAttributeError):

    def __init__(self, device_key, requested_property):
        msg = "'{device_key}' has no property named '{requested_property}'".format(
            device_key=device_key, requested_property=requested_property)
        super(DevicePropertyDoesNotExist, self).__init__(device_key, requested_property, msg)
