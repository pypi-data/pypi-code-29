from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DynamicRate(Base):
	"""The DynamicRate class encapsulates a system managed dynamicRate node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DynamicRate property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'dynamicRate'

	def __init__(self, parent):
		super(DynamicRate, self).__init__(parent)

	@property
	def BitRateUnitsType(self):
		"""

		Returns:
			str(bitsPerSec|bytesPerSec|kbitsPerSec|kbytesPerSec|mbitsPerSec|mbytesPerSec)
		"""
		return self._get_attribute('bitRateUnitsType')
	@BitRateUnitsType.setter
	def BitRateUnitsType(self, value):
		self._set_attribute('bitRateUnitsType', value)

	@property
	def EnforceMinimumInterPacketGap(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('enforceMinimumInterPacketGap')
	@EnforceMinimumInterPacketGap.setter
	def EnforceMinimumInterPacketGap(self, value):
		self._set_attribute('enforceMinimumInterPacketGap', value)

	@property
	def HighLevelStreamName(self):
		"""The name of the high level stream

		Returns:
			str
		"""
		return self._get_attribute('highLevelStreamName')

	@property
	def InterPacketGapUnitsType(self):
		"""

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('interPacketGapUnitsType')
	@InterPacketGapUnitsType.setter
	def InterPacketGapUnitsType(self, value):
		self._set_attribute('interPacketGapUnitsType', value)

	@property
	def OverSubscribed(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('overSubscribed')

	@property
	def Rate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('rate')
	@Rate.setter
	def Rate(self, value):
		self._set_attribute('rate', value)

	@property
	def RateType(self):
		"""

		Returns:
			str(bitsPerSecond|framesPerSecond|interPacketGap|percentLineRate)
		"""
		return self._get_attribute('rateType')
	@RateType.setter
	def RateType(self, value):
		self._set_attribute('rateType', value)

	@property
	def TrafficItemName(self):
		"""The name of the parent traffic item.

		Returns:
			str
		"""
		return self._get_attribute('trafficItemName')

	@property
	def TxPort(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('txPort')

	def find(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, HighLevelStreamName=None, InterPacketGapUnitsType=None, OverSubscribed=None, Rate=None, RateType=None, TrafficItemName=None, TxPort=None):
		"""Finds and retrieves dynamicRate data from the server.

		All named parameters support regex and can be used to selectively retrieve dynamicRate data from the server.
		By default the find method takes no parameters and will retrieve all dynamicRate data from the server.

		Args:
			BitRateUnitsType (str(bitsPerSec|bytesPerSec|kbitsPerSec|kbytesPerSec|mbitsPerSec|mbytesPerSec)): 
			EnforceMinimumInterPacketGap (number): 
			HighLevelStreamName (str): The name of the high level stream
			InterPacketGapUnitsType (str(bytes|nanoseconds)): 
			OverSubscribed (bool): 
			Rate (number): 
			RateType (str(bitsPerSecond|framesPerSecond|interPacketGap|percentLineRate)): 
			TrafficItemName (str): The name of the parent traffic item.
			TxPort (number): 

		Returns:
			self: This instance with found dynamicRate data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
