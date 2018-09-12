import collections
from abc import abstractmethod, ABCMeta

import six

try:  # python 3.5+
    from typing import TypeVar, Callable, Optional, Iterable, Any, Tuple, Mapping, Any, Dict
    YA = TypeVar('YA', bound='YamlAble')
    T = TypeVar('T')
except ImportError:
    pass

try:  # python 3.5.4+
    from typing import Type
except ImportError:
    pass # normal for old versions of typing

from yaml import Loader, SafeLoader, Dumper, SafeDumper, MappingNode

from yamlable.base import AbstractYamlObject, NONE_IGNORE_CHECKS, read_yaml_node_as_dict
from yamlable.yaml_objects import YamlObject2


YAMLABLE_PREFIX = '!yamlable/'


class AbstractYamlAble(AbstractYamlObject):
    """
    The abstract part of YamlAble. It might be useful to inherit if you want to create a super class for several
    classes, with the same YamlAble behaviour.
    """

    @classmethod
    @abstractmethod
    def is_yaml_tag_supported(cls,
                              yaml_tag  # type: str
                              ):
        # type: (...) -> bool
        """
        Implementing classes should return True if they are able to decode yaml objects with this tag.
        Note that the associated yaml object tag will be

            !yamlable/<yaml_tag>

        :param yaml_tag:
        :return:
        """


class YamlAble(AbstractYamlAble):
    """
    A helper class to register a class as able to dump instances to yaml and to load them back from yaml.

    This class does not rely on the `YAMLObject` class provided in pyyaml, so it provides a bit more flexibility (no
    metaclass magic).

    The behaviour is very similar though:
     - fill the `__yaml_tag_suffix__` either directly or using the @yaml_info() decorator
    """
    __yaml_tag_suffix__ = None
    """ placeholder for a class-wide yaml tag. It will be prefixed with '!yamlable/', stored in `YAMLABLE_PREFIX` """

    @classmethod
    def is_yaml_tag_supported(cls,
                              yaml_tag  # type: str
                              ):
        # type: (...) -> bool
        """
        Implementing classes should return True if they are able to decode yaml objects with this yaml tag.
        Default implementation relies on class attribute `__yaml_tag_suffix__` if provided, either manually or through
        the `@yaml_info` decorator.

        :param yaml_tag:
        :return:
        """
        if hasattr(cls, '__yaml_tag_suffix__') and cls.__yaml_tag_suffix__ is not None:
            return cls.__yaml_tag_suffix__ == yaml_tag and cls.__yaml_tag_suffix__ is not NONE_IGNORE_CHECKS
        else:
            raise NotImplementedError("class {} does not seem to have a non-None '__yaml_tag_suffix__' field. You can "
                                      "either create one manually or by decorating your class with @yaml_info. "
                                      "Alternately you should override the 'is_yaml_tag_supported' abstract method "
                                      "from YamlAble".format(cls))


def yaml_info(yaml_tag=None,     # type: str
              yaml_tag_ns=None   # type: str
              ):
    # type: (...) -> Callable[[Type[YA], Optional[str], Optional[str]], Type[YA]]
    """
    A simple class decorator to tag a class with a global yaml tag - that way you do not have to call `YamlAble` super
    constructor.

    You can either provide a full yaml tag suffix:

    ```python
    @yaml_info("com.example.MyFoo")
    class Foo(YamlAble):
        pass

    print(Foo.__yaml_tag_suffix__)  # yields "com.example.MyFoo"
    ```

    or simply provide a namespace, that will be appended with '.<class name>' :

    ```python
    @yaml_info(yaml_tag_ns="com.example")
    class Foo(YamlAble):
        pass

    print(MyFoo.__yaml_tag_suffix__)  # yields "com.example.Foo"
    ```

    In both cases, the suffix is appended at the end of the common yamlable prefix:

    ```python
    print(Foo().dumps_yaml())  # yields "!yamlable/com.example.Foo {}"
    ```

    :param yaml_tag: the complete yaml suffix.
    :param yaml_tag_ns: the yaml namespace. It will be appended with '.<cls.__name__>'
    :return:
    """
    def f(cls):
        return yaml_info_decorate(cls, yaml_tag=yaml_tag, yaml_tag_ns=yaml_tag_ns)
    return f


