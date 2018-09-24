
# from pkg_resources import resource_string

import fconfig.loader as loader

from fconfig.config_data_object import ConfigDataObject


TEST_CONFIG_PACKAGE = "fconfig.test.resources"


def load_test_config_file(*test_filename: str) -> ConfigDataObject:
	sources = []
	for fn in test_filename:
		source = loader.get_config_content_from_resource(TEST_CONFIG_PACKAGE, fn)
		sources.append(source)
	config_map = loader.load_config_data(*sources)
	return config_map
