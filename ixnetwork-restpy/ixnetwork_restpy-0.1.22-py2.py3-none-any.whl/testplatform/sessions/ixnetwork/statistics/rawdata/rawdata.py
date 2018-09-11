from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RawData(Base):
	"""The RawData class encapsulates a required rawData node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the RawData property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'rawData'

	def __init__(self, parent):
		super(RawData, self).__init__(parent)

	@property
	def Statistic(self):
		"""An instance of the Statistic class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic.Statistic)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic import Statistic
		return Statistic(self)

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
	def LastRawDataFolder(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('lastRawDataFolder')

	@property
	def Path(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('path')
	@Path.setter
	def Path(self, value):
		self._set_attribute('path', value)

	def StopCollection(self):
		"""Executes the stopCollection operation on the server.

		Args:
			Arg1 (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=rawData)): The method internally set Arg1 to the current href for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('StopCollection', payload=locals(), response_object=None)
