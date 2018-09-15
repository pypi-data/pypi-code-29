from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailablePortFilter(Base):
	"""The AvailablePortFilter class encapsulates a system managed availablePortFilter node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AvailablePortFilter property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'availablePortFilter'

	def __init__(self, parent):
		super(AvailablePortFilter, self).__init__(parent)

	@property
	def Name(self):
		"""The name of the port filter.

		Returns:
			str
		"""
		return self._get_attribute('name')

	def find(self, Name=None):
		"""Finds and retrieves availablePortFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve availablePortFilter data from the server.
		By default the find method takes no parameters and will retrieve all availablePortFilter data from the server.

		Args:
			Name (str): The name of the port filter.

		Returns:
			self: This instance with found availablePortFilter data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
