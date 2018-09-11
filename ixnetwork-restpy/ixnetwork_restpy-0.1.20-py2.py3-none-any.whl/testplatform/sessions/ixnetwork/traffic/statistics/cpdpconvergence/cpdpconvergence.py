from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CpdpConvergence(Base):
	"""The CpdpConvergence class encapsulates a required cpdpConvergence node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the CpdpConvergence property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'cpdpConvergence'

	def __init__(self, parent):
		super(CpdpConvergence, self).__init__(parent)

	@property
	def DataPlaneJitterWindow(self):
		"""

		Returns:
			str(0|10485760|1310720|167772160|20971520|2621440|335544320|41943040|5242880|671088640|83886080)
		"""
		return self._get_attribute('dataPlaneJitterWindow')
	@DataPlaneJitterWindow.setter
	def DataPlaneJitterWindow(self, value):
		self._set_attribute('dataPlaneJitterWindow', value)

	@property
	def DataPlaneThreshold(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('dataPlaneThreshold')
	@DataPlaneThreshold.setter
	def DataPlaneThreshold(self, value):
		self._set_attribute('dataPlaneThreshold', value)

	@property
	def EnableControlPlaneEvents(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableControlPlaneEvents')
	@EnableControlPlaneEvents.setter
	def EnableControlPlaneEvents(self, value):
		self._set_attribute('enableControlPlaneEvents', value)

	@property
	def EnableDataPlaneEventsRateMonitor(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableDataPlaneEventsRateMonitor')
	@EnableDataPlaneEventsRateMonitor.setter
	def EnableDataPlaneEventsRateMonitor(self, value):
		self._set_attribute('enableDataPlaneEventsRateMonitor', value)

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
