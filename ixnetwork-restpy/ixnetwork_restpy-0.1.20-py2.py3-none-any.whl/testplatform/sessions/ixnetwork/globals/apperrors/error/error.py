from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Error(Base):
	"""The Error class encapsulates a system managed error node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Error property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'error'

	def __init__(self, parent):
		super(Error, self).__init__(parent)

	@property
	def Instance(self):
		"""An instance of the Instance class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance.Instance)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance import Instance
		return Instance(self)

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def ErrorCode(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('errorCode')

	@property
	def ErrorLevel(self):
		"""

		Returns:
			str(kAnalysis|kCount|kError|kMessage|kWarning)
		"""
		return self._get_attribute('errorLevel')

	@property
	def InstanceCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('instanceCount')

	@property
	def LastModified(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('lastModified')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def Provider(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('provider')

	@property
	def SourceColumns(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceColumns')

	@property
	def SourceColumnsDisplayName(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceColumnsDisplayName')

	def find(self, Description=None, ErrorCode=None, ErrorLevel=None, InstanceCount=None, LastModified=None, Name=None, Provider=None, SourceColumns=None, SourceColumnsDisplayName=None):
		"""Finds and retrieves error data from the server.

		All named parameters support regex and can be used to selectively retrieve error data from the server.
		By default the find method takes no parameters and will retrieve all error data from the server.

		Args:
			Description (str): 
			ErrorCode (number): 
			ErrorLevel (str(kAnalysis|kCount|kError|kMessage|kWarning)): 
			InstanceCount (number): 
			LastModified (str): 
			Name (str): 
			Provider (str): 
			SourceColumns (list(str)): 
			SourceColumnsDisplayName (list(str)): 

		Returns:
			self: This instance with found error data from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())
