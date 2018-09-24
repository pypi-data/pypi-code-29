from string import Formatter

# cannot import because python does not support circular dependencies :(
# from fconfig.config_data_object import ConfigDataObject


class ConfigProperty:

	def __init__(self, config_data_object, key, value):
		self.config_data_object = config_data_object
		self.key = key
		self.value = value

	def set_value(self, new_value):
		self.config_data_object.put(self.key, new_value)

	def get_path(self):
		if not self.config_data_object.path:
			return self.key
		elif isinstance(self.key, int):
			return "{}[{}]".format(self.config_data_object.path, self.key)
		else:
			return "{}.{}".format(self.config_data_object.path, self.key)

	def to_string(self) -> str:
		return self.get_path() + ": " + str(self.value)

	def __str__(self) -> str:
		return self.to_string()

	def __repr__(self) -> str:
		return self.to_string()



