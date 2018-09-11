from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Tlv(Base):
	"""The Tlv class encapsulates a user managed tlv node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Tlv property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'tlv'

	def __init__(self, parent):
		super(Tlv, self).__init__(parent)

	@property
	def Length(self):
		"""An instance of the Length class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.length.Length)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.length import Length
		return Length(self)._select()

	@property
	def Type(self):
		"""An instance of the Type class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.type.Type)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.type import Type
		return Type(self)._select()

	@property
	def Value(self):
		"""An instance of the Value class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.value.Value)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.value import Value
		return Value(self)._select()

	@property
	def AvailableIncludeInMessages(self):
		"""A list of available messages which are used in the includeInMessages attribute

		Returns:
			list(str)
		"""
		return self._get_attribute('availableIncludeInMessages')

	@property
	def Description(self):
		"""Description of the tlv

		Returns:
			str
		"""
		return self._get_attribute('description')
	@Description.setter
	def Description(self, value):
		self._set_attribute('description', value)

	@property
	def IncludeInMessages(self):
		"""Include the TLV in these protocol messages

		Returns:
			list(str)
		"""
		return self._get_attribute('includeInMessages')
	@IncludeInMessages.setter
	def IncludeInMessages(self, value):
		self._set_attribute('includeInMessages', value)

	@property
	def IsEditable(self):
		"""Indicates whether this is editable or not

		Returns:
			bool
		"""
		return self._get_attribute('isEditable')
	@IsEditable.setter
	def IsEditable(self, value):
		self._set_attribute('isEditable', value)

	@property
	def IsRepeatable(self):
		"""Indicates whether this can be multiplied in the TLV definition

		Returns:
			bool
		"""
		return self._get_attribute('isRepeatable')
	@IsRepeatable.setter
	def IsRepeatable(self, value):
		self._set_attribute('isRepeatable', value)

	@property
	def IsRequired(self):
		"""Flag indicating whether this is required or not

		Returns:
			bool
		"""
		return self._get_attribute('isRequired')
	@IsRequired.setter
	def IsRequired(self, value):
		self._set_attribute('isRequired', value)

	@property
	def Name(self):
		"""Name of the tlv

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	def add(self, Description=None, IncludeInMessages=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
		"""Adds a new tlv node on the server and retrieves it in this instance.

		Args:
			Description (str): Description of the tlv
			IncludeInMessages (list(str)): Include the TLV in these protocol messages
			IsEditable (bool): Indicates whether this is editable or not
			IsRepeatable (bool): Indicates whether this can be multiplied in the TLV definition
			IsRequired (bool): Flag indicating whether this is required or not
			Name (str): Name of the tlv

		Returns:
			self: This instance with all currently retrieved tlv data using find and the newly added tlv data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the tlv data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AvailableIncludeInMessages=None, Description=None, IncludeInMessages=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
		"""Finds and retrieves tlv data from the server.

		All named parameters support regex and can be used to selectively retrieve tlv data from the server.
		By default the find method takes no parameters and will retrieve all tlv data from the server.

		Args:
			AvailableIncludeInMessages (list(str)): A list of available messages which are used in the includeInMessages attribute
			Description (str): Description of the tlv
			IncludeInMessages (list(str)): Include the TLV in these protocol messages
			IsEditable (bool): Indicates whether this is editable or not
			IsRepeatable (bool): Indicates whether this can be multiplied in the TLV definition
			IsRequired (bool): Flag indicating whether this is required or not
			Name (str): Name of the tlv

		Returns:
			self: This instance with found tlv data from the server available through an iterator or index

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
