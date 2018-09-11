from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NetTopologyFatTree(Base):
	"""The NetTopologyFatTree class encapsulates a user managed netTopologyFatTree node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the NetTopologyFatTree property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'netTopologyFatTree'

	def __init__(self, parent):
		super(NetTopologyFatTree, self).__init__(parent)

	@property
	def Level(self):
		"""An instance of the Level class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.level.Level)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.level import Level
		return Level(self)

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
	def LevelCount(self):
		"""Number of Levels

		Returns:
			number
		"""
		return self._get_attribute('levelCount')
	@LevelCount.setter
	def LevelCount(self, value):
		self._set_attribute('levelCount', value)

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

	def add(self, IncludeEntryPoint=None, LevelCount=None, LinkMultiplier=None):
		"""Adds a new netTopologyFatTree node on the server and retrieves it in this instance.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LevelCount (number): Number of Levels
			LinkMultiplier (number): number of links between two nodes

		Returns:
			self: This instance with all currently retrieved netTopologyFatTree data using find and the newly added netTopologyFatTree data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the netTopologyFatTree data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, IncludeEntryPoint=None, LevelCount=None, LinkMultiplier=None):
		"""Finds and retrieves netTopologyFatTree data from the server.

		All named parameters support regex and can be used to selectively retrieve netTopologyFatTree data from the server.
		By default the find method takes no parameters and will retrieve all netTopologyFatTree data from the server.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LevelCount (number): Number of Levels
			LinkMultiplier (number): number of links between two nodes

		Returns:
			self: This instance with found netTopologyFatTree data from the server available through an iterator or index

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
