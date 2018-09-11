from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedInfo(Base):
	"""The LearnedInfo class encapsulates a system managed learnedInfo node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the LearnedInfo property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'learnedInfo'

	def __init__(self, parent):
		super(LearnedInfo, self).__init__(parent)

	@property
	def Col(self):
		"""An instance of the Col class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col.Col)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.col import Col
		return Col(self)

	@property
	def Table(self):
		"""An instance of the Table class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.table.Table)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.table import Table
		return Table(self)

	@property
	def __id__(self):
		"""A unique id for the learned information table

		Returns:
			list(str)
		"""
		return self._get_attribute('__id__')

	@property
	def Columns(self):
		"""The list of columns in the learned information table

		Returns:
			list(str)
		"""
		return self._get_attribute('columns')

	@property
	def State(self):
		"""The state of the learned information query

		Returns:
			str
		"""
		return self._get_attribute('state')

	@property
	def Type(self):
		"""The type of learned information

		Returns:
			str
		"""
		return self._get_attribute('type')

	@property
	def Values(self):
		"""A list of rows of learned information values

		Returns:
			list(list[str])
		"""
		return self._get_attribute('values')

	def find(self, __id__=None, Columns=None, State=None, Type=None, Values=None):
		"""Finds and retrieves learnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve learnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all learnedInfo data from the server.

		Args:
			__id__ (list(str)): A unique id for the learned information table
			Columns (list(str)): The list of columns in the learned information table
			State (str): The state of the learned information query
			Type (str): The type of learned information
			Values (list(list[str])): A list of rows of learned information values

		Returns:
			self: This instance with found learnedInfo data from the server available through an iterator or index

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
