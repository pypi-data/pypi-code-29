import logging
import re
import sys

from typing import List, Union
from fconfig.config_data_object import ConfigDataObject
# from fconfig.loader import ConfigSource

NAME_PATTERN_STRING = "[a-zA-Z][a-zA-Z0-9_]+"

NUMBER_PATTERN = re.compile("^([0-9])")
BOOLEAN_PATTERN = re.compile(r"^(true|false)$")
TRUE_PATTERN = re.compile("^(true)$")
OPERATOR_PATTERN = re.compile(r"[+\-]")
REFERENCE_PATTERN = re.compile(r"\$({}(\.{})*)".format(NAME_PATTERN_STRING, NAME_PATTERN_STRING))


def parse_simple_value(value: str):
	if NUMBER_PATTERN.match(value):
		if "." in value:
			return float(value)
		else:
			return int(value)
	elif BOOLEAN_PATTERN.match(value):
		return True if TRUE_PATTERN.match(value) else False
	elif value.startswith("'"):
		return value.replace("'", "")
	elif value.startswith("\""):
		return value.replace("\"", "")
	else:
		logging.critical("Unsupported value type: %s", value)


class Reference:
	def __init__(self, reference_token: str):
		self.path_string = reference_token
		self.path = reference_token.split(".")
		self.path[0] = self.path[0][1:]

	def add_prefix(self, prefix: str):
		new_path = []
		new_path.append(prefix)
		for part in self.path:
			new_path.append(part)
		self.path = new_path
		self.path_string = "$" + ".".join(new_path)



class Parser:
	WHITESPACE_LINE_PATTERN = re.compile(r"^\s*$")
	WHITESPACE_PATTERN = re.compile(r"[\r\n\s]+")
	# INDENTION_PATTERN = re.compile("^(    |	)*")
	KEY_PATTERN = re.compile("^({})(:)".format(NAME_PATTERN_STRING))
	VALUE_PATTERN = re.compile(r"^\s*([^\s]+.*)")
	BUILDER_DIRECTIVE_PATTERN = re.compile(r"^!([^\s]*)")
	TOKEN_PATTERN = re.compile(r"[^\s'\"]+|'[^']*'|\"[^\"]*\"")
	# LINE_END_PATTERN = re.compile(r"[\r\n]+")

	# @staticmethod
	# def strip_indention(line):
	# 	line = Parser.INDENTION_PATTERN.sub("", line)
	# 	return line
	#
	# @staticmethod
	# def remove_line_ends(line):
	# 	line = Parser.LINE_END_PATTERN.sub("", line)
	# 	return line

	# @staticmethod
	# def parse_expression(value):
	#
	# 	# do not parse before references are resolved
	# 	if contains_variable(value):
	# 		return value
	# 	else:
	# 		return parse_simple_value(value)

	@staticmethod
	def parse_value_token(token: str) -> Union[str, int, bool, float, Reference]:
		if token.startswith("$"):
			return Reference(token)
		# operators are left as strings now
		elif OPERATOR_PATTERN.match(token):
			return token
		else:
			return parse_simple_value(token)

	@staticmethod
	def terminate():
		sys.exit(1)

	def __init__(self, use_builder_directives=False):
		self.config = ConfigDataObject(False)
		self.object_stack: List[ConfigDataObject] = []
		self.use_builder_directives = use_builder_directives
		self.current_object: ConfigDataObject = self.config
		self.current_key: Union[str, int] = None
		self.current_value = None
		self.in_array = False
		self.skip_next_object = False

	def parse_config_source(self, config_source: str)-> ConfigDataObject:
		for line in config_source:

			# skip blank lines
			if Parser.WHITESPACE_LINE_PATTERN.match(line):
				continue

			# # comment line
			# elif "#" in line:
			#
			# 	# possible comment processing
			# 	pass

			# # directive line
			# elif line.startswith("!"):
			# 	if self.use_builder_directives:
			# 		self.resolve_builder_directive(line)
			
			tokens = self.tokenize(line)
			first_token = tokens[0]

			# comment line
			if first_token.startswith("#"):
				# possible comment processing
				continue

			# new array or object
			elif first_token == "{" or first_token == "[":
				self.process_open_bracket(first_token)

			# close object
			elif first_token == "}" or first_token == "]":
				self.process_close_bracket()

			# # new array or object
			# if "{" in line or "[" in line:
			#
			# 	# push old context to stack
			# 	self.object_stack.append(self.current_object)
			#
			# 	self.in_array = "[" in line
			#
			# 	self.current_object = ConfigDataObject(self.in_array, self.current_object, self.current_key)
			#
			# 	# add new object to parent object
			# 	if self.skip_next_object:
			# 		self.skip_next_object = False
			# 	else:
			# 		self.object_stack[-1].put(self.current_key, self.current_object)
			# 	if self.in_array:
			# 		self.current_key = 0
			#
			# elif "}" in line or "]" in line:
			# 	self.current_object = self.object_stack.pop()
			# 	if self.current_object.is_array:
			# 		self.in_array = True
			# 		self.current_key = self.current_object.getSize()
			# 	else:
			# 		self.in_array = False
			else:
				self.parse_line(tokens)

		return self.config

	# def resolve_builder_directive(self, line):
	# 	match = self.BUILDER_DIRECTIVE_PATTERN.match(line)
	# 	directive = match.group(1)
	# 	if directive == "parent":
	# 		self.skip_next_object = True

	def tokenize(self, line: str) -> List[str]:
		# return self.WHITESPACE_PATTERN.split(line)
		return self.TOKEN_PATTERN.findall(line)

	def process_open_bracket(self, first_token: str):
		# push old context to stack
		self.object_stack.append(self.current_object)

		self.in_array = first_token == "["

		self.current_object = ConfigDataObject(self.in_array, self.current_object, self.current_key)

		# add new object to parent object
		if self.skip_next_object:
			self.skip_next_object = False
		else:
			self.object_stack[-1].put(self.current_key, self.current_object)
		if self.in_array:
			self.current_key = 0

	def process_close_bracket(self):
		self.current_object = self.object_stack.pop()
		if self.current_object.is_array:
			self.in_array = True
			self.current_key = self.current_object.get_size()
		else:
			self.in_array = False

	def parse_line(self, tokens: List[str]):
		# line = self.strip_indention(line)

		# line = self.remove_line_ends(line)

		if not self.in_array:
			self.parse_key(tokens[0])

			# remove key from tokens
			tokens = tokens[1:]

		if self.parse_value(tokens):
			self.current_object.put(self.current_key, self.current_value)

		if self.in_array:
			self.current_key += 1

	def parse_key(self, line):
		match = Parser.KEY_PATTERN.match(line)
		if match:
			self.current_key = match.group(1)
		else:
			logging.critical("No key can be parsed from string '%s', parsing will terminate.", line)
			self.terminate()

	def parse_value(self, tokens: List[str]) -> bool:
		# match = Parser.VALUE_PATTERN.match(line)
		if tokens:
			# self.current_value = self.parse_expression(match.group(1))
			parsed_tokens = []
			for token in tokens:
				parsed_tokens.append(self.parse_value_token(token))
			self.current_value = parsed_tokens
			return True
		return False


