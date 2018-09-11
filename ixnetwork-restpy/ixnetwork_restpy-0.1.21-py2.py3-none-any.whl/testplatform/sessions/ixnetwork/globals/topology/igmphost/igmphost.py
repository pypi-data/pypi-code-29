from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IgmpHost(Base):
	"""The IgmpHost class encapsulates a required igmpHost node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the IgmpHost property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'igmpHost'

	def __init__(self, parent):
		super(IgmpHost, self).__init__(parent)

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
	def Enabled(self):
		"""Enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enabled')

	@property
	def IPDSCP(self):
		"""Specifies the ToS/DSCP value in the IPv4 Header

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('iPDSCP')

	@property
	def InterStbStartDelay(self):
		"""Time in milliseconds between Join messages from clients within the same range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interStbStartDelay')

	@property
	def IntervalInMs(self):
		"""Time interval used to calculate the rate for triggering an action (rate = count/interval)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('intervalInMs')

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
	def RatePerInterval(self):
		"""No. of Reports triggered per time interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ratePerInterval')

	@property
	def RowNames(self):
		"""Name of rows

		Returns:
			list(str)
		"""
		return self._get_attribute('rowNames')

	@property
	def UnicastMode(self):
		"""Unicast Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unicastMode')

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
