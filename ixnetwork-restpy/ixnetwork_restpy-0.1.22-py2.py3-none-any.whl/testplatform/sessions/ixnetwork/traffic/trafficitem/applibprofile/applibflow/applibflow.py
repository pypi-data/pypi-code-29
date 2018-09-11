from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AppLibFlow(Base):
	"""The AppLibFlow class encapsulates a system managed appLibFlow node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the AppLibFlow property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'appLibFlow'

	def __init__(self, parent):
		super(AppLibFlow, self).__init__(parent)

	@property
	def Connection(self):
		"""An instance of the Connection class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection.Connection)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection import Connection
		return Connection(self)

	@property
	def Parameter(self):
		"""An instance of the Parameter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter.Parameter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter import Parameter
		return Parameter(self)

	@property
	def ConfigId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('configId')

	@property
	def ConnectionCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('connectionCount')

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def FlowId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('flowId')

	@property
	def FlowSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('flowSize')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def Parameters(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('parameters')

	@property
	def Percentage(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('percentage')
	@Percentage.setter
	def Percentage(self, value):
		self._set_attribute('percentage', value)

	def find(self, ConfigId=None, ConnectionCount=None, Description=None, FlowId=None, FlowSize=None, Name=None, Parameters=None, Percentage=None):
		"""Finds and retrieves appLibFlow data from the server.

		All named parameters support regex and can be used to selectively retrieve appLibFlow data from the server.
		By default the find method takes no parameters and will retrieve all appLibFlow data from the server.

		Args:
			ConfigId (number): 
			ConnectionCount (number): 
			Description (str): 
			FlowId (str): 
			FlowSize (number): 
			Name (str): 
			Parameters (list(str)): 
			Percentage (number): 

		Returns:
			self: This instance with found appLibFlow data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
