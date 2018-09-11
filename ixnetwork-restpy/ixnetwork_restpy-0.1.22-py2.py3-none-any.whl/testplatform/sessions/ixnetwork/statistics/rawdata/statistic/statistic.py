from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Statistic(Base):
	"""The Statistic class encapsulates a system managed statistic node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Statistic property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'statistic'

	def __init__(self, parent):
		super(Statistic, self).__init__(parent)

	@property
	def Caption(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('caption')

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	def find(self, Caption=None, Enabled=None):
		"""Finds and retrieves statistic data from the server.

		All named parameters support regex and can be used to selectively retrieve statistic data from the server.
		By default the find method takes no parameters and will retrieve all statistic data from the server.

		Args:
			Caption (str): 
			Enabled (bool): 

		Returns:
			self: This instance with found statistic data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