def yaml_info_decorate(cls,               # type: Type[YA]
                       yaml_tag=None,     # type: str
                       yaml_tag_ns=None   # type: str
                       ):
    # type: (...) -> Type[YA]
    """
    A simple class decorator to tag a class with a global yaml tag - that way you do not have to call `YamlAble` super
    constructor.

    You can either provide a full yaml tag suffix:

    ```python
    @yaml_info("com.example.MyFoo")
    class Foo(YamlAble):
        pass

    print(Foo.__yaml_tag_suffix__)  # yields "com.example.MyFoo"
    ```

    or simply provide a namespace, that will be appended with '.<class name>' :

    ```python
    @yaml_info(yaml_tag_ns="com.example")
    class Foo(YamlAble):
        pass

    print(MyFoo.__yaml_tag_suffix__)  # yields "com.example.Foo"
    ```

    In both cases, the suffix is appended at the end of the common yamlable prefix:

    ```python
    print(Foo().dumps_yaml())  # yields "!yamlable/com.example.Foo {}"
    ```

    :param cls:
    :param yaml_tag: the complete yaml suffix.
    :param yaml_tag_ns: the yaml namespace. It will be appended with '.<cls.__name__>'
    :return:
    """
    if yaml_tag_ns is not None:
        if yaml_tag is not None:
            raise ValueError("Only one of 'yaml_tag' and 'yaml_tag_ns' should be provided")
        # default: append the class name
        yaml_tag = yaml_tag_ns + '.' + cls.__name__

    if issubclass(cls, YamlObject2):
        if not yaml_tag.startswith('!'):
            raise ValueError("When extending YamlObject2, the `yaml_tag` field should contain the full yaml tag, "
                             "and should therefore start with !")
        cls.yaml_tag = yaml_tag

    elif issubclass(cls, YamlAble):
        if yaml_tag.startswith('!'):
            raise ValueError("When extending YamlAble, the `yaml_tag` field should only contain the yaml tag suffix, "
                             "and should therefore NOT start with !")
        cls.__yaml_tag_suffix__ = yaml_tag
    else:
        raise TypeError("classes tagged with @yaml_info should be subclasses of YamlAble or YamlObject2")

    return cls


# --------------------------------------Codecs-----------------------------------------------------------
def decode_yamlable(loader,
                    yaml_tag,  # type: str
                    node,      # type: MappingNode
                    **kwargs):
    # type: (...) -> YamlAble
    """
    The method used to decode YamlAble object instances

    :param loader:
    :param yaml_tag:
    :param node:
    :param kwargs:
    :return:
    """
    candidates = _get_all_subclasses(YamlAble)
    errors = dict()
    for clazz in candidates:
        try:
            if clazz.is_yaml_tag_supported(yaml_tag):
                constructor_args = read_yaml_node_as_dict(loader, node)
                return clazz.__from_yaml_dict__(constructor_args, yaml_tag=yaml_tag)
        except Exception as e:
            errors[clazz.__name__] = e

    raise TypeError("No YamlAble subclass found able to decode object !yamlable/" + yaml_tag + ". Tried classes: "
                    + str(candidates) + ". Caught errors: " + str(errors) + ". "
                    "Please check the value of <cls>.__yaml_tag_suffix__ on these classes. Note that this value may be "
                    "set using @yaml_info() so help(yaml_info) might help too.")


def encode_yamlable(dumper,
                    obj,                       # type: YamlAble
                    without_custom_tag=False,  # type: bool
                    **kwargs):
    # type: (...) -> MappingNode
    """
    The method used to encode YamlAble object instances

    :param dumper:
    :param obj:
    :param without_custom_tag: if this is set to True, the yaml tag !yamlable/<yaml_tag_suffix> will not be written to
        the document. Warning: if you do so, decoding the object will not be easy!
    :param kwargs:
    :return:
    """
    # Convert objects to a dictionary of their representation
    new_data = obj.__to_yaml_dict__()

    if without_custom_tag:
        # TODO check that it works
        return dumper.represent_mapping(None, new_data, flow_style=None)
    else:
        # Add the tag information
        if not hasattr(obj, '__yaml_tag_suffix__') or obj.__yaml_tag_suffix__ in {None, NONE_IGNORE_CHECKS}:
            raise NotImplementedError("object {} does not seem to have a non-None '__yaml_tag_suffix__' field. You "
                                      "can either create one manually or by decorating your class with @yaml_info."
                                      "".format(obj))
        yaml_tag = YAMLABLE_PREFIX + obj.__yaml_tag_suffix__
        return dumper.represent_mapping(yaml_tag, new_data, flow_style=None)


