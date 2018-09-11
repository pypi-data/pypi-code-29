from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Checksums(Base):
	"""The Checksums class encapsulates a required checksums node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Checksums property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'checksums'

	def __init__(self, parent):
		super(Checksums, self).__init__(parent)

	@property
	def AlwaysCorrectWhenModifying(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('alwaysCorrectWhenModifying')
	@AlwaysCorrectWhenModifying.setter
	def AlwaysCorrectWhenModifying(self, value):
		self._set_attribute('alwaysCorrectWhenModifying', value)

	@property
	def CorrectTxChecksumOverIp(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('correctTxChecksumOverIp')
	@CorrectTxChecksumOverIp.setter
	def CorrectTxChecksumOverIp(self, value):
		self._set_attribute('correctTxChecksumOverIp', value)

	@property
	def CorrectTxIpv4Checksum(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('correctTxIpv4Checksum')
	@CorrectTxIpv4Checksum.setter
	def CorrectTxIpv4Checksum(self, value):
		self._set_attribute('correctTxIpv4Checksum', value)

	@property
	def CorrectTxL2FcsErrors(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('correctTxL2FcsErrors')
	@CorrectTxL2FcsErrors.setter
	def CorrectTxL2FcsErrors(self, value):
		self._set_attribute('correctTxL2FcsErrors', value)

	@property
	def DropRxL2FcsErrors(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('dropRxL2FcsErrors')
	@DropRxL2FcsErrors.setter
	def DropRxL2FcsErrors(self, value):
		self._set_attribute('dropRxL2FcsErrors', value)
