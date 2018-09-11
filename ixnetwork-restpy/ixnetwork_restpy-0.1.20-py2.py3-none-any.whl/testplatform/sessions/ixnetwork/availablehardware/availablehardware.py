from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableHardware(Base):
	"""The AvailableHardware class encapsulates a required availableHardware node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AvailableHardware property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'availableHardware'

	def __init__(self, parent):
		super(AvailableHardware, self).__init__(parent)

	@property
	def Chassis(self):
		"""An instance of the Chassis class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis.Chassis)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis import Chassis
		return Chassis(self)

	@property
	def VirtualChassis(self):
		"""An instance of the VirtualChassis class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis.VirtualChassis)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis import VirtualChassis
		return VirtualChassis(self)._select()

	@property
	def IsLocked(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isLocked')

	@property
	def IsOffChassis(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isOffChassis')
	@IsOffChassis.setter
	def IsOffChassis(self, value):
		self._set_attribute('isOffChassis', value)

	@property
	def OffChassisHwM(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('offChassisHwM')
	@OffChassisHwM.setter
	def OffChassisHwM(self, value):
		self._set_attribute('offChassisHwM', value)