def register_yamlable_codec(loaders=(Loader, SafeLoader), dumpers=(Dumper, SafeDumper)):
    # type: (...) -> None
    """
    Registers the yamlable encoder and decoder with all pyYaml loaders and dumpers.

    :param loaders:
    :param dumpers:
    :return:
    """
    for loader in loaders:
        loader.add_multi_constructor(YAMLABLE_PREFIX, decode_yamlable)

    for dumper in dumpers:
        dumper.add_multi_representer(YamlAble, encode_yamlable)


# Register the YamlAble encoding and decoding functions
register_yamlable_codec()


def _get_all_subclasses(typ,             # type: Type[T]
                        recursive=True,  # type: bool
                        _memo=None       # type: Set[Type[Any]]
                        ):
    # type: (...) -> Iterable[Type[T]]
    """
    Returns all subclasses of `typ`
    Warning this does not support generic types.
    See parsyfiles.get_all_subclasses() if one day generic types are needed (commented lines below)

    :param typ:
    :param recursive: a boolean indicating whether recursion is needed
    :param _memo: internal variable used in recursion to avoid exploring subclasses that were already explored
    :return:
    """
    _memo = _memo or set()

    # if we have collected the subclasses for this already, return
    if typ in _memo:
        return []

    # else remember that we have collected them, and collect them
    _memo.add(typ)
    # if is_generic_type(typ):
    #     # We now use get_origin() to also find all the concrete subclasses in case the desired type is a generic
    #     sub_list = get_origin(typ).__subclasses__()
    # else:
    sub_list = typ.__subclasses__()

    # recurse
    result = []
    for t in sub_list:
        # only keep the origins in the list
        # to = get_origin(t) or t
        to = t
        # noinspection PyBroadException
        try:
            if to is not typ and to not in result and issubclass(to, typ):  # is_subtype(to, typ, bound_typevars={}):
                result.append(to)
        except Exception:
            # catching an error with is_subtype(Dict, Dict[str, int], bound_typevars={})
            pass

    # recurse
    if recursive:
        for typpp in sub_list:
            for t in _get_all_subclasses(typpp, recursive=True, _memo=_memo):
                # unfortunately we have to check 't not in sub_list' because with generics strange things happen
                # also is_subtype returns false when the parent is a generic
                if t not in sub_list and issubclass(t, typ):  # is_subtype(t, typ, bound_typevars={}):
                    result.append(t)

    return result


