# -*- coding: utf-8 -*-

from django.utils.translation import gettext as _


class Enum(object):
	DEFAULT = 0

	local = (_('-'),)

	def __init__(self):
		# Check if it has valid keys and values
		if not self.length() > 0:
			raise Exception("Class '%s' must have at least one decleared constant variable." % self.__class__.__name__)
		if not self.check_local():
			raise Exception("'local' tuple must have amount of string as there are variable in class '%s'." % self.__class__.__name__)

	def length(self):
		return len(self.get_keys())

	def check_local(self):
		if self.local:
			return len(self.local) == self.length()

	@classmethod
	def get_keys(cls):
		# Get all variables that are spelled with capitals
		return [key for key in cls.__dict__.keys() if cls.is_valid_key(key)]

	@staticmethod
	def is_valid_key(value):
		# Filter all builtin variables starts and ends with double underscore
		return not value.startswith('__') and not value.endswith('__') and value.isupper()

	@classmethod
	def get_values(cls):
		return [cls.__dict__.get(key) for key in cls.get_keys()]

	@classmethod
	def get_sorted_values(cls):
		return sorted([cls.__dict__.get(key) for key in cls.get_keys()])

	@classmethod
	def get_as_tuple_list(cls):
		# Return unsorted list of tuples formatted as [(KEY, value), ...]
		return [(key, cls.__dict__.get(key)) for key in cls.get_keys()]

	@classmethod
	def get_as_dict(cls):
		# Return unsorted dict with class variables
		items = {}
		for key, value in cls.get_as_tuple_list():
			items[key] = value
		return items

	@classmethod
	def validate_values(cls, fail_silently=False):
		# Check that all values defined are integers
		for value in cls.get_values():
			if not cls.is_valid_value(value):
				if fail_silently:
					return False
				else:
					raise ValueError("Value '%s' is not a valid integer." % value)

	@classmethod
	def is_in_keys(cls, value):
		return value in cls.get_keys()

	@classmethod
	def is_in_values(cls, value):
		return value in cls.get_values()

	@classmethod
	def choices(cls):
		items = sorted(cls.get_as_tuple_list(), key=lambda item: item[1])
		return cls.prepend_default_first([(item[1], cls.local[index]) for index, item in enumerate(items)])

	@classmethod
	def get_dict(cls):
	 return cls.__dict__

	@classmethod
	def prepend_default_first(cls, temp_list):
		if not cls.is_default_overridden():
		    return [(Enum.DEFAULT, Enum.local[0])] + temp_list
		else:
		    return temp_list

	@classmethod
	def is_default_overridden(cls):
		#Checks whether the sub-class has overwritten the DEFAULT key
		return cls.is_in_keys('DEFAULT') or cls.is_in_values(0)

	@staticmethod
	def is_valid_value(value):
		try:
		    value = int(value)
		    return True
		except TypeError:
		    return False
		except ValueError:
		    return False

