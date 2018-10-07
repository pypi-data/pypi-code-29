from ruamel import yaml

from .extensions import Extension
from .utils import dict_find_pattern
from .validator import Validator


class DictMentor(object):
    """
    Augments a given dictionary by applying so called extensions.
    """

    def __init__(self, *extensions):
        self._extensions = []
        self._init_extensions(extensions)

    def _init_extensions(self, extensions):
        if extensions is None or not extensions:
            return

        if not Validator.is_real_iterable(extensions=extensions):
            extensions = [extensions]

        for m in extensions:
            self.bind(m)

    def bind(self, extension):
        """
        Add any predefined or custom extension.

        Args:
            extension: Extension to add to the processor.

        Returns:
            The DictMentor itself for chaining.
        """
        if not Extension.is_valid_extension(extension):
            raise ValueError("Cannot bind extension due to missing interface requirements")
        self._extensions.append(extension)

        return self

    def augment(self, dct, document=None):
        """
        Augments the given dictionary by using all the bound extensions.

        Args:
            dct: Dictionary to augment.
            document: The document the dictionary was loaded from.

        Returns:
            The augmented dictionary.
        """
        Validator.instance_of(dict, raise_ex=True, dct=dct)

        # Apply any configured loader
        for instance in self._extensions:
            nodes = list(dict_find_pattern(dct, **instance.config()))
            for parent, k, v in nodes:
                parent.pop(k)
                fragment = instance.apply(
                    mentor=self,
                    document=document or dct,
                    dct=dct,
                    parent_node=parent,
                    node=(k, v)
                )
                if fragment is not None:
                    parent.update(fragment)

        return dct

    @classmethod
    def _load_plain_yaml(cls, yaml_):
        """
        Will just load the yaml without executing any extensions. You will get the plain dictionary without
        augmentation. It is equivalent to just perform `yaml.safe_load`. Besides that you can specify a stream, a file
        or just a string that contains yaml/json data.

        Examples:
            >>> jstr = '{"a":1, "b": {"c": 3, "d": "d"}}'
            >>> d = DictMentor._load_plain_yaml(jstr)
            >>> d['a'], d['b']['c'], d['b']['d']
            (1, 3, 'd')

        Args:
            yaml_: Whether a stream (e.g. file pointer), a file name of an existing file or string containing
                yaml/json data.

        Returns:
            Returns the yaml_ data as a python dictionary.
        """
        if Validator.is_stream(yaml_=yaml_):
            return yaml.safe_load(yaml_)
        if Validator.is_file(yaml_=yaml_):
            with open(yaml_) as fp:
                return yaml.safe_load(fp)
        if Validator.instance_of(target_type=str, yaml_=yaml_):
            return yaml.safe_load(yaml_)

        raise TypeError("Argument 'yaml_' is whether a stream, nor a file, nor a string")

    def load_yaml(self, yaml_):
        """
        Loads a partial yaml and augments it. A partial yaml in this context is a yaml that is syntactically correct,
        but is not yet complete in terms of content.
        The yaml will be completed by augmenting with some external resources and/or executing so called extensions.

        Args:
            yaml_: Whether a stream (e.g. file pointer), a file name of an existing file or string containing yaml data.

        Returns:
            Returns the yaml data as an augmented python dictionary.
        """
        return self.augment(self._load_plain_yaml(yaml_), document=yaml_)
