"""YAML IO."""
from joeutils.io.file_io import read_contents


def yaml_load_clean(data):
    """Read YAML.

    Handles dependencies.

    Raises:
        YAMLError

    Returns:
        dict: Data.
    """
    from yaml import load, YAMLError
    try:
        return load(read_contents(data))
    except YAMLError:
        raise YAMLError('YAMLError: An unexpected error occurred when '
                        'attempting to read supplied YAML.')


def yaml_dump_clean(data):
    """Dump YAML in highly readable format and preserving key order.

    Handles dependencies.

    # TODO: Upgrade to ruamel package to preserve order -
    # https://stackoverflow.com/questions/31605131
    # /dumping-a-dictionary-to-a-yaml-file-while-preserving-order

    Returns:
        str: YAML formatted string.
    """
    import yaml
    return yaml.dump(data=data, default_flow_style=False)
