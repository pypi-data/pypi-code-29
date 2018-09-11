from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Chassis(Base):
	"""The Chassis class encapsulates a user managed chassis node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Chassis property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'chassis'

	def __init__(self, parent):
		super(Chassis, self).__init__(parent)

	@property
	def Card(self):
		"""An instance of the Card class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card.Card)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card import Card
		return Card(self)

	@property
	def CableLength(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('cableLength')
	@CableLength.setter
	def CableLength(self, value):
		self._set_attribute('cableLength', value)

	@property
	def ChainTopology(self):
		"""

		Returns:
			str(daisy|none|star)
		"""
		return self._get_attribute('chainTopology')
	@ChainTopology.setter
	def ChainTopology(self, value):
		self._set_attribute('chainTopology', value)

	@property
	def ChassisType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('chassisType')

	@property
	def ChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('chassisVersion')

	@property
	def ConnectRetries(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('connectRetries')

	@property
	def Hostname(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('hostname')
	@Hostname.setter
	def Hostname(self, value):
		self._set_attribute('hostname', value)

	@property
	def Ip(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ip')

	@property
	def IsLicensesRetrieved(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isLicensesRetrieved')

	@property
	def IsMaster(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isMaster')

	@property
	def IxnBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnBuildNumber')

	@property
	def IxosBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixosBuildNumber')

	@property
	def LicenseErrors(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('licenseErrors')

	@property
	def MasterChassis(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('masterChassis')
	@MasterChassis.setter
	def MasterChassis(self, value):
		self._set_attribute('masterChassis', value)

	@property
	def ProtocolBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('protocolBuildNumber')

	@property
	def SequenceId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('sequenceId')
	@SequenceId.setter
	def SequenceId(self, value):
		self._set_attribute('sequenceId', value)

	@property
	def State(self):
		"""

		Returns:
			str(down|down|polling|polling|polling|ready)
		"""
		return self._get_attribute('state')

	def add(self, CableLength=None, ChainTopology=None, Hostname=None, MasterChassis=None, SequenceId=None):
		"""Adds a new chassis node on the server and retrieves it in this instance.

		Args:
			CableLength (number): 
			ChainTopology (str(daisy|none|star)): 
			Hostname (str): 
			MasterChassis (str): 
			SequenceId (number): 

		Returns:
			self: This instance with all currently retrieved chassis data using find and the newly added chassis data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the chassis data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, CableLength=None, ChainTopology=None, ChassisType=None, ChassisVersion=None, ConnectRetries=None, Hostname=None, Ip=None, IsLicensesRetrieved=None, IsMaster=None, IxnBuildNumber=None, IxosBuildNumber=None, LicenseErrors=None, MasterChassis=None, ProtocolBuildNumber=None, SequenceId=None, State=None):
		"""Finds and retrieves chassis data from the server.

		All named parameters support regex and can be used to selectively retrieve chassis data from the server.
		By default the find method takes no parameters and will retrieve all chassis data from the server.

		Args:
			CableLength (number): 
			ChainTopology (str(daisy|none|star)): 
			ChassisType (str): 
			ChassisVersion (str): 
			ConnectRetries (number): 
			Hostname (str): 
			Ip (str): 
			IsLicensesRetrieved (bool): 
			IsMaster (bool): 
			IxnBuildNumber (str): 
			IxosBuildNumber (str): 
			LicenseErrors (list(str)): 
			MasterChassis (str): 
			ProtocolBuildNumber (str): 
			SequenceId (number): 
			State (str(down|down|polling|polling|polling|ready)): 

		Returns:
			self: This instance with found chassis data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def GetTapSettings(self):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for the given chassis

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis])): The method internally sets Arg1 to the encapsulated list of hrefs for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self
		return self._execute('GetTapSettings', payload=locals(), response_object=None)

	def RefreshInfo(self):
		"""Executes the refreshInfo operation on the server.

		Refresh the hardware information.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=card])): The method internally sets Arg1 to the encapsulated list of hrefs for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self
		return self._execute('RefreshInfo', payload=locals(), response_object=None)

	def SetTapSettings(self):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for the given chassis.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis])): The method internally sets Arg1 to the encapsulated list of hrefs for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self
		return self._execute('SetTapSettings', payload=locals(), response_object=None)
