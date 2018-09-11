from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Filter(Base):
	"""The Filter class encapsulates a required filter node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Filter property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'filter'

	def __init__(self, parent):
		super(Filter, self).__init__(parent)

	@property
	def CaptureFilterDA(self):
		"""

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureFilterDA')
	@CaptureFilterDA.setter
	def CaptureFilterDA(self, value):
		self._set_attribute('captureFilterDA', value)

	@property
	def CaptureFilterEnable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('captureFilterEnable')
	@CaptureFilterEnable.setter
	def CaptureFilterEnable(self, value):
		self._set_attribute('captureFilterEnable', value)

	@property
	def CaptureFilterError(self):
		"""

		Returns:
			str(errAnyFrame|errAnyIpTcpUdpChecksumError|errAnySequencekError|errBadCRC|errBadFrame|errBigSequenceError|errDataIntegrityError|errGoodFrame|errInvalidFcoeFrame|errReverseSequenceError|errSmallSequenceError)
		"""
		return self._get_attribute('captureFilterError')
	@CaptureFilterError.setter
	def CaptureFilterError(self, value):
		self._set_attribute('captureFilterError', value)

	@property
	def CaptureFilterExpressionString(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('captureFilterExpressionString')
	@CaptureFilterExpressionString.setter
	def CaptureFilterExpressionString(self, value):
		self._set_attribute('captureFilterExpressionString', value)

	@property
	def CaptureFilterFrameSizeEnable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('captureFilterFrameSizeEnable')
	@CaptureFilterFrameSizeEnable.setter
	def CaptureFilterFrameSizeEnable(self, value):
		self._set_attribute('captureFilterFrameSizeEnable', value)

	@property
	def CaptureFilterFrameSizeFrom(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('captureFilterFrameSizeFrom')
	@CaptureFilterFrameSizeFrom.setter
	def CaptureFilterFrameSizeFrom(self, value):
		self._set_attribute('captureFilterFrameSizeFrom', value)

	@property
	def CaptureFilterFrameSizeTo(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('captureFilterFrameSizeTo')
	@CaptureFilterFrameSizeTo.setter
	def CaptureFilterFrameSizeTo(self, value):
		self._set_attribute('captureFilterFrameSizeTo', value)

	@property
	def CaptureFilterPattern(self):
		"""

		Returns:
			str(anyPattern|notPattern1|notPattern2|pattern1|pattern1AndPattern2|pattern2)
		"""
		return self._get_attribute('captureFilterPattern')
	@CaptureFilterPattern.setter
	def CaptureFilterPattern(self, value):
		self._set_attribute('captureFilterPattern', value)

	@property
	def CaptureFilterSA(self):
		"""

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureFilterSA')
	@CaptureFilterSA.setter
	def CaptureFilterSA(self, value):
		self._set_attribute('captureFilterSA', value)
