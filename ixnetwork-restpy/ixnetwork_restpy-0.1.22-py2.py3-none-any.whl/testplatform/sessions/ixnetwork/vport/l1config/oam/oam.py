from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OAM(Base):
	"""The OAM class encapsulates a required OAM node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the OAM property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'OAM'

	def __init__(self, parent):
		super(OAM, self).__init__(parent)

	@property
	def EnableTlvOption(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableTlvOption')
	@EnableTlvOption.setter
	def EnableTlvOption(self, value):
		self._set_attribute('enableTlvOption', value)

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

	@property
	def IdleTimer(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('idleTimer')
	@IdleTimer.setter
	def IdleTimer(self, value):
		self._set_attribute('idleTimer', value)

	@property
	def LinkEvents(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('linkEvents')
	@LinkEvents.setter
	def LinkEvents(self, value):
		self._set_attribute('linkEvents', value)

	@property
	def Loopback(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def MacAddress(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('macAddress')
	@MacAddress.setter
	def MacAddress(self, value):
		self._set_attribute('macAddress', value)

	@property
	def MaxOAMPDUSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('maxOAMPDUSize')
	@MaxOAMPDUSize.setter
	def MaxOAMPDUSize(self, value):
		self._set_attribute('maxOAMPDUSize', value)

	@property
	def OrganizationUniqueIdentifier(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('organizationUniqueIdentifier')
	@OrganizationUniqueIdentifier.setter
	def OrganizationUniqueIdentifier(self, value):
		self._set_attribute('organizationUniqueIdentifier', value)

	@property
	def TlvType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('tlvType')
	@TlvType.setter
	def TlvType(self, value):
		self._set_attribute('tlvType', value)

	@property
	def TlvValue(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('tlvValue')
	@TlvValue.setter
	def TlvValue(self, value):
		self._set_attribute('tlvValue', value)

	@property
	def VendorSpecificInformation(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('vendorSpecificInformation')
	@VendorSpecificInformation.setter
	def VendorSpecificInformation(self, value):
		self._set_attribute('vendorSpecificInformation', value)
