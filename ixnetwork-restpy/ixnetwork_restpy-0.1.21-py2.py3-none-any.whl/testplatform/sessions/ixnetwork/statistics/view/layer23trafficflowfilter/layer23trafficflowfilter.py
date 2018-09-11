from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Layer23TrafficFlowFilter(Base):
	"""The Layer23TrafficFlowFilter class encapsulates a user managed layer23TrafficFlowFilter node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Layer23TrafficFlowFilter property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'layer23TrafficFlowFilter'

	def __init__(self, parent):
		super(Layer23TrafficFlowFilter, self).__init__(parent)

	@property
	def EnumerationFilter(self):
		"""An instance of the EnumerationFilter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter.EnumerationFilter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter import EnumerationFilter
		return EnumerationFilter(self)

	@property
	def TrackingFilter(self):
		"""An instance of the TrackingFilter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter.TrackingFilter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter import TrackingFilter
		return TrackingFilter(self)

	@property
	def AggregatedAcrossPorts(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('aggregatedAcrossPorts')
	@AggregatedAcrossPorts.setter
	def AggregatedAcrossPorts(self, value):
		self._set_attribute('aggregatedAcrossPorts', value)

	@property
	def EgressLatencyBinDisplayOption(self):
		"""

		Returns:
			str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)
		"""
		return self._get_attribute('egressLatencyBinDisplayOption')
	@EgressLatencyBinDisplayOption.setter
	def EgressLatencyBinDisplayOption(self, value):
		self._set_attribute('egressLatencyBinDisplayOption', value)

	@property
	def PortFilterIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])
		"""
		return self._get_attribute('portFilterIds')
	@PortFilterIds.setter
	def PortFilterIds(self, value):
		self._set_attribute('portFilterIds', value)

	@property
	def TrafficItemFilterId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)
		"""
		return self._get_attribute('trafficItemFilterId')
	@TrafficItemFilterId.setter
	def TrafficItemFilterId(self, value):
		self._set_attribute('trafficItemFilterId', value)

	@property
	def TrafficItemFilterIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])
		"""
		return self._get_attribute('trafficItemFilterIds')
	@TrafficItemFilterIds.setter
	def TrafficItemFilterIds(self, value):
		self._set_attribute('trafficItemFilterIds', value)

	def add(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
		"""Adds a new layer23TrafficFlowFilter node on the server and retrieves it in this instance.

		Args:
			AggregatedAcrossPorts (bool): 
			EgressLatencyBinDisplayOption (str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)): 
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 
			TrafficItemFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])): 

		Returns:
			self: This instance with all currently retrieved layer23TrafficFlowFilter data using find and the newly added layer23TrafficFlowFilter data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the layer23TrafficFlowFilter data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
		"""Finds and retrieves layer23TrafficFlowFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve layer23TrafficFlowFilter data from the server.
		By default the find method takes no parameters and will retrieve all layer23TrafficFlowFilter data from the server.

		Args:
			AggregatedAcrossPorts (bool): 
			EgressLatencyBinDisplayOption (str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)): 
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 
			TrafficItemFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])): 

		Returns:
			self: This instance with found layer23TrafficFlowFilter data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
