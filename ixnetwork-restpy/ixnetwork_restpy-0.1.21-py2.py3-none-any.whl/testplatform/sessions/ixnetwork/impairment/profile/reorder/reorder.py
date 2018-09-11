from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Reorder(Base):
	"""The Reorder class encapsulates a required reorder node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Reorder property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'reorder'

	def __init__(self, parent):
		super(Reorder, self).__init__(parent)

	@property
	def ClusterSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('clusterSize')
	@ClusterSize.setter
	def ClusterSize(self, value):
		self._set_attribute('clusterSize', value)

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
	def PercentRate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('percentRate')
	@PercentRate.setter
	def PercentRate(self, value):
		self._set_attribute('percentRate', value)

	@property
	def SkipCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('skipCount')
	@SkipCount.setter
	def SkipCount(self, value):
		self._set_attribute('skipCount', value)
