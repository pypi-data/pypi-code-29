from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DelayVariation(Base):
	"""The DelayVariation class encapsulates a required delayVariation node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DelayVariation property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'delayVariation'

	def __init__(self, parent):
		super(DelayVariation, self).__init__(parent)

	@property
	def Distribution(self):
		"""

		Returns:
			str(exponential|gaussian|kExponential|kGaussian|kUniform|uniform)
		"""
		return self._get_attribute('distribution')
	@Distribution.setter
	def Distribution(self, value):
		self._set_attribute('distribution', value)

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
	def ExponentialMeanArrival(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('exponentialMeanArrival')
	@ExponentialMeanArrival.setter
	def ExponentialMeanArrival(self, value):
		self._set_attribute('exponentialMeanArrival', value)

	@property
	def GaussianStandardDeviation(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('gaussianStandardDeviation')
	@GaussianStandardDeviation.setter
	def GaussianStandardDeviation(self, value):
		self._set_attribute('gaussianStandardDeviation', value)

	@property
	def UniformSpread(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('uniformSpread')
	@UniformSpread.setter
	def UniformSpread(self, value):
		self._set_attribute('uniformSpread', value)

	@property
	def Units(self):
		"""

		Returns:
			str(kilometers|kKilometers|kMicroseconds|kMilliseconds|kSeconds|microseconds|milliseconds|seconds)
		"""
		return self._get_attribute('units')
	@Units.setter
	def Units(self, value):
		self._set_attribute('units', value)
