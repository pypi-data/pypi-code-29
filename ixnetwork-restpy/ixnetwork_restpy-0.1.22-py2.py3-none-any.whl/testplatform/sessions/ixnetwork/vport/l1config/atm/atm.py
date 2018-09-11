from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Atm(Base):
	"""The Atm class encapsulates a required atm node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Atm property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'atm'

	def __init__(self, parent):
		super(Atm, self).__init__(parent)

	@property
	def C2Expected(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('c2Expected')
	@C2Expected.setter
	def C2Expected(self, value):
		self._set_attribute('c2Expected', value)

	@property
	def C2Tx(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('c2Tx')
	@C2Tx.setter
	def C2Tx(self, value):
		self._set_attribute('c2Tx', value)

	@property
	def CellHeader(self):
		"""

		Returns:
			str(nni|uni)
		"""
		return self._get_attribute('cellHeader')
	@CellHeader.setter
	def CellHeader(self, value):
		self._set_attribute('cellHeader', value)

	@property
	def CosetActive(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('cosetActive')
	@CosetActive.setter
	def CosetActive(self, value):
		self._set_attribute('cosetActive', value)

	@property
	def CrcSize(self):
		"""

		Returns:
			str(crc16|crc32)
		"""
		return self._get_attribute('crcSize')
	@CrcSize.setter
	def CrcSize(self, value):
		self._set_attribute('crcSize', value)

	@property
	def DataScrambling(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('dataScrambling')
	@DataScrambling.setter
	def DataScrambling(self, value):
		self._set_attribute('dataScrambling', value)

	@property
	def EnablePPM(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enablePPM')
	@EnablePPM.setter
	def EnablePPM(self, value):
		self._set_attribute('enablePPM', value)

	@property
	def FillerCell(self):
		"""

		Returns:
			str(idle|unassigned)
		"""
		return self._get_attribute('fillerCell')
	@FillerCell.setter
	def FillerCell(self, value):
		self._set_attribute('fillerCell', value)

	@property
	def InterfaceType(self):
		"""

		Returns:
			str(oc12|oc3|stm1|stm4)
		"""
		return self._get_attribute('interfaceType')
	@InterfaceType.setter
	def InterfaceType(self, value):
		self._set_attribute('interfaceType', value)

	@property
	def Loopback(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def PatternMatching(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('patternMatching')
	@PatternMatching.setter
	def PatternMatching(self, value):
		self._set_attribute('patternMatching', value)

	@property
	def Ppm(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ppm')
	@Ppm.setter
	def Ppm(self, value):
		self._set_attribute('ppm', value)

	@property
	def ReassemblyTimeout(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('reassemblyTimeout')
	@ReassemblyTimeout.setter
	def ReassemblyTimeout(self, value):
		self._set_attribute('reassemblyTimeout', value)

	@property
	def TransmitClocking(self):
		"""

		Returns:
			str(external|internal|recovered)
		"""
		return self._get_attribute('transmitClocking')
	@TransmitClocking.setter
	def TransmitClocking(self, value):
		self._set_attribute('transmitClocking', value)
