from inspect import getmembers, isclass
import gpiozero


def build_device_classes_index():

    """This function uses the inspect module to find all the device classes in gpiozero and return a dict
    containing pairs {class_name: class_object}. That dictionary is used by the _GPIOController object
    to map requested classes (having received it's name as a string) to their corresponding class object"""

    def is_device_subclass(module_element):
        # Bear in mind that issubclass(cls, cls) returns true, so gpiozero.Device will be included
        return isclass(module_element) and issubclass(module_element, gpiozero.Device)

    class_query = getmembers(gpiozero, is_device_subclass)
    return {name: cls for name, cls in class_query}


def inspect_class(cls):

    """Returns a dictionary containing the members of the class received as a parameter. It has the following format:
    {'callables': list of the names of callable members,
     'settable_properties': list of the names of settable properties,
      'not_settable_properties' list of the names of not settable properties}"""

    members = list(filter(lambda member: not member[0].startswith('_'), getmembers(cls)))
    _remove_repeated_elements(cls, members)
    callables, settable, not_settable = _split_members(members)
    result = {'callables': _filter_attribute_values(callables),
              'settable_properties': _filter_attribute_values(settable),
              'not_settable_properties': _filter_attribute_values(not_settable)}
    return result


def _remove_repeated_elements(cls, members):

    """ Remove elements with repeated values. It happens because gpiozero sometimes creates
    members of a subclass and assignes to them a member of a superclass for domain reasons.
    For example: Button has the attribute 'active_time' it inherits from Hold Mixin, but it
    also has the attribute 'pressed_time' declared this way:
        Button.pressed_time = Button.active_time
    We remove one of those repeated elements, leaving the one that was declared in the class
    we are inspecting at a given moment (we'd keep 'pressed_time' in the above example)."""

    repeated_elements = []
    # Flattened list with the attributes of the parent classes
    bases_elements = [item for parent_class in cls.__bases__ for item in dir(parent_class)]

    for i in range(0, len(members)):
        for j in range(i + 1, len(members)):
            if members[i][1] == members[j][1]:
                repeated_elements.append((members[i], members[j]))

    for repeated in repeated_elements:
        if repeated[0][0] in bases_elements:
            members.remove(repeated[0])
        else:
            members.remove(repeated[1])


def _split_members(members):

    """Splits the members list into 3 sublists:
        -One containing functions (or other callable objects).
        -One containing properties which have a setter
        -The last containing properties which don´t have a setter
    Anything not falling in one of those categories gets discarded."""

    callables, settable_properties, not_settable_properties = [], [], []
    for element in members:
        element_value = element[1]
        if callable(element_value):
            callables.append(element)
        elif isinstance(element_value, property):
            if element_value.fset is None:
                not_settable_properties.append(element)
            else:
                settable_properties.append(element)
    return callables, settable_properties, not_settable_properties


def _filter_attribute_values(attr_list):
    return [element[0] for element in attr_list]
