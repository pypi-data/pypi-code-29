from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Trigger(Base):
	"""The Trigger class encapsulates a required trigger node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Trigger property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'trigger'

	def __init__(self, parent):
		super(Trigger, self).__init__(parent)

	@property
	def CaptureTriggerDA(self):
		"""

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureTriggerDA')
	@CaptureTriggerDA.setter
	def CaptureTriggerDA(self, value):
		self._set_attribute('captureTriggerDA', value)

	@property
	def CaptureTriggerEnable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('captureTriggerEnable')
	@CaptureTriggerEnable.setter
	def CaptureTriggerEnable(self, value):
		self._set_attribute('captureTriggerEnable', value)

	@property
	def CaptureTriggerError(self):
		"""

		Returns:
			str(errAnyFrame|errAnyIpTcpUdpChecksumError|errAnySequencekError|errBadCRC|errBadFrame|errBigSequenceError|errDataIntegrityError|errGoodFrame|errInvalidFcoeFrame|errReverseSequenceError|errSmallSequenceError)
		"""
		return self._get_attribute('captureTriggerError')
	@CaptureTriggerError.setter
	def CaptureTriggerError(self, value):
		self._set_attribute('captureTriggerError', value)

	@property
	def CaptureTriggerExpressionString(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('captureTriggerExpressionString')
	@CaptureTriggerExpressionString.setter
	def CaptureTriggerExpressionString(self, value):
		self._set_attribute('captureTriggerExpressionString', value)

	@property
	def CaptureTriggerFrameSizeEnable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('captureTriggerFrameSizeEnable')
	@CaptureTriggerFrameSizeEnable.setter
	def CaptureTriggerFrameSizeEnable(self, value):
		self._set_attribute('captureTriggerFrameSizeEnable', value)

	@property
	def CaptureTriggerFrameSizeFrom(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('captureTriggerFrameSizeFrom')
	@CaptureTriggerFrameSizeFrom.setter
	def CaptureTriggerFrameSizeFrom(self, value):
		self._set_attribute('captureTriggerFrameSizeFrom', value)

	@property
	def CaptureTriggerFrameSizeTo(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('captureTriggerFrameSizeTo')
	@CaptureTriggerFrameSizeTo.setter
	def CaptureTriggerFrameSizeTo(self, value):
		self._set_attribute('captureTriggerFrameSizeTo', value)

	@property
	def CaptureTriggerPattern(self):
		"""

		Returns:
			str(anyPattern|notPattern1|notPattern2|pattern1|pattern1AndPattern2|pattern2)
		"""
		return self._get_attribute('captureTriggerPattern')
	@CaptureTriggerPattern.setter
	def CaptureTriggerPattern(self, value):
		self._set_attribute('captureTriggerPattern', value)

	@property
	def CaptureTriggerSA(self):
		"""

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureTriggerSA')
	@CaptureTriggerSA.setter
	def CaptureTriggerSA(self, value):
		self._set_attribute('captureTriggerSA', value)
