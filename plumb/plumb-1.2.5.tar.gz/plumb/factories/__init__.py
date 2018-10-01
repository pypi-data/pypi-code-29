import json
from functools import partial

from plumb import kafka, rabbitmq, redis, memory
from plumb.aws import sns, sqs

_SOURCE_CONSTRUCTORS_DICT = {
    'sqs': sqs.Source,
    'kafka': kafka.Source,
    'rabbitmq': rabbitmq.Source,
    'redis': redis.Source,
    'memory': memory.Source
}

_SINK_CONSTRUCTORS_DICT = {
    'sns': sns.Sink,
    'sqs': sqs.Sink,
    'kafka': kafka.Sink,
    'rabbitmq': rabbitmq.Sink,
    'redis': redis.Sink,
    'memory': memory.Sink
}


def create_from_config(constructors_dict: dict, config: dict):
    """
    Returns a list of either Sinks of Sources, depending on the specified configuration.
    """
    if isinstance(config, str):
        config = json.loads(config)
    elif not isinstance(config, dict):
        raise TypeError('Config should be either a string or a dict not a {}'.format(type(config)))
    sources = list()
    for key in config.keys():
        if key in constructors_dict:
            constructor = constructors_dict[key]
            if isinstance(config[key], list):
                for sink_config in config[key]:
                    sources.append(constructor(**sink_config))
            elif isinstance(config[key], dict):
                sources.append(constructor(**config[key]))
            else:
                raise TypeError('The config for a source should be a dict in case of a single source'
                                'or list in case of many sources not a {}'.format(type(config[key])))
        else:
            raise ValueError('Unknown sink module {}. Possible values are {}'.format(key, constructors_dict.keys()))
    return sources


create_sinks_from_config = partial(create_from_config, _SINK_CONSTRUCTORS_DICT)

create_sources_from_config = partial(create_from_config, _SOURCE_CONSTRUCTORS_DICT)
