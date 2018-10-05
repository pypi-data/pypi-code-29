import collections
import json

Config = collections.namedtuple('Config', 'docker max_age interval bucket_prefix')


def load_config(path: str) -> tuple:
    """
    Loads configuration from json file
    :param path:
    :return:
    """

    with open(path) as json_data:
        json_config = json.load(json_data)
    tuple_config = Config(docker=json_config["docker"], max_age=json_config["max_age"],
                          interval=json_config["interval"], bucket_prefix=json_config["bucket_prefix"])
    return tuple_config
