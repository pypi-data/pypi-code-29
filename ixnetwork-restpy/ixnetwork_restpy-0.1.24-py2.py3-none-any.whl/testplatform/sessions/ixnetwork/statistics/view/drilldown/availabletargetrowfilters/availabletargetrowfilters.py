from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableTargetRowFilters(Base):
	"""The AvailableTargetRowFilters class encapsulates a system managed availableTargetRowFilters node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AvailableTargetRowFilters property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'availableTargetRowFilters'

	def __init__(self, parent):
		super(AvailableTargetRowFilters, self).__init__(parent)

	def find(self):
		"""Finds and retrieves availableTargetRowFilters data from the server.

		All named parameters support regex and can be used to selectively retrieve availableTargetRowFilters data from the server.
		By default the find method takes no parameters and will retrieve all availableTargetRowFilters data from the server.

		Returns:
			self: This instance with found availableTargetRowFilters data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