# ------------------------ Easy codecs ---------------
class YamlCodec(six.with_metaclass(ABCMeta, object)):
    """
    Represents a codec class, able to encode several object types into/from yaml, with potentially different yaml tag
    ids. It assumes that the objects are written as yaml dictionaries, and that they all have the same yaml tag prefix

    for example !mycodec/<yaml_tag_suffix>, where 'mycodec' is the yaml prefix associated with this codec.

    This allows the code to be pre-wired so that it is very easy to implement.
     - Decoding:
        - fill get_yaml_prefix
        - fill is_yaml_tag_supported to declare if a given yaml tag is supported or not
        - fill from_yaml_dict to create new instances of objects from a dictionary, according to the yaml tag
     - Encoding:
        - fill get_known_types
        - fill the to_yaml_dict
    """

    # -------------- decoding

    @classmethod
    @abstractmethod
    def get_yaml_prefix(cls):
        # type: (...) -> str
        """
        Implementors should return the yaml prefix associated tto this codec.
        :return:
        """

    @classmethod
    def decode(cls, loader,
               yaml_tag_suffix,  # type: str
               node,             # type: MappingNode
               **kwargs):
        # type: (...) -> Any
        """
        The method used to decode object instances

        :param loader:
        :param yaml_tag_suffix:
        :param node:
        :param kwargs: keyword arguments coming from pyyaml, not sure what you will find here.
        :return:
        """
        if cls.is_yaml_tag_supported(yaml_tag_suffix):
            constructor_args = read_yaml_node_as_dict(loader, node)
            return cls.from_yaml_dict(yaml_tag_suffix, constructor_args, **kwargs)

    @classmethod
    @abstractmethod
    def is_yaml_tag_supported(cls,
                              yaml_tag_suffix  # type: str
                              ):
        # type: (...) -> bool
        """
        Implementing classes should return True if they are able to decode yaml objects with this yaml tag.

        :param yaml_tag_suffix:
        :return:
        """

    @classmethod
    @abstractmethod
    def from_yaml_dict(cls,
                       yaml_tag_suffix,  # type: str
                       dct,              # type: Dict[str, Any]
                       **kwargs):
        # type: (...) -> Any
        """
        Implementing classes should create an object corresponding to the given yaml tag, using the given constructor
        arguments.

        :param dct:
        :param yaml_tag_suffix:
        :param kwargs: keyword arguments coming from pyyaml, not sure what you will find here.
        :return:
        """

    # --------------- encoding

    @classmethod
    @abstractmethod
    def get_known_types(cls):
        # type: (...) -> Iterable[Type[Any]]
        """
        Implementing classes should return an iterable of known object types.
        :return:
        """

    @classmethod
    def encode(cls, dumper, obj,
               without_custom_tag=False,  # type: bool
               **kwargs):
        # type: (...) -> MappingNode
        """
        The method used to encode YamlAble object instances

        :param dumper:
        :param obj:
        :param without_custom_tag: if this is set to True, the yaml tag !yamlable/<yaml_tag_suffix> will not be written to
            the document. Warning: if you do so, decoding the object will not be easy!
        :param kwargs: keyword arguments coming from pyyaml, not sure what you will find here.
        :return:
        """
        # Convert objects to a dictionary of their representation
        yaml_tag_suffix, obj_as_dict = cls.to_yaml_dict(obj)
        if not isinstance(obj_as_dict, collections.Mapping) or not isinstance(yaml_tag_suffix, str):
            raise TypeError("`to_yaml_dict` did not return correct results. It should return a tuple of "
                            "`yaml_tag_suffix, obj_as_dict`")

        if without_custom_tag:
            # TODO check that it works
            return dumper.represent_mapping(None, obj_as_dict, flow_style=None)
        else:
            # Add the tag information
            prefix = cls.get_yaml_prefix()
            if len(prefix) == 0 or prefix[-1] != '/':
                prefix = prefix + '/'
            yaml_tag = prefix + yaml_tag_suffix
            return dumper.represent_mapping(yaml_tag, obj_as_dict, flow_style=None)

    @classmethod
    @abstractmethod
    def to_yaml_dict(cls, obj):
        # type: (...) -> Tuple[str, Dict[str, Any]]
        """
        Implementors should encode the given object as a dictionary and also return the yaml tag that should be used to
        ensure correct decoding.

        :param obj:
        :return: a tuple where the first element is the yaml tag suffix, and the second is the dictionary representing
            the object
        """

    @classmethod
    def register_with_pyyaml(cls, loaders={Loader, SafeLoader}, dumpers={Dumper, SafeDumper}):
        # type: (...) -> None
        """
        Registers this codec with PyYaml, on the provided loaders and dumpers (default: all PyYaml loaders and dumpers).
         - The encoding part is registered for the object types listed in cls.get_known_types(), in order
         - The decoding part is registered for the yaml prefix in cls.get_yaml_prefix()

        :param loaders: the PyYaml loaders to register this codec with. By default all pyyaml loaders are considered
            (Loader, SafeLoader)
        :param dumpers: the PyYaml dumpers to register this codec with. By default all pyyaml loaders are considered
            (Dumper, SafeDumper)
        :return:
        """
        for loader in loaders:
            loader.add_multi_constructor(cls.get_yaml_prefix(), cls.decode)

        for dumper in dumpers:
            for t in cls.get_known_types():
                dumper.add_multi_representer(t, cls.encode)
