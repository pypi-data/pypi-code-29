import pyftdi.gpio
import pyftdi.ftdi
import pyftdi.spi

import abc
import datetime
import time

class ToolError(Exception):
	def __init__(self, message):
		super().__init__(message)

class Tool(metaclass=abc.ABCMeta):
	def __init__(self, url, cs=0, mode=0, freq=1E6):
		"""Configure FT2232x in MPSSE mode

		Args:
			url (:obj:`str`): Device URL
			cs (int, optional): Chip select number to use. Defaults to 0.
			mode (int, optional): SPI protocol mode. Defaults to 0.
			freq (int, optional): Max frequency. Defaults to 1MHz
		"""
		# Define variables
		self._CDONE = 7
		self._CRESET = 8
		self._ENABLE = 4
		self._LED = 11

		# Initialize SPI port
		self._spi_controller = pyftdi.spi.SpiController(cs_count=1)
		self._spi_controller.configure(url)
		self._slave = self._spi_controller.get_port(cs=cs, freq=freq, mode=mode)
		self._gpio = self._spi_controller.get_gpio()

	@abc.abstractmethod
	def _prepare(self):
		"""Configure pins, enable buffers, etc.
		"""
		pass

	@abc.abstractmethod
	def _unprepare(self):
		"""Make all pins inputs, disable buffers, etc.
		"""
		pass

	def _get_cdone(self):
		return bool(self._gpio.read() & (1 << self._CDONE))

	def _set_creset(self, reset):
		self._gpio.write((self._gpio.read() & 0xFEFF) | (reset << self._CRESET))

	def claim_bus(self, timeout=5):
		"""Try to claim the SPI bus using reset sequence

		Args:
			timeout: When to give-up

		Raises:
			ToolError: If the tool failed to claim the bus
		"""

		self._prepare()
		start = datetime.datetime.now()

		# Reset iCE40
		while True:
			self._set_creset(0)
			time.sleep(0.001)
			self._set_creset(1)
			time.sleep(0.001)
			self._set_creset(0)
			time.sleep(0.25)

			# Check cdone
			if self._get_cdone() == False:
				break

			if (datetime.datetime.now() - start)/datetime.timedelta(seconds=1) > timeout:
				spinner.fail()
				raise ToolError("Failed claiming the SPI bus")

	def release_bus(self):
		"""Release the SPI bus
		"""
		self._unprepare()



class ARM_USB_OCD_H(Tool):
	def __init__(self):
		super().__init__("ftdi://olimex:arm-usb-ocd-h/1")

		# LED is always output
		dir = 1 << self._LED
		self._gpio.set_direction(dir, dir)

	def __str__(self):
		return "ARM-USB-OCD-H"

	def _prepare(self):
		"""Prepare ARM-USB-OCD-H

		Make ENABLE and RESET pins output. After that clear ENABLE to enable buffers.
		"""
		# Configure direction
		dir = (1 << self._ENABLE) | (1 << self._CRESET)
		self._gpio.set_direction(dir, dir)

		# Configure values
		self._gpio.write((self._gpio.read() & 0xF7EF) | (1 << self._LED))

	def _unprepare(self):
		"""Unprepare ARM-USB-OCD-H

		Set ENABLE to disable buffer and make all pins inputs
		"""

		# Configure values
		self._gpio.write((self._gpio.read() & 0xF7EF) | (1 << self._ENABLE))

		# Configure direction
		dir = (1 << self._ENABLE) | (1 << self._CRESET)
		self._gpio.set_direction(dir, 0)


class ARM_USB_TINY_H(Tool):
	def __init__(self):
		super().__init__("ftdi://olimex:arm-usb-tiny-h/1")

		# LED is always output
		dir = 1 << self._LED
		self._gpio.set_direction(dir, dir)

	def __str__(self):
		return "ARM-USB-TINY-H"

	def _prepare(self):
		"""Prepare ARM-USB-TINY-H

		Make RESET pin output.
		"""
		# Configure direction
		dir = 1 << self._CRESET
		self._gpio.set_direction(dir, dir)

		# Configure values
		self._gpio.write((self._gpio.read() & 0xF7FF) | (1 << self._LED))

	def _unprepare(self):
		"""Unprepare ARM-USB-TINY-H

		Make all pins inputs
		"""

		# Configure values
		self._gpio.write((self._gpio.read() & 0xF7FF) | 0)

		# Configure direction
		dir = 1 << self._CRESET
		self._gpio.set_direction(dir, 0)
