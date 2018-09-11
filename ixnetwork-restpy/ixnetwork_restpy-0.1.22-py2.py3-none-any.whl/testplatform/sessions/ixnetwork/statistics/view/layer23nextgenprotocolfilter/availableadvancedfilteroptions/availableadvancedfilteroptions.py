from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableAdvancedFilterOptions(Base):
	"""The AvailableAdvancedFilterOptions class encapsulates a system managed availableAdvancedFilterOptions node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AvailableAdvancedFilterOptions property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'availableAdvancedFilterOptions'

	def __init__(self, parent):
		super(AvailableAdvancedFilterOptions, self).__init__(parent)

	@property
	def Operators(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('operators')

	@property
	def Stat(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('stat')

	def find(self, Operators=None, Stat=None):
		"""Finds and retrieves availableAdvancedFilterOptions data from the server.

		All named parameters support regex and can be used to selectively retrieve availableAdvancedFilterOptions data from the server.
		By default the find method takes no parameters and will retrieve all availableAdvancedFilterOptions data from the server.

		Args:
			Operators (str): 
			Stat (str): 

		Returns:
			self: This instance with found availableAdvancedFilterOptions data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
