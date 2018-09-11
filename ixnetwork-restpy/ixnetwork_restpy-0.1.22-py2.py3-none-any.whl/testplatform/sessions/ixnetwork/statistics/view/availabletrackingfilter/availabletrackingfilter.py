from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableTrackingFilter(Base):
	"""The AvailableTrackingFilter class encapsulates a system managed availableTrackingFilter node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AvailableTrackingFilter property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'availableTrackingFilter'

	def __init__(self, parent):
		super(AvailableTrackingFilter, self).__init__(parent)

	@property
	def Constraints(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('constraints')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def TrackingType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('trackingType')

	@property
	def ValueType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('valueType')

	def find(self, Constraints=None, Name=None, TrackingType=None, ValueType=None):
		"""Finds and retrieves availableTrackingFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve availableTrackingFilter data from the server.
		By default the find method takes no parameters and will retrieve all availableTrackingFilter data from the server.

		Args:
			Constraints (list(str)): 
			Name (str): 
			TrackingType (str): 
			ValueType (str): 

		Returns:
			self: This instance with found availableTrackingFilter data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
