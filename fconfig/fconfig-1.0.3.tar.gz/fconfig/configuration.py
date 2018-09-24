import logging
import pkgutil
import os
import sys
import inspect
import argparse
import fconfig.loader as loader

# from os.path import dirname as dirname
from typing import Tuple, TypeVar, Type, Union
from fconfig.builder import Builder
from fconfig.config import Config
from fconfig.loader import ConfigSource


C = TypeVar('C', bound=Config)

# arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-lc', help='Local config file path')
args, _unknown_args = arg_parser.parse_known_args()

logging.basicConfig(level=logging.INFO)


def generate_config(*parent_config: Tuple[C, str]):
	"""
	At this time, this function has to be called from the project root!
	"""
	root_module_name = os.path.basename(os.path.normpath(os.path.dirname(sys.modules['__main__'].__file__)))
	root_config_object_name_name = root_module_name + "_config"
	# default_config_file_name = root_module_name + ".cfg"

	config_package: str = ".".join((root_module_name, loader.DEFAULT_CONFIG_PACKAGE))

	Builder(config_package, root_module_name, root_config_object_name_name,
			loader.DEFAULT_GENERATED_CONFIG_PACKAGE, parent_config).build_config()


def load(*config_def: Tuple[Type[Config], Union[str, None]]):
	config_sources = loader.get_config_sources_from_def(config_def)

	# default_config_source = ConfigSource(_get_project_main_module_name(generated_config), key_in_client)
	# config_sources.append(default_config_source)
	#
	# if client_generated_config:
	# 	config_source = client_config_file_path if client_config_file_path \
	# 		else _get_project_main_module_name(client_generated_config)
	# 	default_client_config_source = ConfigSource(config_source)
	# 	config_sources.append(default_client_config_source)

	if args.lc:
		local_config_source = ConfigSource(loader.get_local_config_content(args.lc))
		config_sources.append(local_config_source)

	logging.info("Loading config for project {} (can be overwritten later)".format(config_def[-1][0].__name__))
	config = loader.load_config_data(*config_sources)

	config_dict = config.get_internal_objects()

	# if client_generated_config:
	# 	generated_config.fill(config_dict[key_in_client])
	# 	client_generated_config.fill(config_dict)
	# else:
	return config_def[-1][0](config_dict)


def _get_project_main_module_name(generated_config: type):
	return generated_config.__module__.split(".")[0]
	# return pkgutil.get_data("roadmaptools", DEFAULT_CONFIG_FILE_NAME)




# def _get_config_file_name(generated_config: type) -> str:
# 	os.path.basename(os.path.normpath(dirname(dirname(inspect.getfile(generated_config))))) + "_config"

# def _get_config_file_path(generated_config: type) -> str:
# 	dirname(dirname(inspect.getfile(generated_config))) + "/" + DEFAULT_CONFIG_FILE_NAME

