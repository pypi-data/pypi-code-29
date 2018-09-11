from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Bool(Base):
	"""The Bool class encapsulates a system managed bool node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Bool property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'bool'

	def __init__(self, parent):
		super(Bool, self).__init__(parent)

	@property
	def Default(self):
		"""(Read only) Parameter default value.

		Returns:
			bool
		"""
		return self._get_attribute('default')

	@property
	def Value(self):
		"""Parameter bool value.

		Returns:
			bool
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def find(self, Default=None, Value=None):
		"""Finds and retrieves bool data from the server.

		All named parameters support regex and can be used to selectively retrieve bool data from the server.
		By default the find method takes no parameters and will retrieve all bool data from the server.

		Args:
			Default (bool): (Read only) Parameter default value.
			Value (bool): Parameter bool value.

		Returns:
			self: This instance with found bool data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
