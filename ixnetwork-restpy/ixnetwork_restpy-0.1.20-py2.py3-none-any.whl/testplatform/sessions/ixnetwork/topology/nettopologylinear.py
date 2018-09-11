from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NetTopologyLinear(Base):
	"""The NetTopologyLinear class encapsulates a user managed netTopologyLinear node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the NetTopologyLinear property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'netTopologyLinear'

	def __init__(self, parent):
		super(NetTopologyLinear, self).__init__(parent)

	@property
	def IncludeEntryPoint(self):
		"""if true, entry node belongs to ring topology, otherwise it is outside of ring

		Returns:
			bool
		"""
		return self._get_attribute('includeEntryPoint')
	@IncludeEntryPoint.setter
	def IncludeEntryPoint(self, value):
		self._set_attribute('includeEntryPoint', value)

	@property
	def LinkMultiplier(self):
		"""number of links between two nodes

		Returns:
			number
		"""
		return self._get_attribute('linkMultiplier')
	@LinkMultiplier.setter
	def LinkMultiplier(self, value):
		self._set_attribute('linkMultiplier', value)

	@property
	def Nodes(self):
		"""number of nodes

		Returns:
			number
		"""
		return self._get_attribute('nodes')
	@Nodes.setter
	def Nodes(self, value):
		self._set_attribute('nodes', value)

	def add(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
		"""Adds a new netTopologyLinear node on the server and retrieves it in this instance.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LinkMultiplier (number): number of links between two nodes
			Nodes (number): number of nodes

		Returns:
			self: This instance with all currently retrieved netTopologyLinear data using find and the newly added netTopologyLinear data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the netTopologyLinear data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
		"""Finds and retrieves netTopologyLinear data from the server.

		All named parameters support regex and can be used to selectively retrieve netTopologyLinear data from the server.
		By default the find method takes no parameters and will retrieve all netTopologyLinear data from the server.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LinkMultiplier (number): number of links between two nodes
			Nodes (number): number of nodes

		Returns:
			self: This instance with found netTopologyLinear data from the server available through an iterator or index

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
