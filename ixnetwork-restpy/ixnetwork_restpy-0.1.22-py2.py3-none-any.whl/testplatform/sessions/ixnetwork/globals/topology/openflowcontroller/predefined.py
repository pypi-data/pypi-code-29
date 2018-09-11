from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Predefined(Base):
	"""The Predefined class encapsulates a user managed predefined node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Predefined property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'predefined'

	def __init__(self, parent):
		super(Predefined, self).__init__(parent)

	@property
	def FlowTemplate(self):
		"""An instance of the FlowTemplate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.flowtemplate.FlowTemplate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.flowtemplate import FlowTemplate
		return FlowTemplate(self)

	def add(self):
		"""Adds a new predefined node on the server and retrieves it in this instance.

		Returns:
			self: This instance with all currently retrieved predefined data using find and the newly added predefined data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the predefined data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self):
		"""Finds and retrieves predefined data from the server.

		All named parameters support regex and can be used to selectively retrieve predefined data from the server.
		By default the find method takes no parameters and will retrieve all predefined data from the server.

		Returns:
			self: This instance with found predefined data from the server available through an iterator or index

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
