from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NestedCounter(Base):
	"""The NestedCounter class encapsulates a system managed nestedCounter node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the NestedCounter property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'nestedCounter'

	def __init__(self, parent):
		super(NestedCounter, self).__init__(parent)

	@property
	def AvailableWidths(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableWidths')

	@property
	def BitOffset(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('bitOffset')
	@BitOffset.setter
	def BitOffset(self, value):
		self._set_attribute('bitOffset', value)

	@property
	def InnerLoopIncrementBy(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopIncrementBy')
	@InnerLoopIncrementBy.setter
	def InnerLoopIncrementBy(self, value):
		self._set_attribute('innerLoopIncrementBy', value)

	@property
	def InnerLoopLoopCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopLoopCount')
	@InnerLoopLoopCount.setter
	def InnerLoopLoopCount(self, value):
		self._set_attribute('innerLoopLoopCount', value)

	@property
	def InnerLoopRepeatValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopRepeatValue')
	@InnerLoopRepeatValue.setter
	def InnerLoopRepeatValue(self, value):
		self._set_attribute('innerLoopRepeatValue', value)

	@property
	def OuterLoopIncrementBy(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('outerLoopIncrementBy')
	@OuterLoopIncrementBy.setter
	def OuterLoopIncrementBy(self, value):
		self._set_attribute('outerLoopIncrementBy', value)

	@property
	def OuterLoopLoopCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('outerLoopLoopCount')
	@OuterLoopLoopCount.setter
	def OuterLoopLoopCount(self, value):
		self._set_attribute('outerLoopLoopCount', value)

	@property
	def StartValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('startValue')
	@StartValue.setter
	def StartValue(self, value):
		self._set_attribute('startValue', value)

	@property
	def Width(self):
		"""

		Returns:
			str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)
		"""
		return self._get_attribute('width')
	@Width.setter
	def Width(self, value):
		self._set_attribute('width', value)

	def find(self, AvailableWidths=None, BitOffset=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, InnerLoopRepeatValue=None, OuterLoopIncrementBy=None, OuterLoopLoopCount=None, StartValue=None, Width=None):
		"""Finds and retrieves nestedCounter data from the server.

		All named parameters support regex and can be used to selectively retrieve nestedCounter data from the server.
		By default the find method takes no parameters and will retrieve all nestedCounter data from the server.

		Args:
			AvailableWidths (list(str)): 
			BitOffset (number): 
			InnerLoopIncrementBy (number): 
			InnerLoopLoopCount (number): 
			InnerLoopRepeatValue (number): 
			OuterLoopIncrementBy (number): 
			OuterLoopLoopCount (number): 
			StartValue (number): 
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): 

		Returns:
			self: This instance with found nestedCounter data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
