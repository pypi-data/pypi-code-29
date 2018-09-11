from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DynamicUpdate(Base):
	"""The DynamicUpdate class encapsulates a system managed dynamicUpdate node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DynamicUpdate property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'dynamicUpdate'

	def __init__(self, parent):
		super(DynamicUpdate, self).__init__(parent)

	@property
	def AvailableDynamicUpdateFields(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableDynamicUpdateFields')

	@property
	def AvailableSessionAwareTrafficFields(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableSessionAwareTrafficFields')

	@property
	def EnabledDynamicUpdateFields(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('enabledDynamicUpdateFields')
	@EnabledDynamicUpdateFields.setter
	def EnabledDynamicUpdateFields(self, value):
		self._set_attribute('enabledDynamicUpdateFields', value)

	@property
	def EnabledDynamicUpdateFieldsDisplayNames(self):
		"""Returns user friendly list of dynamic update fields

		Returns:
			list(str)
		"""
		return self._get_attribute('enabledDynamicUpdateFieldsDisplayNames')

	@property
	def EnabledSessionAwareTrafficFields(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('enabledSessionAwareTrafficFields')
	@EnabledSessionAwareTrafficFields.setter
	def EnabledSessionAwareTrafficFields(self, value):
		self._set_attribute('enabledSessionAwareTrafficFields', value)

	def find(self, AvailableDynamicUpdateFields=None, AvailableSessionAwareTrafficFields=None, EnabledDynamicUpdateFields=None, EnabledDynamicUpdateFieldsDisplayNames=None, EnabledSessionAwareTrafficFields=None):
		"""Finds and retrieves dynamicUpdate data from the server.

		All named parameters support regex and can be used to selectively retrieve dynamicUpdate data from the server.
		By default the find method takes no parameters and will retrieve all dynamicUpdate data from the server.

		Args:
			AvailableDynamicUpdateFields (list(str)): 
			AvailableSessionAwareTrafficFields (list(str)): 
			EnabledDynamicUpdateFields (list(str)): 
			EnabledDynamicUpdateFieldsDisplayNames (list(str)): Returns user friendly list of dynamic update fields
			EnabledSessionAwareTrafficFields (list(str)): 

		Returns:
			self: This instance with found dynamicUpdate data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
