from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FlowSet(Base):
	"""The FlowSet class encapsulates a system managed flowSet node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the FlowSet property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'flowSet'

	def __init__(self, parent):
		super(FlowSet, self).__init__(parent)

	@property
	def FlowProfile(self):
		"""An instance of the FlowProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowprofile.FlowProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowprofile import FlowProfile
		return FlowProfile(self)._select()

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Cookie(self):
		"""Cookie of the flow entry that was looked up. This is the opaque controller-issued identifier.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('cookie')

	@property
	def CookieMask(self):
		"""The mask used to restrict the cookie bits.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('cookieMask')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def FlowAdvertise(self):
		"""If selected, the flows are advertised by the OF Channel.

		Returns:
			bool
		"""
		return self._get_attribute('flowAdvertise')
	@FlowAdvertise.setter
	def FlowAdvertise(self, value):
		self._set_attribute('flowAdvertise', value)

	@property
	def FlowFlags(self):
		"""Allows to configure the Flow Flags. Options are: 1) Send Flow Removed 2) Check Overlap 3) Reset Counts 4) No Packet Count 5) No Byte Count

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flowFlags')

	@property
	def FlowMatchType(self):
		"""The type of match to be configured. Options include the following: 1) Strict 2) Loose

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flowMatchType')

	@property
	def FlowSetId(self):
		"""Specify the controller Flow Set identifier.

		Returns:
			str
		"""
		return self._get_attribute('flowSetId')
	@FlowSetId.setter
	def FlowSetId(self, value):
		self._set_attribute('flowSetId', value)

	@property
	def HardTimeout(self):
		"""The inactive time in seconds after which the Flow range will hard timeout and close.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hardTimeout')

	@property
	def IdleTimeout(self):
		"""The inactive time in seconds after which the Flow range will timeout and become idle.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('idleTimeout')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NumberOfFlows(self):
		"""The number of flows to be configured for the controller table.

		Returns:
			number
		"""
		return self._get_attribute('numberOfFlows')
	@NumberOfFlows.setter
	def NumberOfFlows(self, value):
		self._set_attribute('numberOfFlows', value)

	@property
	def Priority(self):
		"""The priority level for the Flow Range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('priority')

	def find(self, Count=None, DescriptiveName=None, FlowAdvertise=None, FlowSetId=None, Name=None, NumberOfFlows=None):
		"""Finds and retrieves flowSet data from the server.

		All named parameters support regex and can be used to selectively retrieve flowSet data from the server.
		By default the find method takes no parameters and will retrieve all flowSet data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
			FlowSetId (str): Specify the controller Flow Set identifier.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfFlows (number): The number of flows to be configured for the controller table.

		Returns:
			self: This instance with found flowSet data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def FetchAndUpdateConfigFromCloud(self, Mode):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		Args:
			Arg1 (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=*|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): The method internally set Arg1 to the current href for this instance
			Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('FetchAndUpdateConfigFromCloud', payload=locals(), response_object=None)
