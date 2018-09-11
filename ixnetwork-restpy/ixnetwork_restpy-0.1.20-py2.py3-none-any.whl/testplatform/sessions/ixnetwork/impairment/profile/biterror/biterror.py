from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BitError(Base):
	"""The BitError class encapsulates a required bitError node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the BitError property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'bitError'

	def __init__(self, parent):
		super(BitError, self).__init__(parent)

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
	def LogRate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('logRate')
	@LogRate.setter
	def LogRate(self, value):
		self._set_attribute('logRate', value)

	@property
	def SkipEndOctets(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('skipEndOctets')
	@SkipEndOctets.setter
	def SkipEndOctets(self, value):
		self._set_attribute('skipEndOctets', value)

	@property
	def SkipStartOctets(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('skipStartOctets')
	@SkipStartOctets.setter
	def SkipStartOctets(self, value):
		self._set_attribute('skipStartOctets', value)
