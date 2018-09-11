from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DynamicFrameSize(Base):
	"""The DynamicFrameSize class encapsulates a system managed dynamicFrameSize node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DynamicFrameSize property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'dynamicFrameSize'

	def __init__(self, parent):
		super(DynamicFrameSize, self).__init__(parent)

	@property
	def FixedSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('fixedSize')
	@FixedSize.setter
	def FixedSize(self, value):
		self._set_attribute('fixedSize', value)

	@property
	def HighLevelStreamName(self):
		"""The name of the high level stream

		Returns:
			str
		"""
		return self._get_attribute('highLevelStreamName')

	@property
	def RandomMax(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('randomMax')
	@RandomMax.setter
	def RandomMax(self, value):
		self._set_attribute('randomMax', value)

	@property
	def RandomMin(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('randomMin')
	@RandomMin.setter
	def RandomMin(self, value):
		self._set_attribute('randomMin', value)

	@property
	def TrafficItemName(self):
		"""The name of the parent traffic item.

		Returns:
			str
		"""
		return self._get_attribute('trafficItemName')

	@property
	def Type(self):
		"""

		Returns:
			str(fixed|random)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	def find(self, FixedSize=None, HighLevelStreamName=None, RandomMax=None, RandomMin=None, TrafficItemName=None, Type=None):
		"""Finds and retrieves dynamicFrameSize data from the server.

		All named parameters support regex and can be used to selectively retrieve dynamicFrameSize data from the server.
		By default the find method takes no parameters and will retrieve all dynamicFrameSize data from the server.

		Args:
			FixedSize (number): 
			HighLevelStreamName (str): The name of the high level stream
			RandomMax (number): 
			RandomMin (number): 
			TrafficItemName (str): The name of the parent traffic item.
			Type (str(fixed|random)): 

		Returns:
			self: This instance with found dynamicFrameSize data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
