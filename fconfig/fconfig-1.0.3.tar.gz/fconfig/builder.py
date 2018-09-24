import os
import pkgutil

from typing import List, Tuple, TypeVar, Dict
from fconfig.config_data_object import ConfigDataObject
from mako.lookup import TemplateLookup
from mako.template import Template

from fconfig import loader
from fconfig.loader import ConfigSource
from fconfig.config import Config

C = TypeVar('C', bound=Config)


def get_class_name(snake_case_property_name):
	components = snake_case_property_name.split('_')
	return "".join(x.title() for x in components)


class Builder:

	def __init__(self, config_package: str, main_module_name: str, root_class_name: str, output_dir: str,
				 parent_config: List[Tuple[C, str]]):
		self.config_package = config_package
		self.main_module_name = main_module_name
		self.root_class_name = root_class_name
		self.output_dir = output_dir
		self.parent_config = parent_config
		self.parent_config_map: Dict[str, object] = {}
		for pc in parent_config:
			self.parent_config_map[pc[1]] = pc[0]

	def build_config(self):
		"""
		Starts the building process.
		"""

		self._delete_old_files()

		parent_sources = loader.get_config_sources_from_def(self.parent_config)

		source = loader.get_master_config_content(self.config_package)

		config_map = loader.load_config_data(source, *parent_sources, use_builder_directives=True)
		self._generate_config(config_map, self.root_class_name, True)

		self._create_init()

	def _delete_old_files(self):
		if os.path.isdir(self.output_dir):
			for the_file in os.listdir(self.output_dir):
				file_path = os.path.join(self.output_dir, the_file)
				try:
					if os.path.isfile(file_path):
						os.unlink(file_path)
					# elif os.path_in_config.isdir(file_path): shutil.rmtree(file_path)
				except Exception as e:
					print(e)

	def _generate_config(self, config_map: ConfigDataObject, map_name: str, is_root: bool=False):
		properties = {}
		object_properties: Dict[str, Tuple[str,any]] = {}
		array_properties = {}
		for key, value in config_map.items():
			if isinstance(value, ConfigDataObject):
				if value.is_array:
					if isinstance(value.get(0), ConfigDataObject):
						item_name \
							= config_map.path + "_" + key + "_item" if config_map.path else key + "_item"
						self._generate_config(value.get(0), item_name)
					array_properties[key] = value
				else:
					# parent config test
					if value.path in self.parent_config_map:
						import_module = self.parent_config_map[value.path].__module__
						class_name = self.parent_config_map[value.path].__name__
						is_parent = True
					else:
						self._generate_config(value, key)
						import_module = "{}.{}.{}".format(self.main_module_name, self.output_dir, key)
						class_name = get_class_name(key)
						is_parent = False
					object_properties[key] = (import_module, class_name, value, is_parent)
			else:
				properties[key] = value

		template_filename = 'config_root_template.txt' if is_root else 'config_template.txt'
		# template_filename = 'config_template.txt'
		template_data = pkgutil.get_data("fconfig.templates", template_filename)
		lookup = TemplateLookup(module_directory="/tmp")
		class_template = Template(template_data, lookup=lookup)

		if not os.path.exists(self.output_dir):
			os.makedirs(self.output_dir)

		output_file = open("{}/{}.py".format(self.output_dir, map_name), 'w')
		class_name = get_class_name(map_name)
		if is_root:
			parent_parameter_strings = []
			for pc in self.parent_config:
				parent_parameter_strings.append("({}, '{}')".format(pc[0].__name__, pc[1]))
			parent_parameter_strings.append("({}, None)".format(class_name))
			output_file.write(class_template.render(properties=properties, object_properties=object_properties,
													array_properties=array_properties,
													class_name=class_name, map_name=map_name,
													parent_parameter_string=", ".join(parent_parameter_strings)))
		else:
			output_file.write(class_template.render(properties=properties, object_properties=object_properties,
				array_properties=array_properties, class_name=class_name))

	def _create_init(self):
		open("{}/__init__.py".format(self.output_dir), 'a').close()
