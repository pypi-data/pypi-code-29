from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Udf(Base):
	"""The Udf class encapsulates a system managed udf node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Udf property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'udf'

	def __init__(self, parent):
		super(Udf, self).__init__(parent)

	@property
	def Counter(self):
		"""An instance of the Counter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter.Counter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter import Counter
		return Counter(self)

	@property
	def Ipv4(self):
		"""An instance of the Ipv4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4.Ipv4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4 import Ipv4
		return Ipv4(self)

	@property
	def NestedCounter(self):
		"""An instance of the NestedCounter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter.NestedCounter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter import NestedCounter
		return NestedCounter(self)

	@property
	def Random(self):
		"""An instance of the Random class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random.Random)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random import Random
		return Random(self)

	@property
	def RangeList(self):
		"""An instance of the RangeList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist.RangeList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist import RangeList
		return RangeList(self)

	@property
	def ValueList(self):
		"""An instance of the ValueList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist.ValueList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist import ValueList
		return ValueList(self)

	@property
	def ByteOffset(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('byteOffset')
	@ByteOffset.setter
	def ByteOffset(self, value):
		self._set_attribute('byteOffset', value)

	@property
	def Chained(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('chained')

	@property
	def ChainedFromUdf(self):
		"""

		Returns:
			str(none|udf1|udf2|udf3|udf4|udf5)
		"""
		return self._get_attribute('chainedFromUdf')
	@ChainedFromUdf.setter
	def ChainedFromUdf(self, value):
		self._set_attribute('chainedFromUdf', value)

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
	def Type(self):
		"""

		Returns:
			str(counter|ipv4|nestedCounter|random|rangeList|valueList)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	def find(self, ByteOffset=None, Chained=None, ChainedFromUdf=None, Enabled=None, Type=None):
		"""Finds and retrieves udf data from the server.

		All named parameters support regex and can be used to selectively retrieve udf data from the server.
		By default the find method takes no parameters and will retrieve all udf data from the server.

		Args:
			ByteOffset (number): 
			Chained (bool): 
			ChainedFromUdf (str(none|udf1|udf2|udf3|udf4|udf5)): 
			Enabled (bool): 
			Type (str(counter|ipv4|nestedCounter|random|rangeList|valueList)): 

		Returns:
			self: This instance with found udf data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
