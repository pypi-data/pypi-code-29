from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DiscoveredInterface(Base):
	"""The DiscoveredInterface class encapsulates a system managed discoveredInterface node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DiscoveredInterface property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'discoveredInterface'

	def __init__(self, parent):
		super(DiscoveredInterface, self).__init__(parent)

	@property
	def InterfaceName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('interfaceName')

	@property
	def State(self):
		"""

		Returns:
			str(assigned|available|unusable)
		"""
		return self._get_attribute('state')

	def find(self, InterfaceName=None, State=None):
		"""Finds and retrieves discoveredInterface data from the server.

		All named parameters support regex and can be used to selectively retrieve discoveredInterface data from the server.
		By default the find method takes no parameters and will retrieve all discoveredInterface data from the server.

		Args:
			InterfaceName (str): 
			State (str(assigned|available|unusable)): 

		Returns:
			self: This instance with found discoveredInterface data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
