import pkg_resources
__version__ = pkg_resources.get_distribution('panoptes_aggregation').version


def append_version(results):
    if isinstance(results, list):
        for result in results:
            result['aggregation_version'] = __version__
    else:
        results['aggregation_version'] = __version__


def remove_version(input_list):
    for item in input_list:
        if 'aggregation_version' in item:
            del item['aggregation_version']
