from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class StatRequest(Base):
	"""The StatRequest class encapsulates a user managed statRequest node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the StatRequest property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'statRequest'

	def __init__(self, parent):
		super(StatRequest, self).__init__(parent)

	@property
	def Pattern(self):
		"""An instance of the Pattern class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.pattern.pattern.Pattern)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.pattern.pattern import Pattern
		return Pattern(self)

	@property
	def Filter(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)
		"""
		return self._get_attribute('filter')
	@Filter.setter
	def Filter(self, value):
		self._set_attribute('filter', value)

	@property
	def FilterItems(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])
		"""
		return self._get_attribute('filterItems')
	@FilterItems.setter
	def FilterItems(self, value):
		self._set_attribute('filterItems', value)

	@property
	def IsReady(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isReady')

	@property
	def MaxWaitTime(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('maxWaitTime')
	@MaxWaitTime.setter
	def MaxWaitTime(self, value):
		self._set_attribute('maxWaitTime', value)

	@property
	def Source(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)
		"""
		return self._get_attribute('source')
	@Source.setter
	def Source(self, value):
		self._set_attribute('source', value)

	@property
	def Stats(self):
		"""

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*],arg2:str[average|averageRate|countDistinct|delta|divSum|first|intervalAverage|max|maxRate|min|minRate|none|positiveAverageRate|positiveMaxRate|positiveMinRate|positiveRate|rate|runStateAgg|runStateAggIgnoreRamp|standardDeviation|sum|vectorMax|vectorMin|weightedAverage]))
		"""
		return self._get_attribute('stats')
	@Stats.setter
	def Stats(self, value):
		self._set_attribute('stats', value)

	@property
	def Values(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])
		"""
		return self._get_attribute('values')

	def add(self, Filter=None, FilterItems=None, MaxWaitTime=None, Source=None, Stats=None):
		"""Adds a new statRequest node on the server and retrieves it in this instance.

		Args:
			Filter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			FilterItems (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 
			MaxWaitTime (number): 
			Source (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			Stats (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*],arg2:str[average|averageRate|countDistinct|delta|divSum|first|intervalAverage|max|maxRate|min|minRate|none|positiveAverageRate|positiveMaxRate|positiveMinRate|positiveRate|rate|runStateAgg|runStateAggIgnoreRamp|standardDeviation|sum|vectorMax|vectorMin|weightedAverage]))): 

		Returns:
			self: This instance with all currently retrieved statRequest data using find and the newly added statRequest data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the statRequest data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Filter=None, FilterItems=None, IsReady=None, MaxWaitTime=None, Source=None, Stats=None, Values=None):
		"""Finds and retrieves statRequest data from the server.

		All named parameters support regex and can be used to selectively retrieve statRequest data from the server.
		By default the find method takes no parameters and will retrieve all statRequest data from the server.

		Args:
			Filter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			FilterItems (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 
			IsReady (bool): 
			MaxWaitTime (number): 
			Source (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			Stats (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*],arg2:str[average|averageRate|countDistinct|delta|divSum|first|intervalAverage|max|maxRate|min|minRate|none|positiveAverageRate|positiveMaxRate|positiveMinRate|positiveRate|rate|runStateAgg|runStateAggIgnoreRamp|standardDeviation|sum|vectorMax|vectorMin|weightedAverage]))): 
			Values (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 

		Returns:
			self: This instance with found statRequest data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def GetStats(self):
		"""Executes the getStats operation on the server.

		Args:
			Arg1 (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=statRequest)): The method internally set Arg1 to the current href for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('GetStats', payload=locals(), response_object=None)
